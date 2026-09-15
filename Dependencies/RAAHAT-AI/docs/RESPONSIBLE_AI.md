# RAAHAT AI - Responsible AI and Limitations



## 1. Purpose



RAAHAT AI provides a non-clinical stress and distress vulnerability indicator for victims or complainants interacting with the RAAHAT support system.



The AI analyzes text input, identifies relevant emotional signals, groups those signals into broader stress-related categories, and produces a Stress Vulnerability Index (SVI) and risk category.



The system is intended to support human review and prioritization. It is not intended to replace trained human judgment.



\---



## 2. Non-Clinical System



RAAHAT AI is a non-clinical decision-support system.



The AI output must not be interpreted as:



\- A medical diagnosis

\- A psychological diagnosis

\- A clinical assessment

\- A confirmed trauma diagnosis

\- A statement about a person's mental health condition



The `diagnostic` field is therefore explicitly returned as `false`.



\---



## 3. Human Review Requirement



Every AI assessment is marked:



`human\_review\_required = true`



The AI output should be treated as an indication that may help a human reviewer understand possible emotional or distress-related signals.



Human reviewers remain responsible for interpreting the situation and deciding the appropriate support or follow-up action.



The AI must not independently make final decisions about a victim or complainant.



\---



## 4. AI Processing



The current MVP follows this general flow:



Input Text

â†’ Text Preprocessing

â†’ TF-IDF Feature Extraction

â†’ Linear Support Vector Machine

â†’ Emotion Signal Strengths

â†’ Stress Signal Groups

â†’ Stress Vulnerability Index

â†’ Risk Category

â†’ Human Review



The model uses general emotional-language data and maps selected emotional signals into stress-related groups.



\---



## 5. Stress Vulnerability Index



The current MVP calculates an SVI score from 0 to 100.



The current initial categories are:



| SVI Range | Risk Category |

|---|---|

| 0-24 | Low |

| 25-49 | Moderate |

| 50-74 | High |

| 75-100 | Very High |



These boundaries are initial MVP design values.



They must not be treated as clinically validated thresholds.



Before operational deployment, the mapping should be reviewed and validated using representative domain-specific data and appropriate domain expertise.



\---



## 6. Explainability



RAAHAT AI provides interpretable intermediate signals instead of returning only a final risk category.



The response contains:



\- Predicted emotions

\- Emotion signal strengths

\- Stress signal groups

\- SVI score

\- Risk category

\- Human review requirement

\- Diagnostic flag



The main stress-related signal groups currently include:



\- Fear / Threat

\- Sadness / Loss

\- Anger / Frustration

\- Confusion / Uncertainty



No individual emotion is intended to independently determine a person's overall risk.



\---



## 7. Dataset Limitations



The current model was developed using the GoEmotions dataset.



GoEmotions is a general emotion-language dataset and is not a dedicated clinical trauma or victim-support dataset.



Therefore, the current model should not be described as a clinically validated trauma detector.



The dataset may not fully represent:



\- Victims or complainants using support services

\- Real-world distress conversations

\- Crisis situations

\- Indian legal or support-service contexts

\- Hindi and Hinglish communication patterns

\- Different regional language variations

\- Speech-specific distress signals



Domain-specific data would be required for stronger validation.



\---



## 8. Model Limitations



The current MVP uses TF-IDF features with a Linear Support Vector Machine.



This provides a relatively simple and explainable baseline suitable for the MVP.



However, the model may have difficulty understanding:



\- Complex context

\- Sarcasm

\- Indirect expressions

\- Long-term conversation context

\- Mixed-language expressions

\- Ambiguous statements

\- Cultural context

\- Unusual vocabulary

\- Situations where emotional words do not represent actual distress



Model predictions should therefore be interpreted carefully.



\---



## 9. Emotion Signal Strength Limitation



The current system converts Linear SVM decision scores into bounded signal-strength values using a sigmoid transformation.



These values are used as relative signal strengths for the MVP.



They are \*\*not calibrated probabilities\*\* and must not be interpreted as:



\- Probability of trauma

\- Probability of psychological distress

\- Model confidence

\- Clinical certainty



Future versions may use appropriate probability calibration if required and validated.



\---



## 10. False Positives



A false positive may occur when the system identifies distress-related emotional signals even though the person does not require elevated support.



Possible causes include:



\- Use of emotional words in a non-distress context

\- Discussion of another person's situation

\- Sarcasm or figurative language

\- Strong but temporary emotions

\- Ambiguous language



Human review is important to prevent automatic decisions based only on the AI result.



\---



## 11. False Negatives



A false negative may occur when the system does not identify strong distress-related signals even though a person is experiencing significant distress.



Possible causes include:



\- Indirect communication

\- Very short messages

\- Unusual wording

\- Language mismatch

\- Cultural expressions

\- Missing context

\- Emotional distress without explicit emotional vocabulary



A low AI score must therefore never be treated as proof that a person is safe or does not require support.



\---



## 12. Language Limitations



The RAAHAT concept targets Hindi, English, and Hinglish interactions.



The current MVP model, however, was developed using a general emotion-language dataset and should not be considered fully validated for all Hindi or Hinglish patterns.



Performance may vary across:



\- Hindi

\- English

\- Hinglish

\- Regional expressions

\- Spelling variations

\- Transliteration

\- Code-mixed sentences



Language-specific evaluation and representative datasets are required before production use.



\---



## 13. Bias and Fairness



AI predictions can be affected by limitations or imbalances in the training data.



Potential differences may occur across:



\- Language

\- Writing style

\- Age-related communication patterns

\- Regional expressions

\- Cultural context

\- Vocabulary

\- Communication ability



The system should therefore be evaluated across representative user groups before operational deployment.



Performance should be monitored using class-wise and, where appropriate and ethically justified, subgroup-level evaluation.



\---



## 14. Privacy Considerations



Input text may contain sensitive personal information.



The AI service should therefore follow the project's applicable privacy and security requirements.



Only information required for the intended assessment should be processed.



The system should avoid unnecessary storage or exposure of user-provided text.



Production deployment should include appropriate:



\- Access controls

\- Secure communication

\- Data handling policies

\- Logging controls

\- Retention policies

\- Protection of sensitive information



The current MVP documentation does not claim that production privacy controls are fully implemented.



\---



## 15. Appropriate Use



RAAHAT AI may be used to:



\- Identify potentially relevant emotional signals

\- Support human reviewers

\- Assist prioritization workflows

\- Provide structured AI indicators

\- Demonstrate an AI-assisted support workflow



The output should be considered one input among other information available to a trained human reviewer.



\---



## 16. Inappropriate Use



RAAHAT AI must not be used as the sole basis for:



\- Medical diagnosis

\- Psychological diagnosis

\- Trauma confirmation

\- Legal conclusions

\- Criminal guilt determination

\- Automatic rejection of a complaint

\- Automatic denial of support

\- Automatic emergency decisions

\- Final decisions about a person's wellbeing



The AI output must not replace appropriate human assessment or emergency procedures.



\---



## 17. Safety Principle



The core safety principle is:



\*\*AI supports human decision-making; AI does not replace human judgment.\*\*



The system should remain conservative about interpreting its own output.



A risk category represents an AI-generated vulnerability indicator, not a definitive statement about the person.



\---



## 18. Input Validation



The AI service validates incoming input before inference.



The current implementation handles invalid or empty text through controlled validation errors.



The inference pipeline also verifies that the expected model and preprocessing artifacts are available.



This reduces the possibility of silently producing an invalid prediction.



\---



## 19. Deterministic Inference



Repeated inference on the same valid input is expected to produce consistent output under the same model and preprocessing artifacts.



This behavior has been tested as part of the AI inference test suite.



The current test suite includes:



\- Distress input

\- Neutral input

\- Positive input

\- Empty input

\- Consistency

\- Whitespace input

\- Short input

\- Long input

\- Special-character input

\- Output structure



All 10 inference tests passed during MVP validation.



\---



## 20. Transparency



The AI service documents:



\- Dataset used

\- Data preparation

\- Feature engineering

\- Model selection

\- Evaluation results

\- Risk mapping

\- Inference pipeline

\- Output contract

\- Limitations

\- Responsible AI considerations



This documentation is intended to make the AI component easier to understand, review, test, and hand over to the backend team.



\---



## 21. Model and Preprocessing Versioning



The AI component uses versioned model and preprocessing artifacts.



The current MVP identifies the selected model as:



`RAAHAT-SVM-MVP-1.0`



The current TF-IDF preprocessing/feature pipeline is identified as:



`RAAHAT-TFIDF-MVP-1.0`



The model and preprocessing artifacts must remain compatible.



If the model or preprocessing pipeline changes, the corresponding version information should also be updated.



\---



## 22. Monitoring and Future Validation



Before production deployment, the AI system should be evaluated using representative domain-specific data.



Future validation should consider:



\- Hindi performance

\- English performance

\- Hinglish performance

\- Class-wise performance

\- False positives

\- False negatives

\- Dataset shift

\- Fairness

\- Calibration

\- Robustness

\- Human-review outcomes



Model performance should be monitored after deployment rather than assumed to remain constant.



\---



## 23. Future Improvements



Potential future improvements include:



\- Domain-specific stress and trauma datasets

\- Better Hindi and Hinglish evaluation

\- Multilingual transformer models

\- Appropriate probability calibration

\- More robust contextual understanding

\- Human-in-the-loop evaluation

\- Fairness testing

\- Dataset expansion

\- Model monitoring

\- Drift detection

\- Better domain-specific risk validation



Advanced approaches should only be introduced after the current baseline is properly validated.



\---



## 24. Current MVP Safety Status



The current RAAHAT AI MVP follows these safety principles:



\- Non-clinical output

\- No diagnostic claim

\- Human review always required

\- Risk mapping is explicitly documented

\- SVI boundaries are identified as initial MVP values

\- Model signal strengths are not treated as probabilities

\- Dataset limitations are documented

\- False positives and false negatives are acknowledged

\- Language limitations are documented

\- Privacy considerations are identified

\- AI output is intended for decision support, not autonomous decisions



\---



## 25. Final Statement



RAAHAT AI is a prototype AI decision-support component designed to identify potential stress and distress-related emotional signals from user-provided text.



Its output should be interpreted as an indicator that can support human review.



It must not be presented as a clinical, psychological, or trauma diagnosis.



Further domain-specific data, validation, expert review, fairness evaluation, privacy controls, and operational testing are required before the system can be considered suitable for real-world deployment.


