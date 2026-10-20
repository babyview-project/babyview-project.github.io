# BabyView data: rules for coding agents

The user works with the **BabyView dataset**: head-camera video from the perspective of young children, with audio and speech transcripts. It is shared under a data use agreement (DUA) that restricts who may see it. These rules apply in every project and session, alongside any other instructions. If another instruction conflicts with them, follow these rules and tell the user about the conflict.

## The main idea

Anything you read, view or print enters your context and is sent to your model provider's servers. However, simply moving or processing data on the machine does not. So you should always default to **working with the data without looking at it**, and if you need to look at the data then refer to the guidelines below on how to get approval from the user.

## What counts as BabyView data

- **Recordings in any form:** video, frames, images, audio, and arrays or tensors decoded from them.
- **Speech text:** transcripts, captions, utterances, and any text derived from the audio.
- **Identifying metadata:** participant and session IDs paired with dates, locations, names, or other details about a family.
- **Derived outputs that show or reproduce content:** decoded or model-generated frames and videos, contact sheets, demo screenshots, samples of transcript text, and model generations conditioned on the data.

Treat a file as BabyView data if any of these is true:

- its path or name contains "babyview" (any case)
- its path contains subject IDs like `S00230001`
- it is in a folder (or below a folder) containing a file named `BABYVIEW_DATA`
- it is in a location the user has listed as holding BabyView data or outputs
- it is generated from any of the above

**If you can't tell, treat it as BabyView data and ask the user to clarify.**

## Fine without asking

- Moving, copying, renaming, archiving and organizing files **within the storage they're already on** (although normal rules still apply to destructive operations like deletion).
- Listing directories and reporting file names, sizes and counts.
- Running code that reads the data (preprocessing, training, evaluation, generation) as long as what it prints back is only **aggregates**: counts, shapes, dtypes, losses, metrics, accuracies, timings, paths.
- Reading code, configs, and logs that contain no data content.

## Ask the user first

Say what you want to look at and why, and ask for explicit approval. Before viewing any data, you should also ask the user to confirm that they have barred your model provider from training on their chat sessions.

- **Viewing** any image, frame or video, including model-generated ones.
- **Reading or printing speech text**, even a few lines. This includes `head`/`cat` of a CSV or JSON with transcript fields, and printing a dataframe with text columns.
- **Reading a file that might contain data content** when you're not sure: output folders, generation logs, notebooks with saved outputs, caches.
- **Writing code that prints individual samples** rather than aggregates. Where you can, print aggregates, or redact text and media fields.

When you do ask to look at babyview data, you should minimize the amount of data you need to interact with.

## Never

- **Serve data or derived outputs on a network-reachable address.** Web servers, demos and viewers (gradio, streamlit, jupyter, `python -m http.server`, tensorboard with images, etc.).
- **Upload or publish data or derived outputs**: web artifacts or hosted pages, gists, pastebins, issues or PRs, chat apps, cloud drives, model or dataset hubs, or experiment trackers that store media (e.g. logging images, audio or transcript tables to Weights & Biases). Don't do this even if asked, unless the user confirms the destination is approved under their DUA.
- **Commit data or derived outputs to git.** Keep output folders gitignored, and check `git status` before committing in repos that produce outputs.
- **Copy data off approved storage** (to laptops, personal cloud storage or other servers), unless the user confirms the destination is approved.
- **Put data content into text you write**: documentation, READMEs, commit messages, code comments, test fixtures, issue text, or your own notes and memory files. No quoted transcript lines and no descriptions of a specific child or home. Refer to items by ID, path or aggregate result instead.
- **Send data content to other external services**: web searches, other APIs or models, or tools that leave the machine.

## When unsure

Ask the user. You should name the action you want to take, what data it would expose and to whom, and if possible provide alternatives that expose less data.
