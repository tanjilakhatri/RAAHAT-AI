# RAAHAT AI - Model and System Limitations



## 1. Purpose



This document records the known limitations of the current RAAHAT AI MVP.



The purpose is to clearly identify where the current AI component may not perform reliably and where additional validation or development is required.



\---



## 2. Dataset Limitation



The current MVP uses the GoEmotions dataset.



GoEmotions is a general emotion-language dataset. It is not a dedicated dataset for:



\- Stress assessment

\- Trauma assessment

\- Victim support

\- Crisis intervention

\- Clinical psychological assessment



Therefore, the current model must not be described as a clinically validated stress or trauma detector.



\---



## 3. Domain-Specific Validation Limitation



The current model has not been validated on a representative dataset of victims or complainants using the intended support-service workflow.



Before operational deployment, domain-specific validation is required.



Such validation should evaluate:



\- Stress-related signals

\- Distress-related signals

\- Different communication styles

\- Realistic support-service inputs

\- False positives

\- False negatives

\- Human-review outcomes



\---



## 4. Language Limitation



The RAAHAT concept targets:



\- Hindi

\- English

\- Hinglish



However, the current MVP was trained using a general emotion-language dataset and has not been fully validated for all Hindi and Hinglish communication patterns.



Performance may vary because of:



\- Transliteration

\- Spelling variations

\- Code-mixed language

\- Regional expressions

\- Informal language

\- Cultural expressions

\- Vocabulary differences



Language-specific evaluation is required before production use.



\---



## 5. Model Limitation



The current selected model is a Linear Support Vector Machine using TF-IDF features.



This model provides a practical and relatively simple MVP approach.



However, it may have difficulty understanding:



\- Long contextual relationships

\- Indirect distress

\- Sarcasm

\- Figurative language

\- Ambiguous statements

\- Cultural context

\- Conversation history

\- Unusual vocabulary

\- Distress expressed without explicit emotional words



\---



## 6. Context Limitation



The current inference system analyzes the supplied text input.



It does not have full understanding of a person's complete real-world situation.



For example, the same emotional phrase may have different meanings depending on:



\- Previous conversation

\- Personal circumstances

\- Current environment

\- Relationship between people

\- Events being discussed



Therefore, the AI output should not be interpreted independently from relevant human context.



\---



## 7. Short Input Limitation



Very short inputs may contain insufficient information for reliable interpretation.



Examples include:



\- "Help."

\- "Scared."

\- "I can't."



Such inputs can still produce an AI result, but the result may have limited contextual meaning.



Human review is particularly important for short or ambiguous inputs.



\---



## 8. Long Input Limitation



Long inputs may contain multiple topics, emotions, or events.



The current MVP does not perform full conversation-level reasoning.



A long message may therefore produce a result that does not fully represent every part of the user's situation.



\---



## 9. False Positive Limitation



A false positive occurs when the system identifies stronger distress-related signals even though elevated support may not be required.



Possible causes include:



\- Emotional words used in a normal context

\- Discussion of another person's situation

\- Sarcasm

\- Figurative language

\- Temporary emotions

\- Ambiguous wording



The AI output should therefore not automatically trigger a final decision.



\---



## 10. False Negative Limitation



A false negative occurs when the system does not identify strong distress-related signals even though significant distress may be present.



Possible causes include:



\- Indirect communication

\- Very short input

\- Unusual wording

\- Language mismatch

\- Missing context

\- Cultural expressions

\- Distress without explicit emotional vocabulary



A low SVI score must not be interpreted as proof that a person does not need support.



\---



## 11. SVI Threshold Limitation



The current SVI categories are:



| SVI Range | Risk Category |

|---|---|

| 0-24 | Low |

| 25-49 | Moderate |

| 50-74 | High |

| 75-100 | Very High |



These are initial MVP boundaries.



They are not clinically validated thresholds.



The boundaries should be reviewed using representative domain-specific data and appropriate domain expertise before operational use.



\---



## 12. Signal Strength Limitation



The current system converts Linear SVM decision scores into bounded signal-strength values using a sigmoid transformation.



These values are used as relative signal strengths.



They are not calibrated probabilities.



They must not be interpreted as:



\- Probability of trauma

\- Probability of psychological distress

\- Model confidence

\- Clinical certainty



\---



## 13. Emotion Mapping Limitation



The current system groups selected emotions into broader stress-related signal groups.



Current groups include:



\- Fear / Threat

\- Sadness / Loss

\- Anger / Frustration

\- Confusion / Uncertainty



These groups are design-level indicators for the MVP.



They do not represent clinical psychological categories.



No single emotion should independently determine a person's final support decision.



\---



## 14. Generalization Limitation



Model performance observed on the validation data may not remain the same on unseen real-world data.



Differences may occur because of:



\- Dataset shift

\- Different language patterns

\- Different user populations

\- Different communication environments

\- New vocabulary

\- Different emotional contexts



Real-world monitoring and periodic evaluation would therefore be required for production use.



\---



## 15. Bias and Fairness Limitation



Training data may not represent all communication styles and user groups equally.



Potential differences may occur across:



\- Language

\- Region

\- Culture

\- Writing style

\- Vocabulary

\- Communication ability



Fairness and subgroup evaluation should be performed using appropriate and ethically justified data before operational deployment.



\---



## 16. Privacy Limitation



User-provided text may contain sensitive personal information.



The current MVP documentation identifies privacy requirements but does not claim that complete production privacy controls have been implemented.



Production deployment should define and enforce:



\- Access controls

\- Secure communication

\- Data retention rules

\- Logging controls

\- Data protection procedures

\- Appropriate handling of sensitive information



\---



## 17. Human Review Limitation



The AI system is designed to support human review.



The current output includes:



`human\_review\_required = true`



The AI should not independently determine:



\- Medical decisions

\- Psychological diagnoses

\- Legal conclusions

\- Criminal responsibility

\- Final support eligibility

\- Emergency actions



Human reviewers and established operational procedures remain necessary.



\---



## 18. Production Readiness Limitation



The current implementation is an MVP AI component.



Before production deployment, additional work may be required for:



\- Domain-specific validation

\- Language evaluation

\- Fairness evaluation

\- Probability calibration where appropriate

\- Security controls

\- Privacy controls

\- Monitoring

\- Model drift detection

\- Operational testing

\- Human-review workflow validation



\---



## 19. Dependency Limitation



The AI service depends on compatible versions of:



\- Python

\- Pandas

\- NumPy

\- scikit-learn

\- joblib

\- FastAPI

\- Uvicorn



The trained model and preprocessing artifacts must remain compatible.



Changes to the model or preprocessing pipeline should be versioned and tested before use.



\---



## 20. Reproducibility Limitation



The current project documents model selection, preprocessing, model artifacts, evaluation results, and inference behavior.



However, future changes to:



\- Dataset

\- Preprocessing

\- Features

\- Model

\- Dependencies

\- Risk mapping



may change the output.



Such changes should be versioned and evaluated before replacing the current MVP artifacts.



\---



## 21. Testing Limitation



The current MVP includes inference tests covering:



\- Distress input

\- Neutral input

\- Positive input

\- Empty input

\- Repeated-input consistency

\- Whitespace input

\- Short input

\- Long input

\- Special-character input

\- Output structure



These tests verify important technical behavior.



They do not prove clinical validity or real-world effectiveness.



\---



## 22. Current Model Performance Limitation



The selected Linear SVM achieved the following validation results:



| Metric | Linear SVM |

|---|---:|

| Micro Precision | 0.6485 |

| Micro Recall | 0.3698 |

| Micro F1 | 0.4710 |

| Macro F1 | 0.3332 |

| Hamming Loss | 0.0349 |



These results are based on the current validation dataset and should not be interpreted as real-world clinical performance.



\---



## 23. No Clinical Performance Claim



The current model metrics must not be presented as evidence that the system can accurately diagnose stress, trauma, psychological disorders, or mental health conditions.



The evaluation measures machine-learning performance on the current dataset.



It does not establish clinical effectiveness.



\---



## 24. Future Improvements



Potential future improvements include:



\- Domain-specific datasets

\- Better Hindi and Hinglish validation

\- Multilingual transformer models

\- Context-aware models

\- Probability calibration

\- Fairness evaluation

\- Human-in-the-loop evaluation

\- Model monitoring

\- Data drift detection

\- Better domain-specific risk mapping

\- Expanded testing



Advanced models should only be introduced after the current pipeline is properly validated.



\---



## 25. Final Limitation Statement



RAAHAT AI is currently an MVP AI decision-support component.



Its output is a non-clinical indicator of potential stress and distress-related emotional signals.



The system should not be used as a standalone diagnostic, legal, medical, psychological, or emergency decision-making system.



Further representative data, domain-specific validation, expert review, safety evaluation, privacy controls, and operational testing are required before considering real-world deployment.


