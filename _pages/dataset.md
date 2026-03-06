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

The BabyView project is intended to create openly available data for researchers to use to both characterize early learning environments as well as to build computational models to try to better understand cognition. Data collection is still currently ongoing, and our goal is to collect one child’s-years worth of data (4000 hours). Our first release (2025.1) totals 894 hours and our second release (2025.2) totals 1428 hours. We anticipate that active data collection will be ongoing through the 2026 – 2027 academic year.

<div style="text-align: center;">
<video width="320" controls>
  <source src="{{ '/assets/video/owl_puzzle.mp4' | relative_url }}" type="video/mp4">
  Your browser does not support the video tag.
</video>
</div>
---

# Consent and Privacy

Egocentric video data from children in their home and school environments contain more sensitive information than videos in egocentric videos by adults. Participating families provide full consent for the data that are shared at the time of recording and also have a six month period after recording when they can retract any portion of their recording. To ensure BabyView data are accessible to researchers while protecting the privacy of participants, we currently distribute the data through [Databrary](https://nyu.databrary.org/), a US National Institutes of Health-funded site designed specifically for the distribution of developmental video data. Access to data on Databrary requires investigators be authorized via an institutional agreement that bars reidentification of participants and redistribution of data. 

---

# Data Releases

[The main BabyView dataset](https://www.databrary.org/volume/1882) is currently available on Databrary\. We have also released [our BabyView Preschool dataset](https://databrary.org/volume/1856). Please refer to the table below for information about releases and data quantity.

<iframe class="airtable-embed" src="https://airtable.com/embed/appQ7P6moc6knzYzN/shrfUtt2gWNMcQN5V" frameborder="0" scrolling="no" width="100%" height="700" style="background: transparent; border: 0px solid #ccc;"></iframe><br>

---

# Metadata 

## Participant metadata 
We collect both demographic data from each participating family as well as vocabulary checklist surveys (MacArthur-Bates Communicative Development Inventories (CDIs)) every 3 months for English-speaking families. The demographic data includes information about age of the child at the time of recording, the languages spoken at home, and a reported percent of English that the child hears. As of the 2025.2 release, CDI administration data includes 45 English-WG administrations, 51 English-WS administrations, 3 Spanish-WG administrations, and 3 Spanish-WS administrations, stored in CSV files. These data have been released with the video dataset via Databrary. 

## Transcripts
We transcribe and diarize all videos in the dataset and include these annotations on Databrary as well in CSV files. Each row of each file contains the video ID, a token, the utterance that the token appears in, the start and end time for the token, the transcription model's confidence in the token, and the speaker identity of the token (KCHI (target child), OCHI (other child), FEM (female adult), MAL (male adult), Unknown). Videos were transcribed using the WhisperX large-v3 model. Speaker types were generated using VTC 2.0. Given that transcripts were automatically generated, they do not follow conventions detailed by CHILDES or the CHAT transcription format.

## Accelerometer/gyroscope data
The BabyView camera also records accelerometer and gyroscope data, which can be used to estimate children’s head motion while they are wearing the camera. Please check back here for updates on availability of these data.
