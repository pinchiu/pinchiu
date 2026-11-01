<!-- This file is auto-generated from README.template.md by scripts/build_readme.py. Edit README.template.md directly, do not edit README.md. -->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
  <img src="./assets/banner-light.svg" alt="Pin Chiu — Computational Biology · AI Systems · Systems Software" width="100%">
</picture>

<p>
  <a href="https://github.com/pinchiu"><img src="https://img.shields.io/badge/GitHub-pinchiu-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://github.com/pinchiu/cudaq-rag-for-school"><img src="https://img.shields.io/badge/CUDA--Q_RAG-NVIDIA_AI-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="CUDA-Q RAG"></a>
  <a href="https://github.com/pinchiu/EGFR-TKI-Resistance-Pipeline"><img src="https://img.shields.io/badge/EGFR--TKI-Genomics-E11D48?style=for-the-badge&logo=dna&logoColor=white" alt="EGFR Pipeline"></a>
  <a href="https://github.com/pinchiu/qingjian"><img src="https://img.shields.io/badge/Qingjian-Rust_IME-2EA043?style=for-the-badge&logo=rust&logoColor=white" alt="Qingjian"></a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin">
  <img src="https://img.shields.io/badge/C%23_%2F_.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="C# / .NET">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Pixi-663399?style=flat-square&logo=pixi&logoColor=white" alt="Pixi">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
</p>

</div>

## 👋 About

I engineer systems at the convergence of **Intelligent AI Applications**, **Computational Biology & Healthcare Analytics**, and **Low-Latency Systems Tooling**. My work ranges from building end-to-end RAG knowledge engines with vector indexing and local LLMs to containerized cancer genomics pipelines mining high-throughput TCGA datasets. 

On the open-source side, I actively develop and maintain solutions including **[CUDA-Q RAG](https://github.com/pinchiu/cudaq-rag-for-school)** for quantum computing knowledge retrieval, the **[EGFR-TKI Resistance Pipeline](https://github.com/pinchiu/EGFR-TKI-Resistance-Pipeline)** for lung adenocarcinoma mutation analysis, and contribute to **[Qingjian 青简](https://github.com/pinchiu/qingjian)**, a high-performance Rust input method engine designed to teach contextual language vocabulary with sub-millisecond keystroke latency.

The repository statistics, commit metrics, and language distribution card below are automatically recompiled and refreshed weekly via GitHub Actions.

## 🖥 Showcase

<table>
  <tr>
    <td width="50%" align="center">
      <a href="https://github.com/pinchiu/cudaq-rag-for-school"><img src="./assets/showcase-cudaq.svg" alt="CUDA-Q RAG Assistant"></a><br>
      <sub><b>CUDA-Q RAG Assistant</b> · Dual-track ingestion, LaTeX formula parsing &amp; ChromaDB vector store</sub>
    </td>
    <td width="50%" align="center">
      <a href="https://github.com/pinchiu/EGFR-TKI-Resistance-Pipeline"><img src="./assets/showcase-egfr.svg" alt="EGFR-TKI Resistance Pipeline"></a><br>
      <sub><b>EGFR-TKI Resistance Pipeline</b> · TCGA lung adenocarcinoma mutation co-occurrence matrix</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <a href="https://github.com/pinchiu/qingjian"><img src="./assets/showcase-qingjian.svg" alt="Qingjian Rust IME"></a><br>
      <sub><b>Qingjian 青简</b> · High-performance Rust pinyin IME with contextual translation per keystroke</sub>
    </td>
  </tr>
</table>

## 🏗 Engineering Architecture

Multi-tier workflow illustrating how unstructured documents, multi-omics clinical cohorts, and local systems integrate seamlessly.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/architecture-dark.svg">
  <img src="./assets/architecture-light.svg" alt="Technical architecture across RAG, Bioinformatics, and Systems" width="100%">
</picture>

## 🚀 Selected Work

| Project | Stack | Status | Scale | What it is |
|---|---|:---:|---|---|
| **CUDA-Q RAG Assistant** <br> [repo](https://github.com/pinchiu/cudaq-rag-for-school) | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![ChromaDB](https://img.shields.io/badge/-ChromaDB-black) ![Ollama](https://img.shields.io/badge/-Ollama-orange) ![Pixi](https://img.shields.io/badge/-Pixi-663399?logo=pixi&logoColor=white) | ![live](https://img.shields.io/badge/-live-2EA043) | **22 commits** <br> Dual-track Ingestion <br> Local LLM Serving | Intelligent QA assistant for the NVIDIA CUDA-Q framework. Crawls documentation and clones academic GitHub repos, parses AST/LaTeX formulas, and indexes embeddings into ChromaDB for high-precision retrieval. |
| **EGFR-TKI Resistance Pipeline** <br> [repo](https://github.com/pinchiu/EGFR-TKI-Resistance-Pipeline) | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white) ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) ![TCGA](https://img.shields.io/badge/-TCGA-E11D48) | ![oss](https://img.shields.io/badge/-open_source-3178C6) | **28 commits** <br> TCGA LUAD Cohort <br> Dockerized Workflow | Cancer genomics pipeline analyzing Lung Adenocarcinoma (LUAD) data from TCGA. Examines co-occurrence between sensitizing mutations (19del, L858R) and resistance mutations (T790M, C797S) with automated visualization. |
| **Qingjian 青简** <br> [repo](https://github.com/pinchiu/qingjian) | ![Rust](https://img.shields.io/badge/-Rust-000?logo=rust&logoColor=white) ![C++](https://img.shields.io/badge/-C++-00599C?logo=cplusplus&logoColor=white) | ![oss](https://img.shields.io/badge/-open_source-3178C6) | **70 commits** <br> On-device N-gram <br> &lt;1ms Latency | Cross-platform pinyin input method that displays vocabulary translations next to candidates in the language you are learning. Zero-telemetry, fully local dictionary and adaptive learning engine. |
| **Wisdom-Weasel** <br> [repo](https://github.com/pinchiu/Wisdom-Weasel) | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![Rime](https://img.shields.io/badge/-Rime_Weasel-512BD4) | ![oss](https://img.shields.io/badge/-open_source-3178C6) | **11 commits** <br> IME Extension | LLM-powered context enhancement for Rime (小狼豪) input method, delivering intelligent Chinese text completion and sentence generation. |
| **Antigravity Updater** <br> [repo](https://github.com/pinchiu/antigravity-updater-for-ubuntu) | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![Linux](https://img.shields.io/badge/-Linux-FCC624?logo=linux&logoColor=black) | ![oss](https://img.shields.io/badge/-open_source-3178C6) | **10 commits** <br> Automated CLI | Dedicated updater and maintenance utility for developer workstations running Ubuntu, ensuring reproducible toolchain environments. |
| **Wake-on-LAN for Android** <br> [repo](https://github.com/pinchiu/wake-on-lan-for-android) | ![Kotlin](https://img.shields.io/badge/-Kotlin-7F52FF?logo=kotlin&logoColor=white) ![Android](https://img.shields.io/badge/-Android-3DDC84?logo=android&logoColor=white) | ![oss](https://img.shields.io/badge/-open_source-3178C6) | **63 commits** <br> Native Android | Clean and efficient network utility to wake desktop rigs and servers over local area networks with broadcast magic packets. |
| **USB Sound Connect** <br> [repo](https://github.com/pinchiu/usb-sound-connect) | ![C++](https://img.shields.io/badge/-C++-00599C?logo=cplusplus&logoColor=white) ![Audio](https://img.shields.io/badge/-ALSA_Audio-333) | ![oss](https://img.shields.io/badge/-open_source-3178C6) | **10 commits** <br> Low-level C++ | Lightweight native audio hardware connector and device switcher for Linux audio subsystems. |

<sub>Metrics re-indexed from repositories. Last updated 2026-11-01.</sub>

## 📦 Open Source Repositories

| Repository | Focus &amp; Capability |
|---|---|
| [pinchiu/cudaq-rag-for-school](https://github.com/pinchiu/cudaq-rag-for-school) | Dual-track RAG QA engine for NVIDIA CUDA-Q with LaTeX parsing and ChromaDB |
| [pinchiu/EGFR-TKI-Resistance-Pipeline](https://github.com/pinchiu/EGFR-TKI-Resistance-Pipeline) | Cancer genomics mutation analysis pipeline for TCGA LUAD data |
| [pinchiu/qingjian](https://github.com/pinchiu/qingjian) | High-performance Rust pinyin IME with contextual translation per keystroke |
| [pinchiu/Wisdom-Weasel](https://github.com/pinchiu/Wisdom-Weasel) | LLM-powered completion and text expansion plugin for Rime Weasel |
| [pinchiu/wake-on-lan-for-android](https://github.com/pinchiu/wake-on-lan-for-android) | Native Kotlin Wake-on-LAN client with zero background bloat |
| [pinchiu/antigravity-updater-for-ubuntu](https://github.com/pinchiu/antigravity-updater-for-ubuntu) | Automated developer workstation update script for Ubuntu |
| [pinchiu/usb-sound-connect](https://github.com/pinchiu/usb-sound-connect) | Native C++ sound device management utility |
| [pinchiu/pdf-bookshelf-extension](https://github.com/pinchiu/pdf-bookshelf-extension) | Browser extension for organized document shelving and reader workflows |

## 🛠 Skills & Engineering Capabilities

- **AI & Intelligent Systems** — RAG (Retrieval-Augmented Generation), local LLM orchestration (Ollama, Gemma, Qwen), vector search (ChromaDB), AST parsing, and LaTeX mathematical formula extraction.
- **Computational Biology & Data Science** — High-throughput genomics pipelines, TCGA LUAD cohort mining, GEO microarray analysis, epidemiological ML models (CKD NHANES), variant co-occurrence analysis, and Pandas / NumPy / Seaborn scientific computing.
- **Systems & Core Languages** — **Python** (primary data science and AI language), **Rust** (memory-safe systems and fast input engines), **C++** (low-level device integration), **Kotlin** (native Android), and **C# / .NET** (desktop applications).
- **Tooling & Infrastructure** — Docker & Docker Compose containerization, Pixi reproducible environments, Linux system administration, and GitHub Actions CI/CD automation.

## 🧭 Now

- Advancing **CUDA-Q RAG** with dynamic reranking models and expanded quantum algorithm benchmarks.
- Expanding **EGFR-TKI Resistance Pipeline** to integrate multi-cohort validation and Kaplan-Meier survival curves.
- Optimizing **Qingjian** core Trie dictionary structures for ultra-low latency on macOS and Linux.

## 📈 Languages & Code Distribution

Code volume breakdown across repositories, compiled from codebase analysis:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/languages-dark.svg">
  <img src="./assets/languages-light.svg" alt="Languages by code distribution" width="100%">
</picture>
