# RAAHAT AI - Member 2 AI/ML Handover Document



## 1. Purpose



This document provides the AI/ML implementation details required for backend integration of the RAAHAT AI stress and distress vulnerability assessment module.



The AI module is designed as a support and prioritization indicator. It is not a clinical or medical diagnostic system.



## 2. AI Input



The AI service accepts a text-based input.



Example:



```json

{

&#x20; "text": "I am scared and confused about what happened."

}



## 3. AI Processing Pipeline



The current inference pipeline is:



1\. Receive text input.

2\. Validate the input.

3\. Normalize the text.

4\. Convert the text into TF-IDF features.

5\. Apply the selected Linear Support Vector Machine model.

6\. Generate emotion predictions and emotion signal strengths.

7\. Calculate grouped stress/distress-related signals.

8\. Calculate the Stress Vulnerability Index (SVI).

9\. Map the SVI score to a risk category.

10\. Return a structured response for backend consumption.



## 4. Selected Model



The selected MVP model is a One-vs-Rest Linear Support Vector Machine.



The model was selected after comparison with the Logistic Regression baseline.



The SVM provided stronger validation recall, Micro F1, Macro F1 and slightly lower Hamming Loss, while Logistic Regression provided higher precision.



The selected model artifact is:



`models/svm\_model.pkl`



The corresponding TF-IDF vectorizer is:



`models/svm\_tfidf\_vectorizer.pkl`



## 5. Feature Engineering



The current model uses TF-IDF text features.



Configuration:



\- Lowercase: enabled

\- N-gram range: 1â€“2

\- Minimum document frequency: 2

\- Maximum features: 10,000



The vectorizer is saved separately so that inference uses the same feature representation as training.



## 6. Emotion Signal Strengths



The inference system produces signal strengths for the supported emotion labels.



These values are model-derived signal strengths and must not be interpreted as calibrated probabilities or clinical confidence scores.



The selected emotion predictions are generated using the current model signal threshold.



## 7. Stress/Distress Signal Groups



The current MVP groups relevant emotions into:



### Fear/Threat



\- fear

\- nervousness



### Sadness/Loss



\- sadness

\- grief

\- disappointment

\- remorse



### Anger/Frustration



\- anger

\- annoyance

\- disapproval

\- disgust



### Confusion/Uncertainty



\- confusion

\- realization



No single emotion independently determines the final risk category.



## 8. Stress Vulnerability Index



The Stress Vulnerability Index (SVI) is an MVP support-prioritization score ranging from 0 to 100.



Current categories:



| SVI Score | Risk Category |

|---|---|

| 0â€“24 | Low |

| 25â€“49 | Moderate |

| 50â€“74 | High |

| 75â€“100 | Very High |



These boundaries are initial MVP rules and require domain-expert validation and representative real-world data before operational deployment.



## 9. API Endpoint



The AI service provides:



`POST /predict`



Example request:



```json

{

&#x20; "text": "I am scared and confused about what happened."

}

## 10. Health Endpoint

The service provides:

`GET /`

Example response:

```json
{
  "service": "RAAHAT AI",
  "status": "running",
  "diagnostic": false
}



## 11. Backend Integration Notes

The backend should:

- Send user text to `POST /predict`.
- Read the structured AI response.
- Use the approved AI fields in the product workflow.
- Treat the result as a support/risk indicator.
- Keep human review in the workflow.

The backend should not:

- Treat the SVI as a medical diagnosis.
- Treat emotion signal strengths as calibrated probabilities.
- Invent new risk thresholds.
- Automatically make sensitive decisions solely from the AI result.

## 12. Safety and Responsible AI

The RAAHAT AI module is not intended to diagnose mental illness, trauma disorders, or any other medical condition.

The AI output should support trained human review rather than replace human judgment.

The system should communicate uncertainty and limitations appropriately.

## 13. Validation Completed

The AI service has been tested for:

- Distress-related input
- Empty input
- Missing required input field
- Repeated identical input
- End-to-end API inference

Final verification example:

- Predicted emotions: confusion, fear
- SVI: 30.46
- Risk category: Moderate
- Human review required: True
- Diagnostic: False

The same input produced the same result across repeated inference runs.

## 14. Project Artifacts

Important AI/ML files:

src/
- preprocessing.py
- features.py
- model.py
- svm_model.py
- risk_mapping.py
- inference.py

models/
- baseline_model.pkl
- tfidf_vectorizer.pkl
- svm_model.pkl
- svm_tfidf_vectorizer.pkl

api.py
requirements.txt

Important documentation:

docs/
- AI_SPECIFICATION.md
- DATASET_SELECTION.md
- STRESS_SIGNAL_MAPPING.md
- SVI_DESIGN.md
- INFERENCE_CONTRACT.md
- MODEL_SELECTION.md
- FASTAPI_INTEGRATION.md
- MEMBER_2_AI_HANDOVER.md

## 15. Backend Handover Summary

Member 2 provides the trained AI model, preprocessing and feature pipeline, inference logic, SVI mapping, API interface and validation rules.

Member 3/backend integration should consume the `/predict` endpoint according to the documented contract and should not modify the AI scoring logic without coordinating with the AI/ML implementation.

## 16. Current AI Status

The AI/ML implementation for the MVP is complete and has been verified through standalone inference and FastAPI integration testing.

Further improvement can include:

- Larger representative datasets
- Domain validation
- Multilingual model evaluation
- Probability calibration
- Stronger trauma/stress-specific data
- Bias evaluation
- Expert review
