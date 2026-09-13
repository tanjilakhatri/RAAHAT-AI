<div align="center">

# RAAHAT AI

### AI-Based Stress, Trauma & Distress Vulnerability Assessment

**Smart India Hackathon 2026 · SIH 26093**

[![Smart India Hackathon](https://img.shields.io/badge/Smart%20India%20Hackathon-2026-orange?style=for-the-badge)](https://www.sih.gov.in/)
[![SIH 26093](https://img.shields.io/badge/SIH-26093-blue?style=for-the-badge)](https://www.sih.gov.in/)
[![Status](https://img.shields.io/badge/Status-Completed%20MVP-success?style=for-the-badge)](#current-status)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit Learn](https://img.shields.io/badge/Scikit--learn-1.9.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-1.0.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![TF-IDF](https://img.shields.io/badge/NLP-TF--IDF-purple?style=for-the-badge)](#tf-idf-feature-engineering)
[![Linear SVM](https://img.shields.io/badge/Model-Linear%20SVM-red?style=for-the-badge)](#final-model-selection)
[![GoEmotions](https://img.shields.io/badge/Dataset-GoEmotions-yellow?style=for-the-badge)](#dataset)
[![GitHub Stars](https://img.shields.io/github/stars/tanjilakhatri/RAAHAT-AI?style=for-the-badge)](https://github.com/tanjilakhatri/RAAHAT-AI/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/tanjilakhatri/RAAHAT-AI?style=for-the-badge)](https://github.com/tanjilakhatri/RAAHAT-AI/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/tanjilakhatri/RAAHAT-AI?style=for-the-badge)](https://github.com/tanjilakhatri/RAAHAT-AI/commits/main)

**An AI-assisted, non-clinical vulnerability assessment service designed to identify emotion and distress-related signals from user-provided text and generate a structured indicator for human review.**

</div>

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Proposed Solution](#proposed-solution)
- [Key Features](#key-features)
- [System Workflow](#system-workflow)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Dataset](#dataset)
- [Dataset Preparation](#dataset-preparation)
- [Data Quality](#data-quality)
- [Leakage Prevention](#leakage-prevention)
- [Text Preprocessing](#text-preprocessing)
- [TF-IDF Feature Engineering](#tf-idf-feature-engineering)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Baseline Model](#baseline-model)
- [Model Evaluation](#model-evaluation)
- [Model Comparison](#model-comparison)
- [Final Model Selection](#final-model-selection)
- [Model Artifacts](#model-artifacts)
- [Inference Pipeline](#inference-pipeline)
- [Stress Vulnerability Index](#stress-vulnerability-index)
- [Risk Categorization](#risk-categorization)
- [Human Review](#human-review)
- [FastAPI Service](#fastapi-service)
- [API Usage](#api-usage)
- [Testing](#testing)
- [Responsible AI](#responsible-ai)
- [Limitations](#limitations)
- [Project Structure](#project-structure)
- [Implementation Evidence](#implementation-evidence)
- [Member 2 Contribution](#member-2-contribution)
- [Current Status](#current-status)
- [Future Scope](#future-scope)
- [Learning Outcomes](#learning-outcomes)
- [Conclusion](#conclusion)
- [Disclaimer](#disclaimer)

---

## Problem Statement

**SIH 26093 — AI-Based Real-Time Stress and Trauma Assessment Module for Victims/Complainants Accessing NHAA (14566) and Integrated Portal**

RAAHAT AI focuses on the AI/ML component of the proposed system. The objective is to process user-provided text and identify emotion-related signals that may indicate elevated stress or distress vulnerability.

The system is designed as an **AI-assisted decision-support component**, where its output can support prioritization and further human review.

It is **not a clinical or medical diagnostic system**.

---

## Proposed Solution

RAAHAT AI uses a machine-learning pipeline to transform user text into structured emotion signals and an application-specific **Stress Vulnerability Index (SVI)**.

The current MVP uses:

- GoEmotions dataset
- Text normalization
- TF-IDF feature extraction
- One-vs-Rest multi-label classification
- Logistic Regression baseline
- One-vs-Rest Linear SVM
- Emotion signal mapping
- Stress Vulnerability Index
- Risk categorization
- Human-review signaling
- Standalone inference
- FastAPI integration
- Responsible AI safeguards

---

## Key Features

| Feature | Description |
|---|---|
| Multi-label NLP | Predicts multiple emotion labels from a single text input |
| Data Quality Analysis | Checks missing values, duplicates and label quality |
| Leakage Prevention | Uses normalized text grouping before dataset splitting |
| TF-IDF | Converts text into sparse numerical features |
| Baseline Model | One-vs-Rest Logistic Regression |
| Final MVP Model | One-vs-Rest Linear SVM |
| Model Comparison | Compares precision, recall, F1 and Hamming Loss |
| Emotion Signals | Groups model outputs into interpretable signal categories |
| SVI | Converts emotional signals into an application-specific vulnerability indicator |
| Human Review | Every result is marked for human review |
| Standalone Inference | Model artifacts are persisted for inference without retraining |
| FastAPI | Exposes health and prediction endpoints |
| Validation | Includes robustness and API-level testing |
| Responsible AI | Includes safety, bias, privacy and limitation considerations |

---

## System Workflow

```text
                    USER / COMPLAINANT
                           │
                           ▼
                    Text Input
                           │
                           ▼
                  Text Preprocessing
                           │
                           ▼
                  TF-IDF Vectorization
                           │
                           ▼
              One-vs-Rest Linear SVM
                           │
                           ▼
                Emotion Signal Outputs
                           │
                           ▼
              Stress Signal Mapping
                           │
                           ▼
             Stress Vulnerability Index
                         (SVI)
                           │
                           ▼
                 Risk Categorization
                           │
                           ▼
                  Human Review Flag
                           │
                           ▼
                 Structured AI Output
