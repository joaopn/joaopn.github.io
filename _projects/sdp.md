---
title: "Social Data Pipeline (SDP)"
collection: projects
permalink: /projects/sdp/
order: 2
excerpt: "A CLI framework for end-to-end processing and TB-scale ingestion of social media data into OLAP-tuned PostgreSQL/MongoDB, with high-throughput multi-GPU enrichment and MCP servers for agentic SQL."
stack:
  - Python
  - PostgreSQL
  - MongoDB
  - ONNX
  - Docker
  - MCP
---

## Overview

An end-to-end data platform for ingesting, enriching, and querying TB-scale social media datasets. Originally built as research infrastructure at the University of Graz, later abstracted into an open-source package.

## Key features

- **CLI framework for end-to-end processing**: parses raw multi-platform exports and ingests them into OLAP-tuned PostgreSQL and MongoDB backends.
- **Multi-GPU enrichment workflows**: high-throughput inference (emotion, toxicity, stance, embeddings) via optimized ONNX models, achieving significant throughput gains over baseline `transformers` deployments.
- **Agentic SQL via MCP**: customized [Model Context Protocol](https://modelcontextprotocol.io/) servers expose the databases to AI developer tools, enabling agents to run complex queries directly against the data.

## Scale

Deployed to process ~100TB of raw multi-platform data into a ~20TB optimized multi-database ecosystem, supporting a 10-person research team running queries that would be intractable with standard Pandas-based tooling.

## Stack

Python, PostgreSQL, MongoDB, ONNX, Docker, MCP.

## Links

- [GitHub repository](https://github.com/joaopn/social-data-pipeline)
