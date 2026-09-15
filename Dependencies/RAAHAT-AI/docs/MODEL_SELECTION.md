# RAAHAT AI - Model Selection

## 1. Purpose

This document records the model comparison performed for the RAAHAT AI text-based emotion classification module.

The objective was to select a simple, stable, and explainable machine learning model suitable for the MVP.

## 2. Models Compared

Two traditional machine learning approaches were evaluated:

1. Logistic Regression with One-vs-Rest classification
2. Linear Support Vector Machine with One-vs-Rest classification

Both models used the same TF-IDF text features and the same training and validation data.

## 3. Validation Results

| Metric | Logistic Regression | Linear SVM |
|---|---:|---:|
| Micro Precision | 0.7109 | 0.6485 |
| Micro Recall | 0.2672 | 0.3698 |
| Micro F1 | 0.3884 | 0.4710 |
| Macro F1 | 0.2070 | 0.3332 |
| Hamming Loss | 0.0354 | 0.0349 |

## 4. Model Selection

Linear SVM was selected as the current MVP model.

The main reason is its stronger overall recall and F1 performance compared with Logistic Regression.

Linear SVM achieved:

- Higher Micro Recall
- Higher Micro F1
- Higher Macro F1
- Slightly lower Hamming Loss

Logistic Regression achieved higher Micro Precision, but its recall and F1 scores were lower.

## 5. Selected Model

Selected model:

Linear Support Vector Machine using One-vs-Rest classification.

Feature extraction:

TF-IDF with unigram and bigram features.

The trained model and vectorizer are stored separately in the `models/` directory.

## 6. Important Note About Signal Strength

Linear SVM does not directly provide calibrated probabilities.

For the standalone inference pipeline, SVM decision scores are transformed using a sigmoid function to produce bounded signal-strength values between 0 and 1.

These values are not calibrated probabilities and must not be interpreted as model confidence.

## 7. Limitations

The current model is an MVP text-classification model based primarily on the GoEmotions dataset.

GoEmotions represents general emotional language and is not a clinically validated stress or trauma dataset.

Therefore, the model must not be presented as a medical, psychiatric, or trauma diagnosis system.

The SVI is a support-prioritization indicator intended to assist human review.

## 8. Future Improvement

Future versions may evaluate:

- Hindi and Hinglish-specific datasets
- Multilingual transformer models such as IndicBERT or MuRIL
- Domain-specific stress/distress datasets
- Probability calibration
- Larger representative validation datasets
- Domain-expert evaluation

Any future model should be compared using the same evaluation principles before replacing the current MVP model.