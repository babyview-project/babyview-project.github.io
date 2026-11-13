---
layout: page
title: Access
permalink: /access/
description: How researchers can get access to BabyView data
nav: true
nav_order: 2
horizontal: false
---

# Getting access to BabyView

Because BabyView videos show children and families in their homes, the videos are shared only with authorized researchers through [Databrary](https://nyu.databrary.org/), a restricted-access video library funded by the US National Institutes of Health.

- [The main BabyView dataset](https://www.databrary.org/volume/1882) (Databrary)
- [The BabyView Preschool dataset](https://databrary.org/volume/1856) (Databrary)
- [BabyView IMU data](https://stanford.redivis.com/datasets/e7we-asyc0tmc7) (accelerometer and gyroscope; Redivis)

See the [dataset page]({{ '/dataset/' | relative_url }}) for what each release contains.

---

# How to get access

1. **Get authorized on Databrary.** Your institution signs the [Databrary Access Agreement](https://databrary.org/about/agreement/agreement), which makes you an Authorized Investigator. Students and staff can get access as Affiliates of an Authorized Investigator.
2. **Get institutional approval.** Databrary requires approval from your institution (usually your IRB) before you conduct research with shared data. Check with your IT office about secure storage for the downloaded videos.
3. **Read our [data use and ethics guidelines]({{ '/data-use/' | relative_url }})** before working with the data. They explain how the agreement applies to BabyView, including when you use AI models.
4. **Access the BabyView volumes** linked above.

---

# Models trained on BabyView

Researchers with BabyView access can also use models trained on BabyView data. Under our [model-sharing policy]({{ '/data-use/' | relative_url }}#sharing-models-trained-on-babyview-data), these models are gated: request access on each model's Hugging Face page and follow its instructions for showing that you have BabyView access on Databrary.

- [Word-learning vision–language models](https://huggingface.co/collections/mcxfrank/babyview-word-learning-vlms): cross-situational word learners trained on BabyView.
- [DINOv3 vision encoders](https://huggingface.co/collections/mcxfrank/babyview-dino-models) trained on BabyView (ViT-S, ViT-B and ViT-L).
- Zero-shot world models ([Aw et al., 2026](https://arxiv.org/abs/2604.10333)): [ZWM 170M](https://huggingface.co/awwkl/zwm-babyview-170m) and [ZWM 1B](https://huggingface.co/awwkl/zwm-babyview-1b).
- [DINOv3 ViT-L](https://huggingface.co/awwkl/dinov3-vitl-babyview) and [V-JEPA 2 ViT-L](https://huggingface.co/awwkl/vjepa2-vitl-fpc16-256-babyview) trained on BabyView.

---

# Using coding agents

Coding agents (such as Claude Code or Codex) send the files they read to the model provider. Treat an agent like any other AI service under our [guidelines]({{ '/data-use/' | relative_url }}): only let it open BabyView videos, frames, audio, or transcripts if the model runs locally or under terms that bar the provider from training on or otherwise reusing your inputs. Check which terms your agent runs under, since some individual plans allow training on your sessions.

To set up these guardrails, download our <a href="{{ '/assets/files/AGENTS.md' | relative_url }}" download="AGENTS.md">BabyView rules for coding agents (<code>AGENTS.md</code>)</a> and add them to your agent's instructions. The rules apply to every project, so install them globally: for Codex, save the file as `~/.codex/AGENTS.md`; for Claude Code, add its contents to `~/.claude/CLAUDE.md`. You can also mark a folder as holding BabyView data by putting an empty file named `BABYVIEW_DATA` in it.

---

# How to cite

If you use BabyView data, please cite the dataset paper:

> Long, B. L., Sparks, R. Z., Xiang, V., Stojanov, S., Yin, Z., Keene, G., Tan, A. W. M., Feng, S. Y., Nag, A., Zhuang, C., Marchman, V. A., Yamins, D. L. K., & Frank, M. C. (2025). The BabyView dataset: High-resolution egocentric videos of infants' and young children's everyday experiences. _Proceedings of the Cognitive Computational Neuroscience Conference._ [[pdf]](https://openreview.net/pdf?id=bbv4CA2noZ)

The Databrary Access Agreement also asks you to cite the Databrary volumes you use. Each volume page gives its citation.
