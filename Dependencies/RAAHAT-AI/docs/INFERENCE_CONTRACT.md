\# RAAHAT AI - Inference Contract



\## 1. Purpose



This document defines the input, processing flow, output structure, validation rules, and integration requirements for the RAAHAT AI inference module.



The inference module converts a victim or complainant's text into emotion-related language signals and an explainable Stress Vulnerability Index (SVI).



The output is intended to support human review and support prioritization.



The system is NOT a medical, psychiatric, psychological, or clinical diagnostic system.



\---



\## 2. AI Module



\*\*Module Name:\*\*  

Stress, Trauma \& Distress Prediction



\*\*Primary Responsibility:\*\*  

Analyze text provided by a victim or complainant and generate a non-clinical stress/distress vulnerability indicator.



\---



\## 3. Input



The current MVP accepts:



\- Written text

\- English text for the currently validated model



Future versions may support:



\- Hindi

\- Hinglish

\- Voice input converted into text using Automatic Speech Recognition (ASR)



\### Example Input



```text

I am very scared and confused about what happened.

I don't know what to do.

