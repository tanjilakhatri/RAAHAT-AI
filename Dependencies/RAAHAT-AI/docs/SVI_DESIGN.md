\# RAAHAT Stress Vulnerability Index (SVI) Design



\## 1. Purpose



The Stress Vulnerability Index (SVI) is an explainable,

non-clinical indicator designed to summarize language-level

signals that may be associated with stress or distress.



The SVI is intended to support human review and support

prioritization.



It must not be used as a medical, psychiatric, or trauma diagnosis.



\---



\## 2. SVI Score



The MVP will use a normalized score from 0 to 100.



\- 0 = very low observed distress-related language signal

\- 100 = very high observed distress-related language signal



The score represents the strength of the detected language signals,

not the severity of a person's actual mental-health condition.



\---



\## 3. Signal Groups



The SVI considers the following groups:



\### Fear / Threat



Signals:



\- fear

\- nervousness



These may indicate fear, threat-related language, or nervousness.



\### Sadness / Loss



Signals:



\- sadness

\- grief

\- disappointment

\- remorse



These may indicate negative emotional experiences such as sadness,

loss, regret, or emotional pain.



\### Anger / Frustration



Signals:



\- anger

\- annoyance

\- disapproval

\- disgust



These may indicate anger, frustration, or negative reactions.



\### Confusion / Uncertainty



Signals:



\- confusion

\- realization



These may provide additional contextual information about uncertainty

or difficulty understanding a situation.



\---



\## 4. Contextual Signals



Positive and neutral emotions are retained as contextual information.



Examples include:



\- joy

\- gratitude

\- love

\- optimism

\- relief

\- caring

\- admiration

\- approval

\- amusement

\- excitement

\- pride

\- curiosity

\- desire

\- neutral



These signals should not be interpreted as proof that a person has

no distress.



\---



\## 5. SVI Interpretation



The SVI should be interpreted as a language-based vulnerability

indicator.



Suggested interpretation:



| SVI Range | Category | Meaning |

|---|---|---|

| 0–24 | Low | Low observed distress-related language signal |

| 25–49 | Moderate | Some observed distress-related language signals |

| 50–74 | High | Strong observed distress-related language signals |

| 75–100 | Very High | Very strong observed distress-related language signals |



These ranges are initial MVP design boundaries and require validation

with appropriate domain experts and representative data before being

treated as operational thresholds.



\---



\## 6. Human Review



The SVI must not independently determine the final action.



The system should provide the indicator to a trained human reviewer,

who can consider:



\- the original statement

\- detected signals

\- contextual information

\- the circumstances reported by the person

\- other available evidence



Human review remains necessary before support or prioritization

decisions are made.



\---



\## 7. Explainability



The AI response should identify the major detected signal groups.



Example:



\- Fear / Threat: detected

\- Sadness / Loss: detected

\- Anger / Frustration: low

\- Confusion / Uncertainty: detected



This allows the reviewer to understand why the AI generated its

indicator.



\---



\## 8. Important Limitation



The current GoEmotions-based model learns general emotional language.



It is not a clinically validated stress or trauma detection model.



Therefore:



\- SVI must not be called a diagnosis.

\- SVI must not claim to measure clinical trauma.

\- SVI must not replace professional assessment.

\- SVI should be used only as a support and prioritization signal.



\---



\## 9. Future Validation



Before real-world deployment, the SVI should be evaluated using

appropriate domain-specific and representative data.



Future validation should examine:



\- class balance

\- false positives

\- false negatives

\- subgroup performance

\- language differences

\- robustness

\- domain-expert review

\- threshold calibration



\---



\## 10. AI Pipeline



The planned RAAHAT AI pipeline is:



Text Input

→ Preprocessing

→ TF-IDF Feature Extraction

→ Selected ML Model

→ Emotion Predictions

→ Stress/Distress Signal Groups

→ SVI Calculation

→ Risk Category

→ Explainable Structured Output

→ Human Review# RAAHAT Stress Vulnerability Index (SVI) Design



\## 1. Purpose



The Stress Vulnerability Index (SVI) is an explainable,

non-clinical indicator designed to summarize language-level

signals that may be associated with stress or distress.



The SVI is intended to support human review and support

prioritization.



It must not be used as a medical, psychiatric, or trauma diagnosis.



\---



\## 2. SVI Score



The MVP will use a normalized score from 0 to 100.



\- 0 = very low observed distress-related language signal

\- 100 = very high observed distress-related language signal



The score represents the strength of the detected language signals,

not the severity of a person's actual mental-health condition.



\---



\## 3. Signal Groups



The SVI considers the following groups:



\### Fear / Threat



Signals:



\- fear

\- nervousness



These may indicate fear, threat-related language, or nervousness.



\### Sadness / Loss



Signals:



\- sadness

\- grief

\- disappointment

\- remorse



These may indicate negative emotional experiences such as sadness,

loss, regret, or emotional pain.



\### Anger / Frustration



Signals:



\- anger

\- annoyance

\- disapproval

\- disgust



These may indicate anger, frustration, or negative reactions.



\### Confusion / Uncertainty



Signals:



\- confusion

\- realization



These may provide additional contextual information about uncertainty

or difficulty understanding a situation.



\---



\## 4. Contextual Signals



Positive and neutral emotions are retained as contextual information.



Examples include:



\- joy

\- gratitude

\- love

\- optimism

\- relief

\- caring

\- admiration

\- approval

\- amusement

\- excitement

\- pride

\- curiosity

\- desire

\- neutral



These signals should not be interpreted as proof that a person has

no distress.



\---



\## 5. SVI Interpretation



The SVI should be interpreted as a language-based vulnerability

indicator.



Suggested interpretation:



| SVI Range | Category | Meaning |

|---|---|---|

| 0–24 | Low | Low observed distress-related language signal |

| 25–49 | Moderate | Some observed distress-related language signals |

| 50–74 | High | Strong observed distress-related language signals |

| 75–100 | Very High | Very strong observed distress-related language signals |



These ranges are initial MVP design boundaries and require validation

with appropriate domain experts and representative data before being

treated as operational thresholds.



\---



\## 6. Human Review



The SVI must not independently determine the final action.



The system should provide the indicator to a trained human reviewer,

who can consider:



\- the original statement

\- detected signals

\- contextual information

\- the circumstances reported by the person

\- other available evidence



Human review remains necessary before support or prioritization

decisions are made.



\---



\## 7. Explainability



The AI response should identify the major detected signal groups.



Example:



\- Fear / Threat: detected

\- Sadness / Loss: detected

\- Anger / Frustration: low

\- Confusion / Uncertainty: detected



This allows the reviewer to understand why the AI generated its

indicator.



\---



\## 8. Important Limitation



The current GoEmotions-based model learns general emotional language.



It is not a clinically validated stress or trauma detection model.



Therefore:



\- SVI must not be called a diagnosis.

\- SVI must not claim to measure clinical trauma.

\- SVI must not replace professional assessment.

\- SVI should be used only as a support and prioritization signal.



\---



\## 9. Future Validation



Before real-world deployment, the SVI should be evaluated using

appropriate domain-specific and representative data.



Future validation should examine:



\- class balance

\- false positives

\- false negatives

\- subgroup performance

\- language differences

\- robustness

\- domain-expert review

\- threshold calibration



\---



\## 10. AI Pipeline



The planned RAAHAT AI pipeline is:



Text Input

→ Preprocessing

→ TF-IDF Feature Extraction

→ Selected ML Model

→ Emotion Predictions

→ Stress/Distress Signal Groups

→ SVI Calculation

→ Risk Category

→ Explainable Structured Output

→ Human Review

