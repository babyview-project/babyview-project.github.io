---
layout: page
title: Camera
permalink: /camera/
description: The BabyView camera design and its versions
nav: true
nav_order: 4
horizontal: false
---

# The BabyView camera

There isn't just one BabyView camera. BabyView is a general design for recording high-resolution, egocentric video from children 6 – 30 months of age: a small consumer action camera mounted on a soft child safety helmet. We have built several versions of this design as cameras have been discontinued and as we have learned from families. Recordings in the dataset come from more than one version.

All materials – including design documentation, safety testing protocols, assembly instructions (with detailed photos), pilot data, data management protocols, and sample participant instructions – are available on the [BabyView OSF page](https://osf.io/kwvxu/). The design process is described in our paper in _Behavior Research Methods_ ([Long et al., 2023](https://doi.org/10.3758/s13428-023-02206-1); open-access version on [PsyArXiv](https://psyarxiv.com/238jk)).

---

# The general design

<div class="row">
  <div class="col-md-6">
    <img src="{{ '/assets/img/bv_camera.png' | relative_url }}" alt="Illustration of a child wearing the BabyView camera, and the camera's field of view" class="img-fluid" />
  </div>
  <div class="col-md-6">
    <ul>
      <li><strong>A GoPro camera</strong>, for high resolution, good battery life, a built-in inertial motion unit (accelerometer and gyroscope), and wide availability.</li>
      <li><strong>A soft child safety helmet</strong> (SafeheadBABY), which is comfortable, easy to modify, fits a wide range of ages, and bothers children less than headbands.</li>
      <li><strong>A custom 3D-printed mount</strong> attaching the camera to the helmet.</li>
    </ul>
  </div>
</div>

Our goal is to capture a toddler's field of view and their interactions as accurately as possible. We orient the camera vertically, at an angle neutral to the face plane of the child, so that it captures both adult faces and objects in the child's hands in the same image. The camera was developed in collaboration with Daylight, Inc., a product design firm in San Francisco, through over a year of prototyping and field testing.

<div class="row justify-content-center">
  <div class="col-5 col-md-3"><img src="{{ '/assets/img/example_frame_1.png' | relative_url }}" alt="Example frame from a BabyView recording" class="img-fluid" /></div>
  <div class="col-5 col-md-3"><img src="{{ '/assets/img/example_frame_2.png' | relative_url }}" alt="Example frame from a BabyView recording" class="img-fluid" /></div>
</div>
<p class="bv-caption text-center">Example frames from BabyView recordings.</p>

---

# Versions

## BabyView 1.0

<img src="{{ '/assets/img/bv_camera_design.png' | relative_url }}" alt="BabyView 1.0 components: assembled camera, GoPro HERO10 Black Bones, SafeheadBABY helmet, and 3D-printed mounts" class="img-fluid" />

The original design, described in Long et al. (2023): a rotated GoPro HERO10 Black Bones attached to the helmet with a custom 3D-printed mount, powered by a rechargeable 9V battery.

## BabyView 2.0

<div class="row">
  <div class="col-md-6">
    <img src="{{ '/assets/img/about_bv.png' | relative_url }}" alt="Three BabyView 2.0 cameras on helmets" class="img-fluid" />
  </div>
  <div class="col-md-6">
    <p>Also built on the GoPro HERO10 Black Bones.</p>
    <p><strong>[To fill in: what changed from 1.0.]</strong></p>
    <p>The Bones camera has since been discontinued, which led us to version 3.0.</p>
  </div>
</div>

## BabyView 3.0

<div class="row">
  <div class="col-md-4">
    <img src="{{ '/assets/img/new_bv_camera.png' | relative_url }}" alt="BabyView 3.0 camera on a helmet" class="img-fluid" />
  </div>
  <div class="col-md-8">
    <p>Our current build uses the GoPro HERO (2024).</p>
    <ul>
      <li>No external battery, so the build is considerably simpler.</li>
      <li>The internal battery makes the camera easier for parents to use and allows longer recordings.</li>
      <li>It can still overheat in hot weather.</li>
    </ul>
  </div>
</div>

## BabyView 3.1 (in preparation)

A new mount that gives the camera a better view angle.

---

# Which cameras recorded the data

Each recording in the BabyView database is tagged with the camera model used. Versions overlap in time.

<div class="table-responsive">
  <table class="table table-sm">
    <thead>
      <tr><th>Camera model</th><th>BabyView version</th><th class="text-right">Hours</th><th>Recording period</th></tr>
    </thead>
    <tbody>
      {% for c in site.data.bv_summary.cameras %}
        <tr>
          <td>{{ c.camera }}</td>
          <td>
            {% case c.camera %}
              {% when 'GoPro Hero Black Bones 10' %}1.0, 2.0
              {% when 'GoPro HERO Mini' %}3.0
              {% when 'Headlight Camera 1080P' %}&ndash; (Ego Single-Child dataset)
              {% else %}&ndash;
            {% endcase %}
          </td>
          <td class="text-right">{{ c.hours | number_with_delimiter }}</td>
          <td>{{ c.first | append: '-01' | date: '%b %Y' }} &ndash; {{ c.last | append: '-01' | date: '%b %Y' }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

---

# Building your own BabyView

Here is a [detailed guide](https://docs.google.com/document/d/1WNVVGBGL0Wr9JmhAmUBP3aWvqdm5t9pT6djyN3FBbCs/edit) to assembling your own BabyView camera, as well as a [bill of materials](https://docs.google.com/spreadsheets/d/12SI27F_oBQgyvxefRzlTGkFIlSgNnN3jJOYjoff56Ng/edit?usp=sharing) for each component; the custom mounts will need to be 3D printed (see [the BabyView OSF page](https://osf.io/kwvxu/) for CAD files). The [instruction manual for parents](https://docs.google.com/document/d/1uODmIMQMlzofB-oz8A-zfd52h-UdplrrAQ6fKHX4THQ/edit) is also available.
