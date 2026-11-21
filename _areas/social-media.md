---
key: sm
label: "Social media"
tag: "social media"
order: 1
---

## Dynamics *of* platforms

I've analyzed how social media platforms work, and what can be changed in terms of algorithms and design decisions to improve them beyond engagement metrics. I approach this through large-scale data analysis and modelling.

Telegram is an important platform, given its size and use for less visible, more private content-sharing. We parsed and made available a large-scale multimodal (text, audio & video transcriptions) dataset of German-language telegram channels. The underlying 25TB multimodal ETL pipeline (Python, Snakemake, PyTorch, Whisper) achieved a ~250× real-time transcription factor per GPU on `whisper/large-v3-turbo` through finetuned batching and VAD.

## Dynamics *within* platforms

I've analyzed how certain important societal issues interact with, and are affected by, social media. These include
- how conspiracy theories evolve on German Telegram
- how the discourse around climate change has evolved on Reddit
