---
layout: about
title: About
permalink: /
#subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: right
  image: about_bv.png
  image_circular: false # crops the image to make it circular

selected_papers: false # includes a list of papers marked as "selected={true}"
---

The BabyView Project is a research initiative dedicated to capturing children’s everyday experiences via high-resolution videos taken from the infant perspective, and to using the resulting video data to better understand cognitive development. Our dataset is currently the largest open video dataset of children’s everyday experience to date, both in terms of the number of hours and the diversity of the participating families; data collection is currently ongoing.

<div class="row mt-4 mb-2">
  <div class="col-sm-6 mb-3">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">For researchers</h5>
        <p>What's in the <a href="{{ '/dataset/' | relative_url }}">dataset</a> and how to access it, our <a href="{{ '/data-use/' | relative_url }}">data use and ethics guidelines</a>, the <a href="{{ '/camera/' | relative_url }}">camera</a> design, and our <a href="{{ '/publications/' | relative_url }}">publications</a>.</p>
      </div>
    </div>
  </div>
  <div class="col-sm-6 mb-3">
    <div class="card h-100">
      <div class="card-body">
        <h5 class="card-title">For families</h5>
        <p>How to <a href="{{ '/families/' | relative_url }}">take part in BabyView</a>, how we keep your videos secure, and how AI is used in our research.</p>
      </div>
    </div>
  </div>
</div>

## Data Release Snapshot

{% assign bv = site.data.bv_summary %}
So far we have collected **{{ bv.total_hours | number_with_delimiter }} hours** of video from **{{ bv.total_children }} children**. See the [dataset page]({{ '/dataset/' | relative_url }}) for details and access.

{% include bv_releases_table.liquid compact=true %}

## Funding

The BabyView project acknowledges generous support from: 
- The Stanford Human-Centered AI Initiative (HAI) Hoffman-Yee grant program
- Schmidt Futures
- Meta, Inc. 
- The Stanford Center for the Study of Language and Information John Crosby Olney Fund
- Amazon, Inc. 
- Compute support from the Microsoft Accelerating Foundation Models Research (AFMR) program
- NIH K99HD108386 to BLL
