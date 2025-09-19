---
layout: page
title: Dataset
permalink: /dataset/
description: Information about the current BabyView dataset
nav: true
nav_order: 2
display_categories: [work, fun]
horizontal: false
---

# Overview

The BabyView project is intended to create openly available data for researchers to use to both characterize early learning environments as well as to build computational models to try to better understand cognition. Data collection is still currently ongoing, and our goal is to collect one child’s-years worth of data (4000 hours); our current release (2025.1) totals 868 hours. We anticipate that active data collection will be ongoing through 2026.

<div style="text-align: center;">
<video width="320" controls>
  <source src="{{ '/assets/video/owl_puzzle.mp4' | relative_url }}" type="video/mp4">
  Your browser does not support the video tag.
</video>
</div>
---

# Consent and privacy

Egocentric video data from children in their home and school environments contain more sensitive information than videos in egocentric videos by adults. Participating families provide full consent for the data that are shared at the time of recording and also have a 6 month period after recording when they can retract any portion of their recording. To ensure BabyView data are accessible to researchers while protecting the privacy of participants, we currently distribute the data through [Databrary](https://nyu.databrary.org/), a US National Institutes of Health-funded site designed specifically for the distribution of developmental video data. Access to data on Databrary requires investigators be authorized via an institutional agreement that bars reidentification of participants and redistribution of data. 

---

# Data Releases

Currently, we are currently waiting on Databrary to develop their API to enable automatic upload of the videos, as manual upload is laborious for a dataset of this size, even for only our current release. We will update this page as soon as we are able to provide a concrete timeline. We have, however, released [our Babyview Preschool dataset on Databrary](https://databrary.org/volume/1856). 

## Release Timelines 

<iframe class="airtable-embed" src="https://airtable.com/embed/appQ7P6moc6knzYzN/shro8zErAbkGWi84R" frameborder="0" onmousewheel="" width="100%" height="300" style="background: transparent; border: 1px solid #ccc;"></iframe>

---

# Metadata 

## Participant metadata 
We collect both demographic data from each participating family as well as vocabulary checklist surveys every 3 months for English-speaking families.  These data will be released with the upcoming video dataset via Databrary.

## Accelerometer/Gyroscope data
The BabyView camera also records accelerometer and gyroscope data, which can be used to estimate children’s head motion while they are wearing the camera. These data will be openly shared via OSF since Databrary has file type restrictions, but will be linked to the individual video files via hashed IDs.

## Airtable database
We use Airtable for managing video and participant information, and are developing an r package that can be used to download and link metadata for each video. Please check back here for updates on usage and installation.


