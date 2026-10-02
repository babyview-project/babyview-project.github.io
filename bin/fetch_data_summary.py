#!/usr/bin/env python3
"""Fetch aggregate BabyView dataset statistics from Airtable for the website.

Writes _data/bv_summary.json. Only aggregates are written: hours per
dataset per recording week, per-release totals, and overall totals. No
per-video or per-child rows ever leave this script.

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
OUT = pathlib.Path(__file__).resolve().parent.parent / "_data/bv_summary.json"


def fetch(table, fields):
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
        records += [r["fields"] for r in data["records"]]
        offset = data.get("offset")
        if not offset:
            return records


def main():
    videos = fetch(VIDEOS, ["dataset", "monday_of_recording_week", "duration_sec", "subject_id"])
    releases = fetch(RELEASES, ["Name", "Status", "Duration (hrs)", "Subject Count", "Processed", "Released", "Notes"])

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
