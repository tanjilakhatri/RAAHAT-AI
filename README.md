# RAAHAT AI

## AI-Based Stress, Trauma & Distress Vulnerability Assessment

<p align="center">

**Smart India Hackathon 2026 | SIH 26093**

An AI-powered, non-clinical system designed to analyze text-based emotional signals and generate a **Stress Vulnerability Index (SVI)** with interpretable risk indicators and human-review support.

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-scikit--learn-orange)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)
![Status](https://img.shields.io/badge/Project%20Status-Completed-success)
![SIH](https://img.shields.io/badge/Smart%20India%20Hackathon-2026-red)

</p>

---

## Project at a Glance

| Category | Details |
|---|---|
| Project | RAAHAT AI |
| Problem Statement | SIH 26093 |
| Hackathon | Smart India Hackathon 2026 |
| Domain | Artificial Intelligence / Machine Learning |
| Primary Task | Text-based multi-label emotion classification |
| Dataset | GoEmotions |
| Feature Engineering | TF-IDF |
| Classification | Multi-label classification |
| Baseline Model | Logistic Regression |
| Selected MVP Model | Linear Support Vector Machine |
| Inference | Standalone Python inference pipeline |
| AI Service | FastAPI |
| Risk Indicator | Stress Vulnerability Index (SVI) |
| Human Oversight | Human-review flag |
| System Positioning | Non-clinical AI decision-support component |
| Current Status | Completed MVP |

---

## What RAAHAT AI Does

RAAHAT AI processes text input and converts emotional signals into an interpretable vulnerability indicator.

The system follows this pipeline:

```text
User Text
    ↓
Input Validation
    ↓
Text Preprocessing
    ↓
TF-IDF Feature Extraction
    ↓
Multi-Label Emotion Classification
    ↓
Emotion Signal Strength
    ↓
Signal Group Mapping
    ↓
Stress Vulnerability Index (SVI)
    ↓
Risk Category
    ↓
Human Review Indicator
    ↓
FastAPI Response

## Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Project Motivation](#project-motivation)
- [Proposed Solution](#proposed-solution)
- [Project Objectives](#project-objectives)
- [Key Features](#key-features)
- [Complete Project Workflow](#complete-project-workflow)
- [System Architecture](#system-architecture)
- [AI/ML Architecture](#aiml-architecture)
- [Technology Stack](#technology-stack)
- [Dataset](#dataset)
- [Dataset Preparation](#dataset-preparation)
- [Data Quality Analysis](#data-quality-analysis)
- [Duplicate Analysis](#duplicate-analysis)
- [Text Normalization and Grouping](#text-normalization-and-grouping)
- [Data Leakage Prevention](#data-leakage-prevention)
- [Dataset Splitting](#dataset-splitting)
- [Feature Engineering](#feature-engineering)
- [Machine Learning Pipeline](#machine-learning-pipeline)
- [Baseline Model](#baseline-model)
- [Model Evaluation](#model-evaluation)
- [Model Comparison](#model-comparison)
- [Final Model Selection](#final-model-selection)
- [Model Artifacts](#model-artifacts)
- [Standalone Inference](#standalone-inference)
- [Stress Vulnerability Index](#stress-vulnerability-index)
- [Risk Categorization](#risk-categorization)
- [Human Review](#human-review)
- [FastAPI Integration](#fastapi-integration)
- [API Documentation](#api-documentation)
- [AI-to-Backend Integration](#ai-to-backend-integration)
- [Testing](#testing)
- [Responsible AI](#responsible-ai)
- [Privacy and Data Safety](#privacy-and-data-safety)
- [Challenges and Solutions](#challenges-and-solutions)
- [Engineering Decisions](#engineering-decisions)
- [Project Implementation](#project-implementation)
- [Screenshots and Evidence](#screenshots-and-evidence)
- [Project Structure](#project-structure)
- [Current Project Status](#current-project-status)
- [Future Scope](#future-scope)
- [Learning Outcomes](#learning-outcomes)
- [Team Contribution](#team-contribution)
- [Conclusion](#conclusion)
- [Disclaimer](#disclaimer)

---

## Project Overview

RAAHAT AI is an Artificial Intelligence and Machine Learning based system developed for the **Smart India Hackathon 2026 problem statement SIH 26093**.

The project focuses on identifying textual signals associated with stress, trauma, fear, confusion, and other emotional states and converting these signals into a structured vulnerability indicator.

Instead of treating the output as a medical diagnosis, RAAHAT AI is designed as a **non-clinical AI-assisted assessment and decision-support system**.

The machine learning component processes text through a complete pipeline:

```text
Raw Text
   ↓
Text Preprocessing
   ↓
TF-IDF Feature Extraction
   ↓
Multi-Label Emotion Classification
   ↓
Emotion Signal Strength
   ↓
Signal Group Mapping
   ↓
Stress Vulnerability Index (SVI)
   ↓
Risk Category
   ↓
Human Review Indicator

## Problem Statement

Stress and distress can be difficult to identify from limited interactions, especially when people communicate through short text messages or written responses.

Text can contain useful emotional signals such as:

- Fear
- Confusion
- Sadness
- Anger
- Anxiety-related expressions
- Feelings of uncertainty
- Other distress-related emotional patterns

However, raw text is difficult for a conventional application to interpret directly.

The challenge addressed by RAAHAT AI is therefore to build an AI pipeline that can:

1. Accept text input.
2. Preprocess the input consistently.
3. Convert text into machine-readable numerical features.
4. Identify one or more relevant emotional signals.
5. Quantify the resulting emotional signals.
6. Convert those signals into a Stress Vulnerability Index (SVI).
7. Map the result into an interpretable risk category.
8. Indicate when human review may be appropriate.
9. Provide the result through a backend-compatible API.

The system is intentionally positioned as a **non-clinical vulnerability assessment and decision-support component**.

It must not be interpreted as a medical diagnosis, psychological diagnosis, or replacement for a qualified human professional.

## Project Motivation

The motivation behind RAAHAT AI is to explore how Artificial Intelligence can assist in identifying potentially important emotional signals from text.

Traditional software systems generally process text as plain information. They may not understand that different words and expressions can indicate different emotional states.

For example:

```text
"I am scared and confused about what happened."

## Proposed Solution

RAAHAT AI implements an end-to-end machine learning pipeline for text-based emotional signal analysis.

The proposed solution consists of four major layers.

### Layer 1 — Data and Machine Learning

The system uses the GoEmotions dataset to learn relationships between textual expressions and emotion labels.

The dataset is cleaned, validated, normalized, grouped, and split before model training.

### Layer 2 — Emotion Prediction

Text is converted into numerical features using TF-IDF.

A multi-label classification approach is then used because a single text input can express multiple emotions simultaneously.

The project initially establishes a Logistic Regression baseline and then compares it with a Linear Support Vector Machine.

Based on the validation comparison, Linear SVM was selected for the current MVP.

### Layer 3 — Risk Interpretation

The predicted emotion signals are passed to an interpretation layer.

This layer generates:

- Emotion signal strengths
- Signal groups
- Stress Vulnerability Index (SVI)
- Risk category
- Human-review indication

This separates the machine learning prediction from the application-level interpretation.

### Layer 4 — Application Integration

The completed inference pipeline is exposed through FastAPI.

The backend can send text to:

```http
POST /predict

## Project Objectives

The main objective of RAAHAT AI is to develop an AI-assisted system that can analyze text-based emotional signals and convert them into an interpretable vulnerability indicator for further human attention.

The project objectives are:

### 1. Analyze Text-Based Emotional Signals

Develop a machine learning pipeline capable of processing textual input and identifying relevant emotional patterns.

### 2. Perform Multi-Label Emotion Classification

Since a single text can express multiple emotions at the same time, the system is designed to identify multiple relevant emotion labels from a single input.

### 3. Build a Reliable Data Pipeline

Prepare and validate the dataset through:

- Data cleaning
- Missing-value checking
- Duplicate analysis
- Text normalization
- Text grouping
- Leakage prevention
- Train, validation, and test splitting

### 4. Develop Effective Text Features

Convert natural-language text into machine-readable numerical representations using TF-IDF feature engineering with unigram and bigram features.

### 5. Compare Machine Learning Models

Establish a baseline model and compare it with an alternative classifier using validation metrics.

The implemented comparison includes:

```text
Logistic Regression
        VS
Linear Support Vector Machine

## Key Features

- AI-based text emotion analysis
- Multi-label emotion classification
- TF-IDF feature extraction with unigram and bigram features
- One-vs-Rest Linear Support Vector Machine model
- Emotion signal strength calculation
- Stress Vulnerability Index (SVI)
- Risk category generation
- Human review indication
- FastAPI-based AI service
- Structured JSON prediction response
- Input validation and error handling
- Deterministic inference for consistent results
- Automated inference testing
- Responsible AI and non-clinical safety design

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Text Processing | TF-IDF, Unigram & Bigram Features |
| ML Model | One-vs-Rest Linear Support Vector Machine |
| Model Storage | Joblib |
| Backend API | FastAPI |
| API Server | Uvicorn |
| Dataset | GoEmotions |
| Testing | Python-based Inference Tests |
| Version Control | Git, GitHub |
| Development Environment | Windows 11, Python 3.13 |


## Installation & Setup

Follow these steps to set up RAAHAT-AI locally.

### 1. Clone the Repository

```bash
git clone https://github.com/tanjilakhatri/RAAHAT-AI.git
cd RAAHAT-AI
````

Yes. Keep the **Running RAAHAT-AI** section compact enough for one README page.

**MODIFY EXISTING FILE — `README.md`**

Replace the longer version I gave you with this:

````markdown
## Running RAAHAT-AI

After installing the dependencies and activating the virtual environment, start the FastAPI service:

```bash
uvicorn api:app --reload
````

The application will be available at:

```text
http://127.0.0.1:8000
```

### Health Check

Open:

```text
http://127.0.0.1:8000/
```

The service should return its running status.

### Standalone AI Inference

To test the trained model directly:

```bash
python -m src.inference
```

The inference pipeline generates predicted emotions, emotion signal strengths, Stress Vulnerability Index (SVI), risk category, and human-review status.

### Automated Testing

Run:

```bash
python -m tests.test_inference
```

This verifies inference consistency, input handling, output structure, and core inference behavior.

```

**No screenshot needed.**

After this, the next section will be **API Usage**, also kept to one-page style.
```


### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify the Environment

Run:

```bash
python --version
pip --version
```

The project dependencies should now be installed and the virtual environment should be active.

```

### Important

Don't add another screenshot here. This is a **documentation section**, not part of the screenshot section we already closed.

**Next after this:** `Running the RAAHAT-AI Application` — where we document how to start the FastAPI service and run inference. 
```



## Complete Project Workflow

<div align="center">

<table>
<tr>
<td align="center" width="180">

### 📝
<b>USER INPUT</b>

Text message

</td>
<td align="center">→</td>
<td align="center" width="180">

### ✓
<b>VALIDATION</b>

Input checking

</td>
<td align="center">→</td>
<td align="center" width="180">

### ⚙️
<b>PREPROCESSING</b>

Text preparation

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="180">

### 🔢
<b>TF-IDF</b>

Feature extraction

</td>
<td align="center">→</td>
<td align="center" width="180">

### 🧠
<b>LINEAR SVM</b>

ML prediction

</td>
<td align="center">→</td>
<td align="center" width="180">

### 🎯
<b>EMOTIONS</b>

Multi-label output

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="180">

### 📊
<b>SIGNAL STRENGTH</b>

Emotion signals

</td>
<td align="center">→</td>
<td align="center" width="180">

### ⚠️
<b>SVI</b>

Vulnerability score

</td>
<td align="center" width="180">

### 👤
<b>HUMAN REVIEW</b>

Attention indicator

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="180">

### 🚦
<b>RISK CATEGORY</b>

Application-level result

</td>
<td align="center">→</td>
<td align="center" width="180">

### 📦
<b>JSON RESPONSE</b>

Structured output

</td>
<td align="center" width="180">

### 🚀
<b>FASTAPI</b>

AI service

</td>
</tr>
</table>

</div>

### Workflow Explanation

| Stage | Description |
|---|---|
| **1. User Input** | The system receives text from the user. |
| **2. Input Validation** | The input is checked before processing. |
| **3. Text Preprocessing** | The text is prepared for machine learning. |
| **4. TF-IDF** | Text is converted into numerical features. |
| **5. Unigram + Bigram Features** | Individual words and two-word combinations are considered. |
| **6. One-vs-Rest Linear SVM** | The trained model performs multi-label emotion classification. |
| **7. Emotion Prediction** | Multiple relevant emotions can be identified from one text. |
| **8. Emotion Signal Strength** | Predicted emotions are converted into measurable signals. |
| **9. Stress Vulnerability Index** | Emotional signals are mapped into an SVI score. |
| **10. Risk Category** | The SVI is converted into an application-level risk category. |
| **11. Human Review** | The system indicates when human attention should be considered. |
| **12. JSON Response** | Results are returned in a structured format. |
| **13. FastAPI** | The complete AI inference pipeline is exposed through the backend API. |

> **Important:** RAAHAT AI is a non-clinical AI-assisted system. Its output is intended to support human attention and decision-making, not replace qualified human judgment.

## System Architecture

<div align="center">

<table>
<tr>
<td align="center" width="220">

### 👤 USER
Text Input

</td>
<td align="center">→</td>
<td align="center" width="220">

### 🚀 FASTAPI
API Layer

</td>
<td align="center">→</td>
<td align="center" width="220">

### 🧠 AI ENGINE
Inference Pipeline

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="220">

### 📝 TEXT
Preprocessing

</td>
<td align="center">→</td>
<td align="center" width="220">

### 🔢 TF-IDF
Feature Extraction

</td>
<td align="center" width="220">

### 🎯 SVM
Emotion Classification

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="220">

### 📊 SIGNALS
Emotion Strength

</td>
<td align="center">→</td>
<td align="center" width="220">

### ⚠️ SVI
Vulnerability Index

</td>
<td align="center" width="220">

### 👨‍💼 REVIEW
Human Attention

</td>
</tr>
</table>

</div>

### Architecture Components

| Component | Responsibility |
|---|---|
| **User** | Provides text input to the system. |
| **FastAPI** | Receives requests and exposes the AI service. |
| **Inference Pipeline** | Connects preprocessing, vectorization, model prediction and scoring. |
| **TF-IDF** | Converts text into numerical features. |
| **Linear SVM** | Predicts multiple emotional signals. |
| **Emotion Signals** | Represents the detected emotional patterns. |
| **SVI** | Produces the Stress Vulnerability Index. |
| **Risk Category** | Converts the SVI into an application-level category. |
| **Human Review** | Indicates when human attention should be considered. |

> **Architecture Principle:** The AI layer provides an assistive signal. It does not make clinical diagnoses or replace human judgment.

## AI/ML Architecture

<div align="center">

<table>
<tr>
<td align="center" width="180">

### 📥
<b>TEXT INPUT</b>

User message

</td>
<td align="center">→</td>
<td align="center" width="180">

### 🧹
<b>PREPROCESSING</b>

Clean & prepare

</td>
<td align="center">→</td>
<td align="center" width="180">

### 🔢
<b>TF-IDF</b>

10,000 features

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="180">

### 🔤
<b>N-GRAMS</b>

Unigram + Bigram

</td>
<td align="center">→</td>
<td align="center" width="180">

### 🧠
<b>LINEAR SVM</b>

One-vs-Rest

</td>
<td align="center" width="180">

### 🎯
<b>EMOTIONS</b>

Multi-label output

</td>
</tr>

<tr>
<td colspan="5" align="center">↓</td>
</tr>

<tr>
<td align="center" width="180">

### 📊
<b>SIGNALS</b>

Emotion strengths

</td>
<td align="center">→</td>
<td align="center" width="180">

### ⚠️
<b>SVI</b>

Vulnerability score

</td>
<td align="center" width="180">

### 👤
<b>REVIEW</b>

Human attention

</td>
</tr>
</table>

</div>

### Machine Learning Pipeline

```text
Text Input
    │
    ▼
Text Preprocessing
    │
    ▼
TF-IDF Vectorization
    │
    ├── Unigram Features
    └── Bigram Features
    │
    ▼
One-vs-Rest Linear SVM
    │
    ▼
Multi-Label Emotion Classification
    │
    ▼
Emotion Signal Strengths
    │
    ▼
Stress Vulnerability Index (SVI)
    │
    ▼
Risk Category + Human Review Indicator

## My Role as Member 2 — AI/ML

As **Member 2**, my primary responsibility was the AI/ML component of RAAHAT AI.

### Responsibilities

| Area | Contribution |
|---|---|
| Dataset Processing | Prepared and validated the GoEmotions dataset |
| Data Quality | Checked missing values, duplicate IDs and duplicate texts |
| Text Grouping | Created normalized text groups to reduce data leakage |
| Dataset Splitting | Created group-aware train, validation and test splits |
| Feature Engineering | Implemented TF-IDF with unigram and bigram features |
| Model Development | Built the baseline Logistic Regression model |
| Model Comparison | Compared Logistic Regression with Linear SVM |
| Model Selection | Selected Linear SVM for the current MVP |
| Inference | Developed the standalone inference pipeline |
| SVI | Integrated emotion signals into the Stress Vulnerability Index |
| API Integration | Connected AI inference with FastAPI |
| Testing | Tested different input types and inference consistency |
| Responsible AI | Documented limitations, human review and non-clinical use |

### AI/ML Contribution Flow

```text
GoEmotions Dataset
        ↓
Data Cleaning & Validation
        ↓
Duplicate & Leakage Analysis
        ↓
Group-Aware Dataset Split
        ↓
TF-IDF Feature Engineering
        ↓
Model Training
        ↓
Logistic Regression
        ↓
Linear SVM Comparison
        ↓
MVP Model Selection
        ↓
Inference Pipeline
        ↓
Emotion Signals
        ↓
Stress Vulnerability Index
        ↓
FastAPI Integration
        ↓
Testing & Validation

## Dataset

RAAHAT AI uses the **GoEmotions** dataset for emotion classification.

### Dataset Overview

| Property | Details |
|---|---|
| Dataset | GoEmotions |
| Task | Multi-Label Emotion Classification |
| Emotion Labels | 28 |
| Source Files | `goemotions_1.csv`, `goemotions_2.csv`, `goemotions_3.csv` |
| Processed Dataset | `goemotions_consensus.csv` |
| Processed Rows | 54,263 |
| Missing Text | 0 |
| Missing Emotion Labels | 0 |
| Duplicate IDs | 0 |

### Why GoEmotions?

GoEmotions provides a broad set of emotion categories that can be used to identify emotional signals from natural-language text.

The dataset supports the project's multi-label classification approach, where a single text can contain more than one emotional signal.

### Dataset Processing

```text
Raw GoEmotions CSV Files
        ↓
Dataset Combination
        ↓
Consensus-Based Label Preparation
        ↓
Missing Value Validation
        ↓
Duplicate ID Check
        ↓
Duplicate Text Analysis
        ↓
Text Normalization
        ↓
Text Group Creation
        ↓
Group-Aware Dataset Splitting
        ↓
Train / Validation / Test Data

## Dataset Preparation

The dataset preparation process was designed to improve data quality and reduce the possibility of data leakage during model evaluation.

### Preparation Pipeline

```text
Raw CSV Files
      ↓
Combine Dataset
      ↓
Consensus Label Processing
      ↓
Missing Value Check
      ↓
Duplicate ID Check
      ↓
Duplicate Text Analysis
      ↓
Text Normalization
      ↓
Text Group Creation
      ↓
Group-Aware Splitting

## Dataset Preparation

The dataset preparation process was designed to improve data quality and reduce the possibility of data leakage during model evaluation.


## Data Quality Analysis

Before training the machine learning model, the dataset was examined for common data-quality issues.

### Quality Checks Performed

<div align="center">

<table>
<tr>
<td align="center" width="180">

### ✓
<b>Missing Values</b>

0 detected

</td>
<td align="center" width="180">

### ✓
<b>Duplicate IDs</b>

0 detected

</td>
<td align="center" width="180">

### ⚠
<b>Duplicate Text</b>

Analyzed

</td>
</tr>

<tr>
<td align="center" width="180">

### ✓
<b>Text Groups</b>

53,943 unique

</td>
<td align="center" width="180">

### ✓
<b>Emotion Labels</b>

Validated

</td>
<td align="center" width="180">

### ✓
<b>Data Splits</b>

Group-aware

</td>
</tr>
</table>

</div>

### Duplicate Text Analysis

The raw dataset contained repeated text entries. Therefore, duplicate analysis was performed at multiple levels:

- Raw text duplication
- Normalized text duplication
- Duplicate text groups
- Emotion-label differences among duplicate texts

The analysis identified:

| Metric | Result |
|---|---:|
| Duplicate Raw Text Values | 269 |
| Rows Involved | 435 |
| Unique Duplicate Groups | 166 |
| Duplicate Groups With Different Emotion Sets | 74 |
| Unique Normalized Text Groups | 53,943 |
| Duplicate Normalized Groups | 186 |
| Rows in Duplicate Groups | 506 |

### Why This Matters

Duplicate and repeated text can cause overly optimistic model evaluation if the same or highly similar examples appear in both training and evaluation datasets.

To reduce this risk, normalized text groups were used during dataset splitting.

> **Result:** The dataset preparation process was designed to provide a cleaner and more reliable foundation for model training and evaluation.


## Data Quality Analysis

Before training the machine learning model, the dataset was examined for common data-quality issues.

### Quality Checks Performed

<div align="center">

<table>
<tr>
<td align="center" width="180">

### ✓
<b>Missing Values</b>

0 detected

</td>
<td align="center" width="180">

### ✓
<b>Duplicate IDs</b>

0 detected

</td>
<td align="center" width="180">

### ⚠
<b>Duplicate Text</b>

Analyzed

</td>
</tr>

<tr>
<td align="center" width="180">

### ✓
<b>Text Groups</b>

53,943 unique

</td>
<td align="center" width="180">

### ✓
<b>Emotion Labels</b>

Validated

</td>
<td align="center" width="180">

### ✓
<b>Data Splits</b>

Group-aware

</td>
</tr>
</table>

</div>

### Duplicate Text Analysis

The raw dataset contained repeated text entries. Therefore, duplicate analysis was performed at multiple levels:

- Raw text duplication
- Normalized text duplication
- Duplicate text groups
- Emotion-label differences among duplicate texts

The analysis identified:

| Metric | Result |
|---|---:|
| Duplicate Raw Text Values | 269 |
| Rows Involved | 435 |
| Unique Duplicate Groups | 166 |
| Duplicate Groups With Different Emotion Sets | 74 |
| Unique Normalized Text Groups | 53,943 |
| Duplicate Normalized Groups | 186 |
| Rows in Duplicate Groups | 506 |

### Why This Matters

Duplicate and repeated text can cause overly optimistic model evaluation if the same or highly similar examples appear in both training and evaluation datasets.

To reduce this risk, normalized text groups were used during dataset splitting.

> **Result:** The dataset preparation process was designed to provide a cleaner and more reliable foundation for model training and evaluation.

## Data Leakage Prevention

Data leakage can cause machine learning models to appear more accurate than they actually are.

RAAHAT AI addresses this risk by grouping identical or normalized text before creating the dataset splits.

### Leakage Prevention Approach

```text
Raw Text
   ↓
Text Normalization
   ↓
Create Text Group
   ↓
GroupShuffleSplit
   ↓
Train Set
Validation Set
Test Set


## Dataset Splitting

The prepared dataset was divided into three groups for model development and evaluation.

| Dataset Split | Rows | Groups | Purpose |
|---|---:|---:|---|
| Training | 43,412 | 43,154 | Train the machine learning model |
| Validation | 5,418 | 5,394 | Compare and evaluate models |
| Test | 5,433 | 5,395 | Final unseen-data evaluation |

### Split Strategy

The project uses:

```text
GroupShuffleSplit
Random State = 42
Grouping Column = text_group

## Feature Engineering

RAAHAT AI converts natural-language text into numerical features that can be processed by the machine learning model.

### TF-IDF Vectorization

The project uses **Term Frequency–Inverse Document Frequency (TF-IDF)** to represent text numerically.

```text
Raw Text
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Numerical Feature Matrix
   ↓
Linear SVM

## Machine Learning Pipeline

RAAHAT AI uses a multi-label text classification pipeline to identify emotional signals from user-provided text.

### Model Pipeline

```text
Text Input
    ↓
TF-IDF Vectorization
    ↓
Unigram + Bigram Features
    ↓
One-vs-Rest Classification
    ↓
Linear SVM
    ↓
28 Emotion Labels
    ↓
Predicted Emotion Signals

## Model Evaluation

The models were evaluated using the validation dataset with multiple metrics to understand both overall and class-level performance.

### Validation Results

| Metric | Logistic Regression | Linear SVM |
|---|---:|---:|
| Micro Precision | 0.7109 | 0.6485 |
| Micro Recall | 0.2672 | 0.3698 |
| Micro F1 | 0.3884 | 0.4710 |
| Macro F1 | 0.2070 | 0.3332 |
| Hamming Loss | 0.0354 | 0.0349 |

### Evaluation Metrics

**Micro Precision**  
Measures the overall proportion of correctly predicted emotion labels among all predicted labels.

**Micro Recall**  
Measures how many of the relevant emotion labels were successfully identified.

**Micro F1**  
Provides a combined measure of precision and recall across all emotion labels.

**Macro F1**  
Calculates F1 independently for each emotion and then averages the results, giving each emotion equal importance.

**Hamming Loss**  
Measures the fraction of incorrectly predicted labels.

### Baseline Validation

The Logistic Regression baseline achieved:

```text
Micro Precision : 0.7109
Micro Recall    : 0.2672
Micro F1        : 0.3884
Macro F1        : 0.2070
Hamming Loss    : 0.0354


## Model Persistence

After training and selecting the MVP model, the required machine learning artifacts are saved so that the system can perform inference without retraining the model.

### Saved Artifacts

| Artifact | Purpose |
|---|---|
| Trained Model | Performs emotion classification |
| TF-IDF Vectorizer | Converts new text into the same feature representation used during training |
| Evaluation Metrics | Stores model performance information |
| Model Comparison | Stores comparison results between evaluated models |

### Persistence Workflow

```text
Training Dataset
      ↓
Model Training
      ↓
Model Evaluation
      ↓
MVP Model Selection
      ↓
Save Model Artifacts
      ↓
Load Artifacts During Inference
      ↓
Predict New Text


## Standalone Inference

RAAHAT AI provides a separate inference pipeline that loads the saved model and vectorizer to process new text without retraining.

### Inference Flow

```text
New Text Input
      ↓
Input Validation
      ↓
Text Preprocessing
      ↓
Saved TF-IDF Vectorizer
      ↓
Saved Linear SVM Model
      ↓
Emotion Prediction
      ↓
Emotion Signal Strength
      ↓
Stress Vulnerability Index
      ↓
Risk Category
      ↓
Human Review Indicator

## FastAPI Integration

RAAHAT AI exposes the trained inference pipeline through a FastAPI service.

### API Architecture

```text
Client / Frontend
       ↓
   FastAPI API
       ↓
Prediction Request
       ↓
Input Validation
       ↓
run_inference()
       ↓
Saved ML Model + Vectorizer
       ↓
Prediction Processing
       ↓
JSON Response


## API Endpoints

### 1. Health Check

**Method:** `GET`

**Endpoint:**

```text
/

## AI to Backend Integration

The AI/ML pipeline is integrated with the FastAPI backend through a dedicated inference function.

### Integration Flow

```text
Client Request
      ↓
FastAPI `/predict`
      ↓
PredictionRequest
      ↓
run_inference(text)
      ↓
Load TF-IDF Vectorizer
      ↓
Load Linear SVM Model
      ↓
Emotion Prediction
      ↓
Emotion Signal Processing
      ↓
SVI Calculation
      ↓
Risk Category
      ↓
Human Review Indicator
      ↓
JSON Response

## Testing

RAAHAT AI includes inference testing to verify that the AI pipeline behaves correctly across different types of input.

### Test Cases

| Test | Input Type | Result |
|---|---|---|
| 1 | Distress-related text | PASS |
| 2 | Neutral text | PASS |
| 3 | Positive text | PASS |
| 4 | Empty input | PASS |
| 5 | Consistency check | PASS |
| 6 | Whitespace input | PASS |
| 7 | Short text | PASS |
| 8 | Long text | PASS |
| 9 | Special characters | PASS |
| 10 | Output structure | PASS |

### Test Command

```bash
python -m tests.test_inference

## Project Structure

```text
RAAHAT-AI/
│
├── data/
│   └── goemotions/
│       ├── goemotions_1.csv
│       ├── goemotions_2.csv
│       ├── goemotions_3.csv
│       └── goemotions_consensus.csv
│
├── docs/
│
├── images/
│
├── models/
│
├── outputs/
│
├── screenshots/
│
├── src/
│   ├── model.py
│   └── inference.py
│
├── tests/
│   └── test_inference.py
│
├── api.py
├── requirements.txt
├── README.md
└── .gitignore
#### 1. Project Setup & Environment

<p align="center">
  <img src="screenshots/01-project-setup.png" width="850">
</p>

<p align="center">
  <b>Project environment and initial setup</b>
</p>

#### 2. Dataset Collection & Processing

<p align="center">
  <img src="screenshots/02-dataset-processing.png" width="850">
</p>

<p align="center">
  <b>GoEmotions dataset collection, processing, and consensus dataset preparation</b>
</p>

#### 3. Data Quality Analysis

<p align="center">
  <img src="screenshots/03-data-quality-analysis.png" width="850">
</p>

<p align="center">
  <b>Missing-value validation, duplicate analysis, and dataset quality checks</b>
</p>

#### 4. Text Normalization & Grouping

<p align="center">
  <img src="screenshots/04-text-normalization-grouping.png" width="850">
</p>

<p align="center">
  <b>Text normalization and creation of text groups for leakage prevention</b>
</p>

#### 5. Data Leakage Prevention & Dataset Splitting

<p align="center">
  <img src="screenshots/05-data-leakage-dataset-split.png" width="850">
</p>

<p align="center">
  <b>Group-aware dataset splitting using normalized text groups</b>
</p>

#### 6. TF-IDF Feature Engineering

<p align="center">
  <img src="screenshots/06-tfidf-feature-engineering.png" width="850">
</p>

<p align="center">
  <b>TF-IDF vectorization with unigram and bigram features</b>
</p>

#### 7. Baseline Model Training

<p align="center">
  <img src="screenshots/07-baseline-model-implementation.png" width="850">
</p>

<p align="center">
  <b>Implementation of the baseline multi-label emotion classification model using Logistic Regression with One-vs-Rest</b>
</p>


#### 8. Model Comparison & MVP Selection

<p align="center">
  <img src="screenshots/08-model-comparison.png" width="850">
</p>

<p align="center">
  <b>Validation-based comparison of Logistic Regression and Linear SVM</b>
</p>

#### 9. Model Persistence & Artifact Verification

<p align="center">
  <img src="screenshots/09-model-artifact-verification.png" width="850">
</p>

<p align="center">
  <b>Verification of trained model, TF-IDF vectorizer, evaluation metrics, and documentation artifacts</b>
</p>

#### 10. Baseline Model Evaluation

<p align="center">
  <img src="screenshots/10-baseline-model-evaluation.png" width="850">
</p>

<p align="center">
  <b>Validation results of the baseline multi-label emotion classification model using precision, recall, F1-score, Hamming Loss, and Exact Accuracy</b>
</p>

#### 11. Stress Vulnerability Index & Risk Mapping

<p align="center">
  <img src="screenshots/11-svi-risk-mapping.png" width="850">
</p>

<p align="center">
  <b>Conversion of emotion signals into Stress Vulnerability Index (SVI) and risk category</b>
</p>

#### 12. FastAPI Interface Verification

<p align="center">
  <img src="screenshots/12-fastapi-interface-verification.png" width="850">
</p>

<p align="center">
  <b>Verification that the FastAPI interface is ready for integration with the RAAHAT-AI inference service</b>
</p>


#### 13. API Prediction Testing

<p align="center">
  <img src="screenshots/13-api-prediction-test.png" width="850">
</p>

<p align="center">
  <b>Testing the /predict API endpoint with sample text and receiving emotion signals, SVI score, risk category, and human-review indication</b>
</p>

#### 14. Automated Inference Test Suite

<p align="center">
  <img src="screenshots/14-inference-test-suite.png" width="850">
</p>

<p align="center">
  <b>Automated validation of inference behavior, edge cases, consistency, input handling, and output structure</b>
</p>

#### 15. Final Environment Verification

<p align="center">
  <img src="screenshots/15-final-environment-verification.png" width="850">
</p>

<p align="center">
  <b>Final verification of dependencies, AI inference, SVI, risk classification, human review, and overall system status</b>
</p>

#### 16. Responsible AI & Safety Documentation

<p align="center">
  <img src="screenshots/16-responsible-ai-safety-documentation.png" width="850">
</p>

<p align="center">
  <b>Responsible AI documentation covering non-clinical use, human review, limitations, privacy, fairness, safety, and appropriate system usage</b>
</p>

#### 17. Model Artifacts Verification

<p align="center">
  <img src="screenshots/17-model-artifacts-verification.png" width="850">
</p>

<p align="center">
  <b>Verification of the trained model, TF-IDF vectorizer, evaluation metrics, model comparison, and documentation artifacts</b>
</p>

#### 18. AI/ML Feature Specification & Pipeline

<p align="center">
  <img src="screenshots/18-ai-ml-feature-pipeline.png" width="850">
</p>

<p align="center">
  <b>Complete AI/ML pipeline from user text preprocessing and TF-IDF feature extraction to emotion signals and Stress Vulnerability Index</b>
</p>


#### 19. Class-Wise Model Evaluation Metrics

<p align="center">
  <img src="screenshots/19-classwise-model-metrics.png" width="850">
</p>

<p align="center">
  <b>Class-wise evaluation metrics generated for the multi-label emotion classification model</b>
</p>

#### 20. Real Inference Pipeline Test

<p align="center">
  <img src="screenshots/20-real-inference-pipeline-test.png" width="850">
</p>

<p align="center">
  <b>End-to-end inference pipeline test producing emotion predictions, signal strengths, Stress Vulnerability Index, risk category, and human-review indication</b>
</p>

#### 21. Inference Contract Documentation

<p align="center">
  <img src="screenshots/21-inference-contract-documentation.png" width="850">
</p>

<p align="center">
  <b>Inference contract documenting the expected input, output structure, and behavior of the RAAHAT-AI inference pipeline</b>
</p>

#### 22. Inference Robustness Testing

<p align="center">
  <img src="screenshots/22-inference-robustness-testing.png" width="850">
</p>

<p align="center">
  <b>Robustness testing of the inference pipeline across distress-related, neutral, positive, empty, and repeated inputs</b>
</p>

#### 23. Inference Contract Verification

<p align="center">
  <img src="screenshots/23-inference-contract-verification.png" width="850">
</p>

<p align="center">
  <b>Verification of the inference contract, AI prediction output, SVI, risk category, human review, and diagnostic status</b>
</p>

#### 24. Backend Output Verification

<p align="center">
  <img src="screenshots/24-backend-output-verification.png" width="850">
</p>

<p align="center">
  <b>Backend verification of predicted emotions, SVI score, risk category, signal groups, human-review status, and diagnostic flag</b>
</p>

#### 25. Real Inference Pipeline Test

<p align="center">
  <img src="screenshots/25-real-inference-pipeline-test.png" width="850">
</p>

<p align="center">
  <b>Real inference pipeline test demonstrating emotion prediction, signal strength, Stress Vulnerability Index, risk category, and human-review indication</b>
</p>


#### 26. FastAPI Server & Swagger Documentation Verification

<p align="center">
  <img src="screenshots/26-fastapi-swagger-verification.png" width="850">
</p>

<p align="center">
  <b>Verification of the FastAPI service and interactive Swagger API documentation interface</b>
</p>


#### 27. FastAPI API Documentation Interface

<p align="center">
  <img src="screenshots/27-fastapi-api-documentation.png" width="850">
</p>

<p align="center">
  <b>Interactive FastAPI Swagger/OpenAPI interface exposing the RAAHAT-AI API endpoints</b>
</p>


#### 28. FastAPI Health Check

<p align="center">
  <img src="screenshots/28-fastapi-health-check.png" width="850">
</p>

<p align="center">
  <b>Health-check verification confirming that the RAAHAT AI FastAPI service is running and remains non-diagnostic</b>
</p>

#### 29. FastAPI Error Handling Test

<p align="center">
  <img src="screenshots/29-fastapi-error-handling.png" width="850">
</p>

<p align="center">
  <b>API error-handling verification demonstrating how the FastAPI service handles invalid prediction requests</b>
</p>

#### 30. FastAPI Prediction Response Verification

<p align="center">
  <img src="screenshots/30-fastapi-prediction-response.png" width="850">
</p>

<p align="center">
  <b>Verification of the FastAPI prediction endpoint and structured AI inference response</b>
</p>


#### 31. FastAPI API Output Verification

<p align="center">
  <img src="screenshots/31-fastapi-api-output-verification.png" width="850">
</p>

<p align="center">
  <b>Verification of the FastAPI prediction endpoint and structured AI output returned by the RAAHAT AI backend</b>
</p>

#### 32. Optimized Inference Test

<p align="center">
  <img src="screenshots/32-optimized-inference-test.png" width="850">
</p>

<p align="center">
  <b>Optimized inference verification demonstrating emotion prediction, Stress Vulnerability Index, risk classification, and human-review status</b>
</p>

#### 33. Model Artifacts Verification

<p align="center">
  <img src="screenshots/33-model-artifacts-verification.png" width="850">
</p>

<p align="center">
  <b>Verification of the trained model, TF-IDF vectorizer, evaluation metrics, model comparison, and documentation artifacts</b>
</p>


#### 34. Baseline Error Analysis

<p align="center">
  <img src="screenshots/34-baseline-error-analysis.png" width="850">
</p>

<p align="center">
  <b>Baseline error analysis identifying low-performing emotion classes and saving detailed error-analysis results</b>
</p>

#### 35. Linear SVM Validation & Final Model Evaluation

<p align="center">
  <img src="screenshots/35-linear-svm-validation-results.png" width="850">
</p>

<p align="center">
  <b>Validation of the selected One-vs-Rest Linear SVM model with overall and class-wise performance metrics</b>
</p>

#### 36. Linear SVM Model Creation & Environment Verification

<p align="center">
  <img src="screenshots/36-linear-svm-model-creation.png" width="850">
</p>

<p align="center">
  <b>Verification of the Linear SVM model creation and One-vs-Rest multi-label classification setup</b>
</p>

#### 37. Linear SVM Training & Model Persistence

<p align="center">
  <img src="screenshots/37-linear-svm-training-persistence.png" width="850">
</p>

<p align="center">
  <b>Successful Linear SVM training with TF-IDF features and persistence of the trained model and vectorizer artifacts</b>
</p>

#### 38. Stress Signal Mapping Documentation

<p align="center">
  <img src="screenshots/38-stress-signal-mapping-documentation.png" width="850">
</p>

<p align="center">
  <b>Verification of the Stress Signal Mapping documentation used to connect detected emotion signals with the RAAHAT AI risk-assessment workflow</b>
</p>

#### 39. Class-Wise Baseline Metrics

<p align="center">
  <img src="screenshots/39-class-wise-baseline-metrics.png" width="850">
</p>

<p align="center">
  <b>Detailed class-wise evaluation of the baseline multi-label model across individual emotion categories</b>
</p>

#### 40. Text Preprocessing Consistency Test

<p align="center">
  <img src="screenshots/40-preprocessing-consistency-test.png" width="850">
</p>

<p align="center">
  <b>Consistency testing of the text preprocessing pipeline across repeated inference runs and different input samples</b>
</p>


#### 41. Baseline Model Training & Artifact Creation

<p align="center">
  <img src="screenshots/41-baseline-model-training.png" width="850">
</p>

<p align="center">
  <b>Successful baseline model training using TF-IDF features with creation of the trained model and vectorizer artifacts</b>
</p>

#### 42. TF-IDF Feature Extraction Test

<p align="center">
  <img src="screenshots/42-tfidf-feature-extraction-test.png" width="850">
</p>

<p align="center">
  <b>TF-IDF feature extraction verification showing vocabulary size, feature matrix dimensions, and generated unigram and bigram features</b>
</p>

#### 43. Model Comparison Results

<p align="center">
  <img src="screenshots/43-model-comparison-results.png" width="850">
</p>

<p align="center">
  <b>Comparison of Logistic Regression and Linear SVM models using multi-label evaluation metrics for MVP model selection</b>
</p>

#### 44. Baseline Model Configuration Verification

<p align="center">
  <img src="screenshots/44-baseline-model-configuration.png" width="850">
</p>

<p align="center">
  <b>Verification of the baseline One-vs-Rest Logistic Regression model configuration before training</b>
</p>


#### 45. Text Preprocessing Module Implementation

<p align="center">
  <img src="screenshots/45-text-preprocessing-module.png" width="850">
</p>

<p align="center">
  <b>Implementation of the reusable and deterministic text preprocessing module used during training and inference</b>
</p>

#### 46. TF-IDF Feature Engineering Module

<p align="center">
  <img src="screenshots/46-tfidf-feature-engineering-module.png" width="850">
</p>

<p align="center">
  <b>Implementation of the TF-IDF feature engineering module using unigram and bigram text features for machine learning</b>
</p>

#### 47. Stress Vulnerability Index (SVI) Calculation & Risk Mapping

<p align="center">
  <img src="screenshots/47-svi-calculation-risk-mapping.png" width="850">
</p>

<p align="center">
  <b>Real inference demonstration showing emotion signals mapped into the Stress Vulnerability Index, risk category, and human-review requirement</b>
</p>

#### 48. Emotion Class Distribution Analysis

<p align="center">
  <img src="screenshots/48-emotion-class-distribution.png" width="850">
</p>

<p align="center">
  <b>Visualization of the distribution of emotion classes in the processed GoEmotions dataset</b>
</p>

### Screenshot 49 — Text Length Analysis

Text length analysis was performed on the training dataset to understand the distribution of input text before feature engineering and model training.

![Text Length Analysis](screenshots/49-text-length-analysis.png)

## API Usage

RAAHAT-AI provides a REST API using FastAPI for health checking and AI-based text inference.

### 1. Health Check

**Method:** `GET`

**Endpoint:**

```text
http://127.0.0.1:8000/

Example
curl http://127.0.0.1:8000/

Example response
{
  "service": "RAAHAT AI",
  "status": "running",
  "diagnostic": false
}

## Example API Response

A successful `/predict` request returns the processed input, predicted emotions, emotion signal strengths, SVI score, risk category, signal groups, and human-review status.

```json
{
  "input_text": "I am very scared and confused about what happened.",
  "predicted_emotions": ["confusion", "fear"],
  "svi_score": 30.46,
  "risk_category": "Moderate",
  "human_review_required": true,
  "diagnostic": false
}

## Limitations

RAAHAT-AI is an MVP designed for non-clinical stress and distress vulnerability assessment. The current system has the following limitations:

- The model is trained on text-based emotion data and may not capture every form of human distress.
- Predictions may contain false positives or false negatives.
- The system may perform differently across languages, writing styles, and cultural contexts.
- The Stress Vulnerability Index (SVI) is an indicator and should not be interpreted as a clinical score.
- Human review is required for situations where the system identifies a moderate or higher vulnerability signal.
- The current model requires further validation on diverse, real-world datasets.

> **Important:** RAAHAT-AI does not diagnose mental health conditions and should not replace professional assessment.

## Responsible AI & Safety

RAAHAT-AI is designed as a **non-clinical AI support system** for identifying potential stress, trauma, and distress vulnerability signals from text.

### Safety Principles

- The system does **not provide medical or psychological diagnosis**.
- The Stress Vulnerability Index (SVI) is an indicator, not a clinical measurement.
- AI predictions should be treated as supportive signals rather than final decisions.
- Moderate or higher vulnerability signals can be flagged for **human review**.
- The system should not be used as the sole basis for medical, emergency, or other high-impact decisions.
- Model limitations, false positives, false negatives, dataset limitations, and language limitations should be considered when interpreting results.

> **Safety Principle:** RAAHAT-AI supports human decision-making; it does not replace qualified human judgment or professional assessment.

### Next Section: Future Improvements

**MODIFY EXISTING FILE — `README.md`**

Paste **only this** after `## Responsible AI & Safety`:

```markdown id="x3h5qz"
## Future Improvements

The current RAAHAT-AI MVP can be further improved through:

- Training and validating the model on larger and more diverse datasets.
- Improving performance across different languages and writing styles.
- Evaluating additional machine learning and transformer-based models.
- Improving emotion-level and vulnerability-level prediction accuracy.
- Strengthening explainability of AI-generated signals.
- Adding continuous model monitoring and validation.
- Improving privacy and secure handling of user-provided text.
- Conducting broader real-world testing with appropriate human oversight.
- Extending the system with additional responsible AI and safety mechanisms.

These improvements can help make RAAHAT-AI more reliable, explainable, scalable, and suitable for future development.
```

## Team & Contribution

RAAHAT-AI was developed as a team project for **Smart India Hackathon 2026** under Problem Statement **SIH 26093**.

### My Contribution — Member 2: AI/ML

My primary contribution focused on the AI/ML workflow of the project:

- GoEmotions dataset preparation and validation
- Data quality analysis and leakage prevention
- Text preprocessing and normalization
- TF-IDF feature engineering
- Multi-label emotion classification
- Logistic Regression baseline development
- Linear SVM model development and comparison
- Model evaluation and error analysis
- Model persistence and artifact verification
- Inference pipeline development
- Stress Vulnerability Index (SVI) and risk mapping integration
- Inference testing and validation
- FastAPI integration support
- AI/ML documentation and responsible AI documentation

The AI/ML component was designed to provide interpretable, non-clinical vulnerability signals that can support human review.

## Conclusion

RAAHAT-AI is an AI-based, non-clinical system designed to identify potential stress, trauma, and distress vulnerability signals from user-provided text.

The project combines text preprocessing, TF-IDF feature engineering, multi-label emotion classification, Linear SVM, emotion signal mapping, and the Stress Vulnerability Index (SVI) into a complete inference pipeline.

The system also includes FastAPI integration, automated testing, human-review indicators, and responsible AI safeguards.

RAAHAT-AI is currently an MVP and provides supportive vulnerability indicators rather than medical diagnosis. Future improvements can further enhance its accuracy, reliability, explainability, and real-world applicability.
