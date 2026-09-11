# 🧠 RAAHAT AI

### AI-Based Stress, Trauma & Distress Vulnerability Assessment

<p align="center">

<b>Smart India Hackathon 2026 • SIH 26093</b>

<br>

AI/ML service for analyzing emotional language and generating an explainable
<b>Stress Vulnerability Index (SVI)</b> to support human review.

</p>

---

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
