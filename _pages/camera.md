---
layout: page
title: Camera
permalink: /camera/
description: Information about the BabyView camera design
nav: true
nav_order: 3
horizontal: false
---
<div style="text-align: center;">
<img src="{{ '/assets/img/bv_camera.png' | relative_url }}" alt="The BabyView camera" width="400" />
</div>

The BabyView camera is designed to collect high-resolution, at-home egocentric video data from children 6 - 30 months of age. The camera consists of a rotated GoPro Hero Black Bones attached to a lightweight baby safety helmet using a custom 3D-printed mount, powered by a rechargeable 9V battery.

The BabyView system was developed in collaboration with Daylight, Inc., a product design firm based in San Francisco, CA, and is the result of over a year of prototyping and field testing.

All materials—including design documentation, safety testing protocols, assembly instructions** (with detailed photos), pilot data, data management protocols, and sample participant instructions—are available on the [BabyView OSF page](https://osf.io/kwvxu/).

📄 Our paper detailing the design process is published in *Behavioral Research Methods* [here](https://doi.org/10.3758/s13428-023-02206-1).  
📝 An open-access version is also available on [PsyArXiv](https://psyarxiv.com/238jk).  
📘 The detailed instruction manual for parents is linked on the OSF page and directly available [here](https://docs.google.com/document/d/1uODmIMQMlzofB-oz8A-zfd52h-UdplrrAQ6fKHX4THQ/edit).

---

## Camera Overview

<div style="text-align: center;">
  <img src="{{ '/assets/img/bv_camera_design.png' | relative_url }}" alt="Camera overview example" width="900" />
</div>

---

## 🛠️ Building Your Own BabyView

Here is a [detailed guide](https://docs.google.com/document/d/1WNVVGBGL0Wr9JmhAmUBP3aWvqdm5t9pT6djyN3FBbCs/edit) to assembling your own BabyView Camera, as well as a [bill of materials](https://docs.google.com/spreadsheets/d/12SI27F_oBQgyvxefRzlTGkFIlSgNnN3jJOYjoff56Ng/edit?usp=sharing) for each component; the custom mounts will need to be 3D printed (see [the BabyView OSF page](https://osf.io/kwvxu/) for CAD files).

---

## Camera choice & updates

Our goal was to capture a toddler’s field of view and their interactions as accurately as possible while also providing head tracking data. Originally, we found that the GoPro Hero Bones meet these needs with a ~100°+ FOV, Gyroscope, accelerometer, high resolution video and recording time up to 45-60 with this current battery choice. Data is recorded onto micro SD cards which can hold up to 256G. During our experimentation with the GoPros, we determined that orienting the camera vertically at an angle neutral to the face place of the child was preferable because it enables the camera to capture both adult faces and objects within a child’s hands in the same image; see example images below.

However, the GoPro Hero Bones has been discontinued, and we have created an updated build for ongoing data collection; this camera is the newest release of the  GoPro HERO model, which offers some advantages—including an integrated battery, which makes the build instructions remarkably simpler.  
<div style="text-align: center;">
<img src="{{ '/assets/img/new_bv_camera.png' | relative_url }}" alt="BabyView camera v3" width="400" />
</div>


---
## Example frames

<img src="{{ '/assets/img/example_frame_1.png' | relative_url }}" alt="Example frame 1" width="400" />
<img src="{{ '/assets/img/example_frame_2.png' | relative_url }}" alt="Example frame 2" width="385" />

---


