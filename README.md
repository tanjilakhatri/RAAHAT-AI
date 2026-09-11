# 🧠 RAAHAT AI

### AI-Based Stress, Trauma & Distress Vulnerability Assessment

<p align="center">

<b>Smart India Hackathon 2026 • SIH 26093</b>

<br>

AI/ML service for analyzing emotional language and generating an explainable
<b>Stress Vulnerability Index (SVI)</b> to support human review.

</p>

---

# 🧠 RAAHAT AI

### AI-Based Stress, Trauma & Distress Vulnerability Assessment

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.9.0-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0.5-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.5.2-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Joblib](https://img.shields.io/badge/Joblib-1.6.0-orange)](https://joblib.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-MVP%20Complete-success)]()
[![SIH 2026](https://img.shields.io/badge/SIH-2026-blueviolet)]()

## 🚀 What is RAAHAT?

**RAAHAT** is an AI-assisted support platform designed for victims and
complainants accessing the **National Helpline and Assistance Architecture
(NHAA – 14566)**.

The AI component analyzes user-provided text for emotional signals such as:

`Fear` • `Sadness` • `Anger` • `Confusion` • `Nervousness`

These signals are transformed into an explainable:

> **Stress Vulnerability Index (SVI)**

The resulting risk indicator can help downstream systems prioritize
appropriate **human review and support**.

### ⚠️ Responsible AI

RAAHAT AI is **not a medical or clinical diagnostic system**.

It does not diagnose:

- Trauma
- PTSD
- Depression
- Anxiety disorders
- Mental illness

AI output is a **supporting vulnerability indicator** and must be reviewed
by appropriate human professionals.

---
# 🧠 RAAHAT AI
        ↓
## 🚀 What is RAAHAT?
        ↓
# 🏗️ RAAHAT Project Architecture    ← ADD IT HERE
        ↓
# ✨ AI Pipeline
        ↓
# 👩‍💻 My Contribution — Member 2
        ↓
# 🛠️ Tech Stack
        ↓
# 📊 Dataset
        ↓
# 🧹 Data Quality & Leakage Prevention
        ↓
# ⚙️ Feature Engineering
        ↓
# 🤖 Model Development
        ↓
# 📈 Model Comparison
        ↓
# 🧩 Emotion Signal Mapping
        ↓
# 📊 Stress Vulnerability Index
        ↓
# 🔍 Example Inference
        ↓
# 🧠 Standalone Inference
        ↓
# 🌐 FastAPI Service
        ↓
# 🧪 Testing
        ↓
# 🔐 Responsible AI
        ↓
# 🚀 Future Roadmap
        ↓
# 📚 Documentation
        ↓
# 👩‍💻 Developer Contribution




# ✨ AI Pipeline

```text
                    USER / COMPLAINANT
                           │
                           ▼
                     Text Input
                           │
                           ▼
                  ┌─────────────────┐
                  │ Text Validation │
                  └────────┬────────┘
                           ▼
                  ┌─────────────────┐
                  │  Preprocessing  │
                  └────────┬────────┘
                           ▼
                  ┌─────────────────┐
                  │ TF-IDF Features │
                  └────────┬────────┘
                           ▼
                  ┌─────────────────┐
                  │   Linear SVM    │
                  └────────┬────────┘
                           ▼
                 Emotion Signal Strengths
                           │
                           ▼
                 Stress Signal Groups
                           │
                           ▼
                Stress Vulnerability Index
                           │
                           ▼
                    Risk Category
                           │
                           ▼
                  👤 HUMAN REVIEW
