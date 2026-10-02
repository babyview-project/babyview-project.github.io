---
layout: page
title: Dataset
permalink: /dataset/
description: What's in the BabyView dataset and how to access it
nav: true
nav_order: 1
horizontal: false
---

{% assign bv = site.data.bv_summary %}

# Overview

The BabyView project is intended to create openly available data for researchers to use to both characterize early learning environments as well as to build computational models to try to better understand cognition. Our goal is to collect one child's-years worth of data (4,000 hours). So far we have collected **{{ bv.total_hours | number_with_delimiter }} hours** of video from **{{ bv.total_children }} children**. We anticipate that active data collection will be ongoing through the 2026 – 2027 academic year.

<div style="text-align: center;">
<video width="320" controls>
  <source src="{{ '/assets/video/owl_puzzle.mp4' | relative_url }}" type="video/mp4">
  Your browser does not support the video tag.
</video>
<p class="bv-caption">This clip is a pilot recording from one of our researchers, released as an example to illustrate BabyView. Researchers are welcome to reuse it.</p>
</div>

---

# Data collected so far

{% include bv_hours_chart.liquid %}

<p class="bv-caption">Hours of video by recording week. <strong>BV-main</strong> is the main home-recording dataset; <strong>Preschool</strong> contains recordings made in a preschool classroom; <strong>Ego Single-Child</strong> contains recordings of a single child.</p>

---

# Data releases

[The main BabyView dataset](https://www.databrary.org/volume/1882) is available on Databrary, as is [the BabyView Preschool dataset](https://databrary.org/volume/1856). [BabyView IMU data](https://stanford.redivis.com/datasets/e7we-asyc0tmc7) (accelerometer and gyroscope) are available on Redivis.

{% include bv_releases_table.liquid %}

---

# Accessing the data

Because BabyView videos show children and families in their homes, the videos are shared only with authorized researchers through [Databrary](https://nyu.databrary.org/), a restricted-access video library funded by the US National Institutes of Health.

1. **Get authorized on Databrary.** Your institution signs the [Databrary Access Agreement](https://databrary.org/about/agreement/agreement), which makes you an Authorized Investigator. Students and staff can get access as Affiliates of an Authorized Investigator.
2. **Read our [data use and ethics guidelines]({{ '/data-use/' | relative_url }})** before working with the data. They explain how the agreement applies to BabyView, including when you use AI models.
3. **Access the BabyView volumes** linked above.

---

# What's included

## Participant metadata

We collect both demographic data from each participating family as well as vocabulary checklist surveys (MacArthur-Bates Communicative Development Inventories (CDIs)) every 3 months for English-speaking families. The demographic data includes information about age of the child at the time of recording, the languages spoken at home, and a reported percent of English that the child hears. As of the 2025.2 release, CDI administration data includes 45 English-WG administrations, 51 English-WS administrations, 3 Spanish-WG administrations, and 3 Spanish-WS administrations, stored in CSV files. These data have been released with the video dataset via Databrary.

## Transcripts

We transcribe and diarize all videos in the dataset and include these annotations on Databrary as well in CSV files. Each row of each file contains the video ID, a token, the utterance that the token appears in, the start and end time for the token, the transcription model's confidence in the token, and the speaker identity of the token (KCHI (target child), OCHI (other child), FEM (female adult), MAL (male adult), Unknown). Videos were transcribed using the WhisperX large-v3 model. Speaker types were generated using VTC 2.0. Given that transcripts were automatically generated, they do not follow conventions detailed by CHILDES or the CHAT transcription format.

## Accelerometer/gyroscope data

The BabyView camera also records accelerometer and gyroscope data, which can be used to estimate children's head motion while they are wearing the camera. These data are available as the [BabyView IMU data release on Redivis](https://stanford.redivis.com/datasets/e7we-asyc0tmc7). Each file contains the GoPro telemetry from one BabyView recording, extracted from the video's GPMF track: a merged ~200 Hz IMU CSV file with accelerometer, gyroscope, and gravity measurements, as well as additional camera telemetry streams such as orientation quaternions (CORI/IORI).

---

# How to cite

If you use BabyView data, please cite the dataset paper:

> Long, B. L., Sparks, R. Z., Xiang, V., Stojanov, S., Yin, Z., Keene, G., Tan, A. W. M., Feng, S. Y., Nag, A., Zhuang, C., Marchman, V. A., Yamins, D. L. K., & Frank, M. C. (2025). The BabyView dataset: High-resolution egocentric videos of infants' and young children's everyday experiences. _Proceedings of the Cognitive Computational Neuroscience Conference._ [[pdf]](https://openreview.net/pdf?id=bbv4CA2noZ)

The Databrary Access Agreement also asks you to cite the Databrary volumes you use. Each volume page gives its citation.
