\# RAAHAT AI - Model and Preprocessing Versioning



\## 1. Purpose



This document defines the versioning and traceability approach for the RAAHAT AI machine learning model and preprocessing artifacts.



The purpose is to ensure that the model used during standalone inference can be identified and matched with the preprocessing artifacts used during training.



\---



\## 2. Selected Model



The selected model for the current MVP is:



Linear Support Vector Machine (Linear SVM)



Implementation:



scikit-learn LinearSVC



Multi-label strategy:



OneVsRestClassifier



The SVM model was selected after comparison with the Logistic Regression baseline.



\---



\## 3. Current Model Artifact



The selected trained model is stored as:



models/svm\_model.pkl



This file contains the trained multi-label Linear SVM model used by the current inference pipeline.



\---



\## 4. Current Preprocessing Artifact



The TF-IDF vectorizer associated with the selected SVM model is stored as:



models/svm\_tfidf\_vectorizer.pkl



This vectorizer must be used together with the selected SVM model.



The vectorizer should not be replaced with a separately fitted vectorizer during inference.



\---



\## 5. Current Artifact Set



| Component | File | Status |

|---|---|---|

| Selected model | models/svm\_model.pkl | Available |

| Selected TF-IDF vectorizer | models/svm\_tfidf\_vectorizer.pkl | Available |

| Baseline model | models/baseline\_model.pkl | Available |

| Baseline TF-IDF vectorizer | models/tfidf\_vectorizer.pkl | Available |



The SVM model and svm\_tfidf\_vectorizer are the active production-MVP inference pair.



\---



\## 6. Model Version



Current MVP model version:



RAAHAT-SVM-MVP-1.0



This version identifies the current selected SVM model artifact and its associated inference configuration.



\---



\## 7. Preprocessing Version



Current preprocessing version:



RAAHAT-TFIDF-MVP-1.0



The preprocessing version represents the current text normalization and TF-IDF feature extraction configuration used by the selected model.



\---



\## 8. Preprocessing Configuration



The current TF-IDF configuration is:



\- lowercase = True

\- ngram\_range = (1, 2)

\- min\_df = 2

\- max\_features = 10,000



Text preprocessing performs:



1\. None handling

2\. String conversion

3\. Leading and trailing whitespace removal

4\. Repeated whitespace normalization



\---



\## 9. Model and Preprocessing Compatibility



The following components must remain compatible:



Model:



RAAHAT-SVM-MVP-1.0



Preprocessing:



RAAHAT-TFIDF-MVP-1.0



If preprocessing or TF-IDF configuration changes significantly, the model should be retrained and assigned a new compatible version.



\---



\## 10. Inference Artifact Loading



The standalone inference module loads the saved SVM model and saved TF-IDF vectorizer.



The current inference pipeline is:



Input Text

&#x20;   |

&#x20;   v

Input Validation

&#x20;   |

&#x20;   v

Text Preprocessing

&#x20;   |

&#x20;   v

Saved TF-IDF Vectorizer

&#x20;   |

&#x20;   v

Saved SVM Model

&#x20;   |

&#x20;   v

Emotion Signals

&#x20;   |

&#x20;   v

Stress Vulnerability Index

&#x20;   |

&#x20;   v

Structured Response



This allows inference to run without requiring a training notebook.



\---



\## 11. Why Versioning Is Required



Versioning is required so that:



\- The deployed model can be identified.

\- The preprocessing configuration can be identified.

\- Model and vectorizer compatibility can be maintained.

\- Previous model artifacts can be distinguished from newer versions.

\- Backend integration can reference a known model version.

\- Evaluation results can be linked to the correct model.

\- Future model updates can be tracked.



\---



\## 12. Model Update Rule



When a new model is trained, the following should be updated:



1\. Model version

2\. Model artifact

3\. Preprocessing version if preprocessing changes

4\. Evaluation results

5\. Model selection documentation

6\. Inference configuration

7\. Backend handover documentation



A new model should not silently replace an existing model without recording its version.



\---



\## 13. Preprocessing Update Rule



If preprocessing changes, the change must be documented.



Examples include:



\- Changing text normalization

\- Changing TF-IDF n-gram configuration

\- Changing minimum document frequency

\- Changing maximum feature count

\- Introducing a new text transformation



If the preprocessing change affects the feature representation, the model should normally be retrained using the new preprocessing configuration.



\---



\## 14. Reproducibility



The current project maintains reproducibility through:



\- Documented dataset preparation

\- Leakage-safe train/validation/test splitting

\- Reusable preprocessing code

\- Saved TF-IDF vectorizer

\- Saved trained model

\- Documented model configuration

\- Recorded evaluation metrics

\- Documented inference contract



The training and inference environments should use compatible dependency versions.



\---



\## 15. Artifact Verification



The current model directory was verified to contain:



baseline\_model.pkl



tfidf\_vectorizer.pkl



svm\_model.pkl



svm\_tfidf\_vectorizer.pkl



The selected SVM model and its TF-IDF vectorizer are available for standalone inference.



\---



\## 16. Model Selection Relationship



The current SVM model was selected because it provided stronger validation performance on the primary multi-label metrics compared with the Logistic Regression baseline.



Validation comparison:



| Metric | Logistic Regression | Linear SVM |

|---|---:|---:|

| Micro Precision | 0.7109 | 0.6485 |

| Micro Recall | 0.2672 | 0.3698 |

| Micro F1 | 0.3884 | 0.4710 |

| Macro F1 | 0.2070 | 0.3332 |

| Hamming Loss | 0.0354 | 0.0349 |



The Linear SVM provided better recall, Micro F1, Macro F1, and Hamming Loss.



\---



\## 17. Important Signal-Strength Note



The current SVM inference pipeline uses decision scores and applies a sigmoid transformation to obtain bounded signal-strength values.



These values are not calibrated probabilities.



They must not be described as model confidence or as the probability that an emotion is present.



They are used as model-derived signal strengths for the project's downstream stress/distress signal mapping.



\---



\## 18. Risk Output Versioning



The model output is passed to the RAAHAT Stress Vulnerability Index mapping.



The risk mapping is separately documented in:



docs/SVI\_DESIGN.md



and:



docs/STRESS\_SIGNAL\_MAPPING.md



Changes to risk boundaries or risk interpretation must be documented separately from changes to the machine learning model.



\---



\## 19. Backend Handover



The backend integration should use the known-good model artifact pair:



models/svm\_model.pkl



models/svm\_tfidf\_vectorizer.pkl



The backend should consume the structured output from the FastAPI AI service rather than loading the model directly.



The current API endpoint is:



POST /predict



\---



\## 20. Current Status



Status: COMPLETED FOR MVP



Current active model:



RAAHAT-SVM-MVP-1.0



Current preprocessing:



RAAHAT-TFIDF-MVP-1.0



Current model artifact:



models/svm\_model.pkl



Current preprocessing artifact:



models/svm\_tfidf\_vectorizer.pkl



The model and preprocessing artifacts have been verified and are ready for the current MVP inference pipeline and backend handover.

