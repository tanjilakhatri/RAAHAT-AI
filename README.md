::: {align="center"}
# RAAHAT AI

### AI-Based Stress, Trauma & Distress Vulnerability Assessment

**Smart India Hackathon 2026 --- SIH 26093**

```{=html}
<p>
```
`<img src="https://img.shields.io/badge/SIH-2026-6f42c1?style=for-the-badge" alt="SIH 2026">`{=html}
`<img src="https://img.shields.io/badge/AI%2FML-Member%202-4c1d95?style=for-the-badge" alt="AI ML Member 2">`{=html}
`<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">`{=html}
`<img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">`{=html}
`<img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">`{=html}
`<img src="https://img.shields.io/badge/FastAPI-API%20Integration-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">`{=html}
`<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License">`{=html}
```{=html}
</p>
```
```{=html}
<p>
```
`<strong>`{=html}From text data to an explainable vulnerability
indicator --- designed for reliable AI-to-Backend handoff and human
review.`</strong>`{=html}
```{=html}
</p>
```
:::

------------------------------------------------------------------------

## Table of Contents

-   [Overview](#overview)
-   [Problem Statement](#problem-statement)
-   [Proposed AI Solution](#proposed-ai-solution)
-   [Project Architecture](#project-architecture)
-   [AI Pipeline](#ai-pipeline)
-   [Member 2 Contribution](#member-2-contribution)
-   [Dataset and Data Preparation](#dataset-and-data-preparation)
-   [Feature Engineering](#feature-engineering)
-   [Model Development and
    Evaluation](#model-development-and-evaluation)
-   [Risk Output](#risk-output)
-   [Standalone Inference](#standalone-inference)
-   [Backend Handoff Contract](#backend-handoff-contract)
-   [Testing Strategy](#testing-strategy)
-   [Responsible AI](#responsible-ai)
-   [Data and Model Governance](#data-and-model-governance)
-   [Technology Stack](#technology-stack)
-   [Project Structure](#project-structure)
-   [Getting Started](#getting-started)
-   [Limitations](#limitations)
-   [Future Improvements](#future-improvements)
-   [Definition of Done](#definition-of-done)
-   [License](#license)

------------------------------------------------------------------------

## Overview

**RAAHAT AI** is the Artificial Intelligence and Machine Learning
component of the RAAHAT project for Smart India Hackathon 2026.

The AI component is designed to transform valid assessment input into a
**consistent, documented and appropriately qualified vulnerability/risk
output** that can be consumed by the Backend and ultimately reviewed by
the appropriate human stakeholders.

The Member 2 scope covers the complete AI intelligence path:

> **Problem Definition → Data Preparation → Features → Model →
> Evaluation → Risk Output → Inference → Backend Handoff → Responsible
> AI**

The project follows an important engineering principle:

> **A simple, evaluated, reproducible and explainable model is more
> valuable than unnecessary model complexity.**

------------------------------------------------------------------------

## Quick Highlights

-   AI/ML-focused component for stress, trauma and distress
    vulnerability assessment
-   Structured data preparation and reproducible preprocessing
-   Feature engineering with documented feature definitions
-   Baseline-first model development
-   Precision, Recall, F1-score and Confusion Matrix based evaluation
-   Defined risk-score/category mapping
-   Standalone inference without requiring the training notebook
-   Stable AI-to-Backend contract
-   Input validation and controlled error handling
-   Model and preprocessing version tracking
-   Responsible AI and non-diagnostic positioning
-   Designed for integration with the wider RAAHAT system

------------------------------------------------------------------------

## Problem Statement

Systems dealing with stress, trauma and distress-related complaints need
a consistent way to identify signals that may require additional
attention.

The AI component must therefore do more than produce a prediction. It
should provide a workflow that is:

-   Reproducible
-   Evaluated
-   Explainable
-   Consistent
-   Safe to integrate
-   Clear about limitations

The model output is intended as a **decision-support / risk
indication**, not as a clinical diagnosis.

------------------------------------------------------------------------

## Proposed AI Solution

RAAHAT AI follows a structured machine-learning workflow.

``` text
                ┌──────────────────────┐
                │   Assessment Input   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Input Validation   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Preprocessing     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Feature Engineering  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    ML Prediction     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Risk Mapping       │
                │ Score / Category     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Human Review       │
                └──────────────────────┘
```

------------------------------------------------------------------------

## Project Architecture

> **Architecture image:** add the final architecture diagram to\
> `images/raahat-architecture.png`

```{=html}
<p align="center">
```
`<img src="images/raahat-architecture.png" alt="RAAHAT AI Project Architecture" width="100%">`{=html}
```{=html}
</p>
```
### Architecture Layers

  -----------------------------------------------------------------------
  Layer                               Responsibility
  ----------------------------------- -----------------------------------
  Input Layer                         Receives the documented assessment
                                      input

  Validation Layer                    Checks required fields, types,
                                      ranges and valid values

  Data Layer                          Handles dataset preparation and
                                      documented preprocessing

  Feature Layer                       Converts approved inputs into
                                      model-ready features

  ML Layer                            Trains, evaluates and executes the
                                      selected model

  Risk Layer                          Converts model output into the
                                      approved score/category

  Inference Layer                     Provides a stable callable
                                      prediction component

  Integration Layer                   Allows Backend to consume the AI
                                      contract

  Human Review                        Provides the final human
                                      interpretation and action
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## AI Pipeline

The AI workflow is designed as a reproducible sequence:

``` text
Input
  │
  ▼
Validate
  │
  ▼
Preprocess
  │
  ▼
Transform into Features
  │
  ▼
Run Selected Model
  │
  ▼
Generate Prediction
  │
  ▼
Map to Risk Output
  │
  ▼
Format Stable Response
  │
  ▼
Backend
  │
  ▼
Human Review
```

### Core Inference Flow

``` text
validate
   ↓
preprocess
   ↓
predict
   ↓
map
   ↓
format response
   ↓
return
```

The same preprocessing used during training must be reused during
inference.

------------------------------------------------------------------------

# Member 2 Contribution

## AI/ML Engineer --- Stress, Trauma & Distress Prediction

Member 2 owns the **AI intelligence layer** from problem definition
through model evaluation, risk output and standalone inference.

### My Responsibility

  -----------------------------------------------------------------------
  Area                                Contribution
  ----------------------------------- -----------------------------------
  AI Problem Definition               Defined target, inputs, outputs,
                                      assumptions and limitations

  Dataset                             Dataset inspection, cleaning
                                      decisions and reproducible
                                      preparation

  Preprocessing                       Documented and leakage-safe
                                      preprocessing

  Feature Engineering                 Defined feature meaning, source,
                                      transformation and rationale

  Model Development                   Baseline and candidate model
                                      development

  Model Evaluation                    Precision, Recall, F1-score and
                                      Confusion Matrix

  Model Selection                     Selected approach using
                                      performance, stability, simplicity
                                      and explainability

  Risk Output                         Defined score/category mapping and
                                      interpretation

  Inference                           Built a standalone prediction path
                                      independent of the notebook

  Testing                             Valid, invalid, repeated-input and
                                      edge-case checks

  Backend Handoff                     Input/output/error contract and
                                      known-good examples

  Responsible AI                      Documented limitations and
                                      non-diagnostic use

  Governance                          Model, feature, preprocessing and
                                      dependency version tracking
  -----------------------------------------------------------------------

### Contribution Flow

``` text
Dataset
   ↓
Data Quality
   ↓
Preprocessing
   ↓
Feature Engineering
   ↓
Baseline
   ↓
Model Comparison
   ↓
Selected Model
   ↓
Risk Mapping
   ↓
Standalone Inference
   ↓
Testing
   ↓
Backend Handoff
```

------------------------------------------------------------------------

## Dataset and Data Preparation

The AI workflow requires documented and reproducible data handling.

### Data Preparation Principles

1.  Inspect rows, columns and data types.
2.  Analyse missing and invalid values.
3.  Identify and handle duplicates when justified.
4.  Document cleaning decisions.
5.  Define the train/validation/test strategy before tuning.
6.  Fit preprocessing only on training data.
7.  Apply learned transformations to validation/test data.
8.  Record known dataset limitations.

### Required Data Artifacts

-   Data dictionary
-   Dataset notes
-   Preprocessing pipeline
-   Split strategy
-   Cleaning decisions
-   Leakage-prevention documentation

------------------------------------------------------------------------

## Feature Engineering

Every feature should have a clear purpose.

For each feature, the project records:

  -----------------------------------------------------------------------
  Field                               Description
  ----------------------------------- -----------------------------------
  Feature Name                        Exact feature name

  Meaning                             What the feature represents

  Type                                Numeric, categorical or other type

  Source                              Original assessment/data field

  Transformation                      Encoding, scaling, aggregation or
                                      other transformation

  Reason                              Why the feature is useful

  Status                              Included/excluded with rationale
  -----------------------------------------------------------------------

The feature specification should be frozen before model comparison. Any
later change should be recorded as a new experiment/version.

------------------------------------------------------------------------

## Model Development and Evaluation

### Baseline-First Strategy

RAAHAT AI follows a baseline-first approach rather than immediately
choosing a complex model.

The baseline helps determine whether the selected features contain
useful predictive signal before additional complexity is introduced.

### Model Selection Principles

The final approach should balance:

-   Performance
-   Stability
-   Simplicity
-   Explainability
-   Reproducibility
-   Integration reliability

A model is **not** selected simply because it is complex or fashionable.

### Evaluation Metrics

  -----------------------------------------------------------------------
  Metric                              Purpose
  ----------------------------------- -----------------------------------
  Precision                           Helps understand false-positive
                                      behaviour

  Recall                              Helps understand missed higher-risk
                                      cases

  F1-score                            Balances precision and recall

  Confusion Matrix                    Shows which classes are being
                                      confused

  Accuracy                            Provides useful overall context but
                                      may be misleading for imbalanced
                                      data
  -----------------------------------------------------------------------

### Model Results

> **Important:** Only verified experiment results should be added here.
> Do not publish estimated or placeholder metrics as actual results.

  Metric                                          Result
  ----------- ------------------------------------------
  Accuracy      To be populated from verified experiment
  Precision     To be populated from verified experiment
  Recall        To be populated from verified experiment
  F1-score      To be populated from verified experiment

### Evaluation Evidence

Recommended repository evidence:

``` text
images/
├── raahat-architecture.png
├── model-results.png
└── api-demo.png
```

------------------------------------------------------------------------

## Risk Output

If a numerical score is used, the project must define:

-   Output type
-   Valid score range
-   Allowed categories
-   Category boundaries
-   Mapping logic
-   Interpretation
-   Limitations

The risk output should be consistent:

> Same model/version + same valid input + deterministic settings →
> consistent output.

### Responsible Interpretation

The risk output is a **vulnerability/risk indicator or decision-support
signal**.

It must **not** be presented as a clinical diagnosis.

------------------------------------------------------------------------

## Standalone Inference

A major completion criterion for Member 2 is that prediction must work
**without opening the training notebook**.

### Standalone Inference Requirements

-   Load the saved model
-   Load the matching preprocessing objects
-   Validate input
-   Apply training-consistent transformations
-   Generate prediction
-   Map prediction to the approved risk structure
-   Return a stable response
-   Handle controlled errors

This creates a clean separation between:

``` text
Training
   ↓
Saved Model + Preprocessing
   ↓
Standalone Inference
   ↓
Backend
```

------------------------------------------------------------------------

## Backend Handoff Contract

The Backend/API layer is owned by the Backend member. Member 2 provides
the AI contract required for integration.

### Handoff Includes

  -----------------------------------------------------------------------
  Item                                Member 2 Provides
  ----------------------------------- -----------------------------------
  Input Schema                        Field names, types,
                                      required/optional fields and valid
                                      values

  Preprocessing                       Exact transformations used before
                                      inference

  Model                               Saved model and dependency/version
                                      information

  Output                              Stable prediction response
                                      structure

  Errors                              Invalid input, unavailable model
                                      and inference behaviour

  Evaluation                          Metrics and selected-model evidence

  Limitations                         Known data/model limitations

  Examples                            Known test payload and expected
                                      response
  -----------------------------------------------------------------------

### Integration Test

``` text
Known Test Payload
       ↓
Input Validation
       ↓
Preprocessing
       ↓
Model Inference
       ↓
Response Schema
       ↓
Backend Receives Expected Result
```

------------------------------------------------------------------------

## Testing Strategy

RAAHAT AI testing focuses on critical prediction behaviour.

  -----------------------------------------------------------------------
  Test Case                           Expected Behaviour
  ----------------------------------- -----------------------------------
  Valid Input                         Stable prediction in documented
                                      format

  Missing Field                       Clear validation error

  Invalid Type/Range                  Safely rejected or handled

  Repeated Input                      Consistent result under
                                      deterministic settings

  Unknown Category                    Safely handled according to
                                      preprocessing

  Model Unavailable                   Controlled error

  Edge Case                           Output remains within valid
                                      range/category

  Preprocessing                       Same transformations as training

  Version Mismatch                    Incompatible model/preprocessing is
                                      detected or identified
  -----------------------------------------------------------------------

### Troubleshooting Flow

``` text
Observe
  ↓
Reproduce
  ↓
Isolate
  ↓
Assign
  ↓
Fix
  ↓
Retest
  ↓
Record
```

AI problems should be fixed at the correct ownership layer rather than
patched in the user interface.

------------------------------------------------------------------------

# Responsible AI

Because RAAHAT deals with stress, trauma and distress, responsible use
is a core engineering requirement.

### The system should

-   Describe output as a risk indicator or decision-support signal.
-   Document dataset limitations.
-   Validate inputs.
-   Restrict unnecessary exposure of sensitive data.
-   Record model and version information.
-   Use consistent approved terminology.
-   Keep human review in the decision process.

### The system should not

-   Claim to diagnose a mental-health condition.
-   Hide uncertainty or known limitations.
-   Treat invalid input as valid prediction data.
-   Expose sensitive case data unnecessarily.
-   Invent risk meanings independently in the UI.
-   Silently replace a model without evidence.

> **Responsible-AI Gate:** If the team cannot clearly explain what the
> model can and cannot infer, the AI component is not ready for
> integration.

------------------------------------------------------------------------

## Data and Model Governance

The project follows a traceable governance checklist.

  Area               Requirement
  ------------------ ----------------------------------------------
  Data Source        Record origin and suitability/permitted use
  Data Dictionary    Every used field has meaning and type
  Sensitive Fields   Avoid unnecessary variables
  Preprocessing      Reproducible and leakage-safe
  Feature Version    Frozen and traceable
  Model Version      Saved and identifiable
  Dependencies       Python/package versions recorded
  Metrics            Evaluation results stored
  Limitations        Known limitations documented
  Inference          Standalone component works independently
  Test Evidence      Known-good test payload and results recorded

------------------------------------------------------------------------

# Technology Stack

::: {align="center"}
  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  **Python**                          AI/ML development and inference

  **Pandas**                          Data cleaning and transformation

  **NumPy**                           Numerical operations

  **scikit-learn**                    Machine-learning models and
                                      evaluation

  **Jupyter Notebook**                Experimentation and analysis

  **VS Code**                         Development

  **Joblib / Model Serialization**    Saving model and preprocessing
                                      objects

  **HTTP API Interface**              AI-to-Backend integration

  **FastAPI**                         API integration layer
  -----------------------------------------------------------------------
:::

------------------------------------------------------------------------

## Project Structure

The repository should follow the actual final implementation. A
recommended structure is:

``` text
RAAHAT-AI/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── experiments/
│
├── src/
│   ├── preprocessing/
│   ├── features/
│   ├── model/
│   ├── inference/
│   └── risk/
│
├── models/
│
├── tests/
│
├── images/
│   ├── raahat-architecture.png
│   ├── model-results.png
│   └── api-demo.png
│
├── docs/
│
├── requirements.txt
├── README.md
└── LICENSE
```

> Keep the structure synchronized with the actual repository. Do not
> document files that do not exist in the final implementation.

------------------------------------------------------------------------

# Getting Started

## 1. Clone the Repository

``` bash
git clone https://github.com/tanjilakhatri/RAAHAT-AI.git
cd RAAHAT-AI
```

## 2. Create a Virtual Environment

### Windows

``` bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

## 4. Run the AI Component

Use the final project entry point documented in the repository.

The final inference component should be callable without opening the
training notebook.

------------------------------------------------------------------------

# Current Implementation Evidence

The project evidence should focus on **real, reproducible outputs**.

Recommended evidence to publish:

### 1. Architecture

`images/raahat-architecture.png`

### 2. Model Evaluation

`images/model-results.png`

Show:

-   Model comparison
-   Precision
-   Recall
-   F1-score
-   Confusion Matrix

### 3. API / Inference

`images/api-demo.png`

Show:

-   Input
-   Successful inference
-   Output structure
-   Validation/error behaviour where relevant

------------------------------------------------------------------------

# Limitations

RAAHAT AI should clearly communicate its limitations.

-   The model is a decision-support/risk-indication component.
-   It is not a clinical diagnostic system.
-   Model behaviour depends on the quality and suitability of the
    training data.
-   Dataset limitations can affect generalisation.
-   Predictions should not be treated as absolute truth.
-   Input validation and preprocessing consistency are required for
    reliable inference.
-   Model/version changes must be documented and evaluated.
-   Human review remains important for consequential decisions.

------------------------------------------------------------------------

# Future Improvements

Once the baseline and inference path are stable, future work can focus
on:

-   Improved dataset coverage and quality
-   More robust validation
-   Class-imbalance handling where required
-   Cross-validation
-   Hyperparameter tuning
-   Model explainability
-   Stronger robustness testing
-   Better version and experiment tracking
-   Production monitoring
-   Privacy and sensitive-data controls
-   Integration testing across AI and Backend
-   Deployment optimisation

### Improvement Principle

> **Improve reproducibility, validation, robustness and evidence before
> adding unnecessary model complexity.**

------------------------------------------------------------------------

# Definition of Done

The Member 2 AI component is considered ready when:

-   [x] AI target is clearly defined
-   [x] Required inputs and outputs are documented
-   [x] Assumptions and limitations are documented
-   [x] Dataset handling is documented
-   [x] Preprocessing is reproducible
-   [x] Data leakage is addressed
-   [x] Features are defined and traceable
-   [x] Baseline/model direction is established
-   [x] Evaluation uses suitable metrics
-   [x] Risk output rules are documented
-   [x] Standalone inference path is defined
-   [x] Input validation is included
-   [x] Invalid and edge-case behaviour is considered
-   [x] Backend handoff contract is defined
-   [x] Responsible-AI limitations are documented

### Final AI Success Condition

> **The Backend member can call the inference component reliably using
> the documented contract, while the team can explain what the model
> predicts, how the data becomes features, why the model was selected,
> what the output means, and what its limitations are.**

------------------------------------------------------------------------

# AI Integration Gate

``` text
A0 — Specification Ready
          ↓
A1 — Data Ready
          ↓
A2 — Features Frozen
          ↓
A3 — Model Evaluated
          ↓
A4 — Inference Ready
          ↓
A5 — Contract Ready
          ↓
A6 — Backend Integration Verified
          ↓
A7 — Release Ready
```

A failed gate means the responsible layer should be investigated,
corrected and retested before moving forward.

------------------------------------------------------------------------

# Why This Engineering Approach?

RAAHAT AI follows a practical machine-learning engineering process
rather than selecting a complex model first.

The workflow prioritises:

**Clean Data → Sensible Features → Baseline → Evaluation → Risk Mapping
→ Standalone Inference → Backend Integration**

This makes the AI component easier to:

-   Test
-   Explain
-   Reproduce
-   Integrate
-   Demonstrate
-   Maintain

------------------------------------------------------------------------

# Smart India Hackathon 2026

**Problem / Project Reference:** SIH 26093

RAAHAT AI is being developed as the AI/ML component of the RAAHAT
solution for Smart India Hackathon 2026.

The Member 2 contribution focuses on making the AI layer **reproducible,
evaluated, explainable, integration-ready and responsibly positioned**.

------------------------------------------------------------------------

# Developer Contribution

**Tanjila Khatri --- Member 2 \| AI/ML Engineer**

Primary focus:

> **Data → Features → Model → Evaluation → Risk Output → Inference →
> Backend Handoff**

The contribution is designed around measurable engineering evidence
rather than only model complexity.

------------------------------------------------------------------------

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

------------------------------------------------------------------------

::: {align="center"}
### RAAHAT AI

**Responsible AI. Reproducible ML. Reliable Integration.**

**Smart India Hackathon 2026 • SIH 26093**
:::
