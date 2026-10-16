---
layout: page
title: Camera
permalink: /camera/
description: The BabyView camera design and its versions
nav: true
nav_order: 5
horizontal: false
versions:
  - version: "1.0"
    camera: GoPro HERO8 Black
    attachment: Full 3D-printed enclosure
    status: Retired
  - version: "2.0"
    camera: GoPro HERO10 Black Bones
    airtable_camera: GoPro Hero Black Bones 10
    attachment: 3D-printed mount
    power: External rechargeable 9V battery
    status: In use (camera discontinued)
  - version: "3.0"
    camera: GoPro HERO (2024)
    airtable_camera: GoPro HERO Mini
    attachment: 3D-printed mount
    power: Internal battery
    status: In use
  - version: "3.1"
    camera: GoPro LIT HERO
    airtable_camera: GoPro LIT HERO
    attachment: 3D-printed mount
    power: Internal battery
    status: In use
  - version: "3.2"
    attachment: New mount with a better view angle
    status: In preparation
---

# The BabyView camera

There isn't just one BabyView camera. BabyView is a general design for recording high-resolution, egocentric video from children 6 – 30 months of age: a small consumer action camera mounted on a soft child safety helmet. We have built several versions of this design as cameras have been discontinued and as we have learned from families. Recordings in the dataset come from more than one version.

All materials – including design documentation, safety testing protocols, assembly instructions (with detailed photos), pilot data, data management protocols, and sample participant instructions – are available on the [BabyView OSF page](https://osf.io/kwvxu/). The design process is described in our paper in _Behavior Research Methods_ ([Long et al., 2023](https://doi.org/10.3758/s13428-023-02206-1); open-access version on [PsyArXiv](https://psyarxiv.com/238jk)).

---

# The general design

<div class="row">
  <div class="col-md-6">
    <img src="{{ '/assets/img/bv_camera.webp' | relative_url }}" alt="Illustration of a child wearing the BabyView camera, and the camera's field of view" class="img-fluid" />
  </div>
  <div class="col-md-6">
    <ul>
      <li><strong>A GoPro camera</strong>, for high resolution, good battery life, a built-in inertial motion unit (accelerometer and gyroscope), and wide availability.</li>
      <li><strong>A soft child safety helmet</strong> (SafeheadBABY), which is comfortable, easy to modify, fits a wide range of ages, and bothers children less than headbands.</li>
      <li><strong>A custom 3D-printed mount</strong> attaching the camera to the helmet (in version 1.0, a full 3D-printed enclosure).</li>
    </ul>
  </div>
</div>

<img src="{{ '/assets/img/bv_camera_design.webp' | relative_url }}" alt="BabyView 2.0 components: assembled camera, GoPro HERO10 Black Bones, SafeheadBABY helmet, and 3D-printed mounts" class="img-fluid" />
<p class="bv-caption">The parts of a BabyView camera, shown for version 2.0.</p>

Our goal is to capture a toddler's field of view and their interactions as accurately as possible. We orient the camera vertically, at an angle neutral to the face plane of the child, so that it captures both adult faces and objects in the child's hands in the same image. The camera was developed in collaboration with Daylight, Inc., a product design firm in San Francisco, through over a year of prototyping and field testing.

<div class="row justify-content-center">
  <div class="col-5 col-md-3"><img src="{{ '/assets/img/example_frame_1.webp' | relative_url }}" alt="Example frame from a BabyView recording" class="img-fluid" /></div>
  <div class="col-5 col-md-3"><img src="{{ '/assets/img/example_frame_2.webp' | relative_url }}" alt="Example frame from a BabyView recording" class="img-fluid" /></div>
</div>
<p class="bv-caption text-center">Example frames from BabyView pilot recordings, posted with permission.</p>

---

# Versions

Versions overlap in time: several builds are in use at once, so the dataset includes recordings from more than one version.

<div class="table-responsive">
  <table class="table table-sm">
    <thead>
      <tr><th>Version</th><th>Camera</th><th>Attachment</th><th>Power</th><th>Status</th><th class="text-right">Hours in dataset</th><th>Recording period</th></tr>
    </thead>
    <tbody>
      {% for v in page.versions %}
        {% assign c = site.data.bv_summary.cameras | where: "camera", v.airtable_camera | first %}
        <tr>
          <td><strong>{{ v.version }}</strong></td>
          <td>{{ v.camera | default: '&ndash;' }}</td>
          <td>{{ v.attachment }}</td>
          <td>{{ v.power | default: '&ndash;' }}</td>
          <td>{{ v.status }}</td>
          <td class="text-right">{% if c %}{{ c.hours | number_with_delimiter }}{% else %}&ndash;{% endif %}</td>
          <td>{% if c %}{{ c.first | append: '-01' | date: '%b %Y' }} &ndash; {{ c.last | append: '-01' | date: '%b %Y' }}{% else %}&ndash;{% endif %}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
{% assign ego = site.data.bv_summary.cameras | where: "camera", "Headlight Camera 1080P" | first %}
<p class="bv-caption">Hours and recording periods come from the camera model recorded for each video. The Ego Single-Child dataset was recorded with a different camera (Headlight Camera 1080P; {{ ego.hours | number_with_delimiter }} hours).</p>

## BabyView 1.0

<div class="row mb-4">
  <div class="col-md-5">
    <img src="{{ '/assets/img/bv1_blurred.webp' | relative_url }}" alt="A child wearing the BabyView 1.0 camera, a GoPro in a red 3D-printed enclosure on a helmet" class="img-fluid" />
  </div>
  <div class="col-md-7">
    <p>Our first build: a GoPro HERO8 Black in a fully 3D-printed enclosure on the helmet. This design has been retired.</p>
  </div>
</div>

## BabyView 2.0

<div class="row mb-4">
  <div class="col-md-5">
    <img src="{{ '/assets/img/about_bv.webp' | relative_url }}" alt="Three BabyView 2.0 cameras on helmets" class="img-fluid" />
  </div>
  <div class="col-md-7">
    <p>A rotated GoPro HERO10 Black Bones attached to the helmet with a custom 3D-printed mount, powered by a rechargeable 9V battery.</p>
    <p>The Bones camera has since been discontinued, which led us to version 3.0.</p>
  </div>
</div>

## BabyView 3.0

<!-- TODO: replace with a higher-resolution photo when available -->
<div class="row mb-4">
  <div class="col-md-5">
    <img src="{{ '/assets/img/new_bv_camera.webp' | relative_url }}" alt="BabyView 3.0 camera on a helmet" class="img-fluid" />
  </div>
  <div class="col-md-7">
    <p>Built on the GoPro HERO (2024).</p>
    <ul>
      <li>No external battery, so the build is considerably simpler.</li>
      <li>The internal battery makes the camera easier for parents to use and allows longer recordings.</li>
      <li>It can still overheat in hot weather.</li>
    </ul>
  </div>
</div>

## BabyView 3.1

<div class="row mb-4">
  <div class="col-md-5">
    <div class="d-flex align-items-center justify-content-center text-center bv-caption" style="aspect-ratio: 4 / 3; border: 1px dashed var(--global-divider-color);">Photo to come</div>
  </div>
  <div class="col-md-7">
    <p>The 3.0 build with a different camera, the GoPro LIT HERO.</p>
  </div>
</div>

## BabyView 3.2 (in preparation)

<!-- TODO: add a photo when available -->
<div class="row mb-4">
  <div class="col-md-5">
    <div class="d-flex align-items-center justify-content-center text-center bv-caption" style="aspect-ratio: 4 / 3; border: 1px dashed var(--global-divider-color);">Photo to come</div>
  </div>
  <div class="col-md-7">
    <p>A new mount that gives the camera a better view angle.</p>
  </div>
</div>

---

# Building your own BabyView

Here is a [detailed guide](https://docs.google.com/document/d/1WNVVGBGL0Wr9JmhAmUBP3aWvqdm5t9pT6djyN3FBbCs/edit) to assembling your own BabyView camera, as well as a [bill of materials (version 3.0)](https://docs.google.com/spreadsheets/d/12SI27F_oBQgyvxefRzlTGkFIlSgNnN3jJOYjoff56Ng/edit?usp=sharing) for each component; the custom mounts will need to be 3D printed (see [the BabyView OSF page](https://osf.io/kwvxu/) for CAD files). The [instruction manual for parents (version 3.0)](https://docs.google.com/document/d/1teLEj1LZ7dQ22qEzKZIFF9gXZZqdiJCEuA3xqtuL7R0/edit?tab=t.0#heading=h.nrqgp6jboqxf) is also available.
