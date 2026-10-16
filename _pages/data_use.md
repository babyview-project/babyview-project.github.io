---
layout: page
title: Data Use & Ethics
nav_title: Ethics
permalink: /data-use/
description: How we protect participating families, and what we ask of researchers who use BabyView data
nav: true
nav_order: 3
horizontal: false
---

# Consent and privacy

Egocentric video data from children in their home and school environments contain more sensitive information than egocentric videos recorded by adults. Participating families provide full consent for the data that are shared at the time of recording and also have a six-month period after recording when they can retract any portion of their recording. To ensure BabyView data are accessible to researchers while protecting the privacy of participants, we distribute the data through [Databrary](https://nyu.databrary.org/), a US National Institutes of Health-funded site designed specifically for the distribution of developmental video data.

---

# The Databrary Access Agreement

Access to BabyView requires that your institution sign the [Databrary Access Agreement](https://databrary.org/about/agreement/agreement). Its terms include:

- **Non-commercial use only.** Data may be used exclusively for non-commercial scientific research or education, and may not be sold, traded, or used for other commercial purposes.
- **Access is limited to authorized researchers.** BabyView is shared at Databrary's [Learning Audiences](https://databrary.org/about/agreement/agreement-annex-III) release level: the data are restricted to authorized Databrary users, who may show clips or images in presentations for informational or educational purposes.
- **Data must be secured.** Downloaded data must be protected with the highest safeguards your institution specifies for sensitive research data.
- **No reidentification.** You may not attempt to reidentify or recontact participants.

Please read the full agreement and its [Statement of Rights and Responsibilities](https://databrary.org/about/agreement/agreement-annex-I) before using the data.

---

# BabyView guidelines for researchers

## Using AI models with BabyView data

Databrary's policy is that restricted-access data may not be shared with any outside commercial service that could reuse the data in any way. Databrary has told us that the signed access agreement already precludes this, and that more explicit language is being added to the agreement and the site's terms of use.

- **Use local models, or services that cannot train on your data.** When you analyze BabyView data with AI models (for example, for object detection, captioning, or transcription), either run the models locally or use a commercial service only under terms that bar the provider from training on or otherwise reusing your inputs (for example, Google Cloud's Vertex AI). This applies to model APIs and [coding agents]({{ '/access/' | relative_url }}#using-coding-agents) alike. Never upload BabyView data to consumer chatbots. Check with your IT office and IRB about which services your institution has approved.
- **Keep BabyView data out of frontier model training.** Do not include BabyView data in training datasets for large-scale commercial or "frontier" models, or contribute it to datasets that may be used this way.

## Sharing models trained on BabyView data

Models trained on BabyView data can encode features of the people in the recordings, such as their faces and voices. We therefore ask that models be shared the same way as the data: any model trained or fine-tuned on BabyView data should be available only to researchers who have been granted access to BabyView on Databrary. In practice, host the weights in a gated repository (for example, a gated Hugging Face repository), and grant access only once the requester shows they have BabyView access on Databrary. The model card should explain why access is restricted, link to the [BabyView Databrary volume](https://www.databrary.org/volume/1882), and direct access requests to [babyview-study@stanford.edu](mailto:babyview-study@stanford.edu); see the [ZWM BabyView model](https://huggingface.co/awwkl/zwm-babyview-170m) for an example. If you have been given access to a gated model, please don't share the weights with others. If you aren't sure whether this applies to something you want to release, email us.

## Additional requests from the BabyView team

These go beyond what the Databrary agreement requires. We ask them out of respect for the families who share their everyday lives with us.

- **Presentations.** You may show BabyView examples in scientific presentations, but please **blur faces**, and do not allow presentations containing BabyView examples to be recorded and redistributed.
- **Social media.** Do not post BabyView examples on social media (for example, in threads summarizing your paper).
- **Identifying features.** Models trained on BabyView data may encode features of the people in the recordings, such as voices or faces. Do not attempt to prompt or otherwise get models to reproduce these features.

Note that the [owl puzzle clip]({{ '/dataset/' | relative_url }}) on our dataset page is a pilot recording from one of our researchers that we release as an example. You are welcome to reuse it, including in presentations.

---

# Questions

If you're not sure whether a planned use fits these guidelines, please email us at [babyview-study@stanford.edu](mailto:babyview-study@stanford.edu) before you start.
