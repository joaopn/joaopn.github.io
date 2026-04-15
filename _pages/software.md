---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

This page contains links to software packages and models I've developed or contributed to.

## Packages
- [`joaopn/zotero_llm`](https://github.com/joaopn/zotero_llm): Package for adding fulltext LLM analysis (summarization, QA, etc) to Zotero academic papers through notes.
- [`JanaLasser/civirank`](https://github.com/JanaLasser/civirank/tree/dev): Social media content ranker based on combining multiple NLP-based classifiers. Developed for the *[Prosocial Ranking Challenge](https://www.mediatorsfoundation.org/current-projects/prosocial-ranking-challenge)*.
- [`Priesemann-Group/mrestimator`](https://github.com/Priesemann-Group/mrestimator): Package for estimating subsampled-corrected R parameters from autoregressive timeseries.
- [`joaopn/criticalavalanches`](https://github.com/joaopn/criticalavalanches): Package for simulating running and spatially-sampling near-critical branching networks.

## Models
In order to analyze large-scale social media data, I've converted a number of `BERT`-based models to `onnx-fp16`, which can more than 2X the `transformers` throughput.
- [`joaopn/gpu_benchmark_goemotions`](https://github.com/joaopn/gpu_benchmark_goemotions): Benchmark repo with code and comparison between the various formats (torch, onnx, onnx-fp16)
- Optimized models:
    - [`joaopn/roberta-large-openai-detector-onnx-fp16`](https://huggingface.co/joaopn/roberta-large-openai-detector-onnx-fp16)
    - [`joaopn/roberta-base-go_emotions-onnx-fp16`](https://huggingface.co/joaopn/roberta-base-go_emotions-onnx-fp16)
    - [`joaopn/unbiased-toxic-roberta-onnx-fp16`](https://huggingface.co/joaopn/unbiased-toxic-roberta-onnx-fp16)


*Last updated: {{ site.time | date: '%d/%m/%y' }}*
