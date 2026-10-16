#!/usr/bin/env python3
"""Fetch aggregate BabyView dataset statistics from Airtable for the website.

Writes _data/bv_summary.json. Only aggregates are written: hours per
dataset per recording week, per-release totals, hours and recording months
per camera model, overall totals, and each BV-main child's cumulative hours
by age (children are numbered by starting age, not by any ID; ages are
rounded to 0.1 month). No per-video rows ever leave this script.

Requires AIRTABLE_TOKEN in the environment (read-only token for the
BabyView base). Uses only the Python standard library.
"""

import collections
import datetime
import json
import os
import pathlib
import urllib.parse
import urllib.request

BASE = "appQ7P6moc6knzYzN"
VIDEOS = "tblkRXMPT0hTIYZcu"
RELEASES = "tblVeWx2MbrXRa6o1"
CAMERAS = "tbl9nAHSwcreUvnrs"
OUT = pathlib.Path(__file__).resolve().parent.parent / "_data/bv_summary.json"


def fetch(table, fields):
    return [r["fields"] for r in fetch_records(table, fields)]


def fetch_records(table, fields):
    token = os.environ["AIRTABLE_TOKEN"]
    records, offset = [], None
    while True:
        query = [("fields[]", f) for f in fields] + [("pageSize", "100")]
        if offset:
            query.append(("offset", offset))
        url = f"https://api.airtable.com/v0/{BASE}/{table}?" + urllib.parse.urlencode(query)
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
        with urllib.request.urlopen(req) as resp:
            data = json.load(resp)
        records += data["records"]
        offset = data.get("offset")
        if not offset:
            return records


def main():
    videos = fetch(VIDEOS, ["dataset", "monday_of_recording_week", "duration_sec", "subject_id", "camera", "date", "age (years)"])
    cameras = {c["id"]: c["fields"] for c in fetch_records(CAMERAS, ["Full Name"])}
    releases = fetch(RELEASES, ["Name", "Status", "Duration (hrs)", "Subject Count", "Processed", "Released", "Notes"])

    child_videos = collections.defaultdict(list)
    camera_hours = collections.defaultdict(float)
    camera_months = collections.defaultdict(list)
    weekly = collections.defaultdict(float)
    hours = collections.defaultdict(float)
    children = collections.defaultdict(set)
    for v in videos:
        dataset, week = v.get("dataset"), v.get("monday_of_recording_week")
        h = v.get("duration_sec", 0) / 3600
        if not dataset or h == 0:
            continue
        hours[dataset] += h
        children[dataset].update(v.get("subject_id", []))
        if week:
            weekly[(week, dataset)] += h
        age = v.get("age (years)")
        if dataset == "BV-main" and isinstance(age, (int, float)):
            for subject in v.get("subject_id", []):
                child_videos[subject].append((age * 12, h))
        for c in v.get("camera", []):
            name = cameras.get(c, {}).get("Full Name", "Unknown")
            camera_hours[name] += h
            if v.get("date"):
                camera_months[name].append(v["date"][:7])

    # cumulative hours by age, one series per child, ordered by starting age
    child_series = []
    for vids in sorted(child_videos.values(), key=lambda vids: min(a for a, _ in vids)):
        total, points = 0.0, {}
        for age, h in sorted(vids):
            total += h
            points[round(age, 1)] = round(total, 1)
        child_series.append([[a, t] for a, t in points.items()])

    summary = {
        "updated": datetime.date.today().isoformat(),
        "total_hours": round(sum(hours.values()), 1),
        "total_children": len(set().union(*children.values())),
        "datasets": [
            {"dataset": d, "hours": round(hours[d], 1), "children": len(children[d])}
            for d in sorted(hours, key=hours.get, reverse=True)
        ],
        "releases": sorted(
            [
                {
                    "release": r.get("Name"),
                    "status": r.get("Status"),
                    "hours": round(r.get("Duration (hrs)", 0), 1),
                    "children": r.get("Subject Count"),
                    "processed": r.get("Processed"),
                    "released": r.get("Released"),
                    "notes": r.get("Notes"),
                }
                for r in releases
            ],
            key=lambda r: r["release"],
            reverse=True,
        ),
        "cameras": [
            {
                "camera": c,
                "hours": round(camera_hours[c], 1),
                "first": min(camera_months[c], default=None),
                "last": max(camera_months[c], default=None),
            }
            for c in sorted(camera_hours, key=lambda c: min(camera_months[c], default=""))
        ],
        "children": child_series,
        "weekly": [
            {"week": w, "dataset": d, "hours": round(h, 2)}
            for (w, d), h in sorted(weekly.items())
        ],
    }
    OUT.write_text(json.dumps(summary, indent=1) + "\n")
    print(f"Wrote {OUT}: {summary['total_hours']} h, {summary['total_children']} children, "
          f"{len(summary['releases'])} releases, {len(summary['weekly'])} weekly rows")


if __name__ == "__main__":
    main()
