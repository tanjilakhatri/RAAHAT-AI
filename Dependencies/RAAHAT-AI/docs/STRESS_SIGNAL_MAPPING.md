\# RAAHAT Stress/Distress Signal Mapping



\## 1. Purpose



The RAAHAT AI module uses emotion predictions as language-level signals

that may help identify possible stress or distress in a victim or

complainant's response.



These signals are not medical diagnoses and must not be interpreted

as proof of trauma, psychiatric illness, or clinical stress.



The purpose is to support human review and support prioritization.



\---



\## 2. Relevant Signal Groups



\### 2.1 Fear / Threat Signal



Relevant emotion classes:



\- fear

\- nervousness



Interpretation:



These emotions may indicate that the text contains language associated

with fear, threat, worry, or nervousness.



They may be relevant when identifying possible distress-related language.



\---



\### 2.2 Sadness / Loss Signal



Relevant emotion classes:



\- sadness

\- grief

\- disappointment

\- remorse



Interpretation:



These emotions may indicate sadness, loss, emotional pain, regret,

or negative emotional experience.



They can contribute to a broader distress signal but should not

independently determine risk.



\---



\### 2.3 Anger / Frustration Signal



Relevant emotion classes:



\- anger

\- annoyance

\- disapproval

\- disgust



Interpretation:



These emotions may indicate anger, frustration, dissatisfaction,

or negative reaction.



They are contextual signals and are not direct indicators of trauma.



\---



\### 2.4 Confusion / Uncertainty Signal



Relevant emotion classes:



\- confusion

\- realization



Interpretation:



These signals may indicate uncertainty, difficulty understanding

a situation, or a change in understanding.



They may provide additional context during human review.



\---



\### 2.5 Positive / Protective Context



Relevant emotion classes:



\- joy

\- gratitude

\- love

\- optimism

\- amusement

\- excitement

\- relief

\- caring

\- admiration

\- approval

\- pride

\- desire

\- curiosity



Interpretation:



These emotions provide contextual information and help prevent the

system from treating every emotional response as distress.



They should not automatically be interpreted as evidence that a

person is safe or has no distress.



\---



\## 3. Important Design Principle



No individual emotion class should independently determine the final

RAAHAT risk category.



The system should combine multiple signals and contextual information

before producing an SVI.



\---



\## 4. Responsible AI Limitation



The GoEmotions dataset represents general emotional language and is

not a clinically validated trauma or stress dataset.



Therefore, the RAAHAT system must describe its output as a

stress/distress vulnerability indicator rather than a diagnosis.



Final decisions should remain with trained human reviewers.



\---



\## 5. Next Step



The next stage is to define the Stress Vulnerability Index (SVI)

using these signal groups.



The SVI design should specify:



\- signal contribution

\- score range

\- risk categories

\- interpretation

\- limitations

\- explainability information

