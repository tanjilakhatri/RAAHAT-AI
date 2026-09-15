# RAAHAT AI Specification

## 1\. AI Module

Stress, Trauma \& Distress Prediction

## 2\. Objective

The objective of the AI module is to analyze text provided by a victim or complainant and generate a non-clinical stress/distress vulnerability indicator.

The output is intended to support human review and prioritization of support.

## 3\. Input

The primary input for the MVP is written text provided by the victim or complainant.

Voice input may be converted into text using an Automatic Speech Recognition system before being processed by the AI module.

## 4\. Output

The AI module will generate:

* Stress/distress prediction
* Emotion signal strengths
* Stress Vulnerability Index (SVI)
* Risk category
* Support priority indicator

## 5\. AI Approach

The project will use supervised machine learning for text classification.

Different suitable models will be evaluated using appropriate classification metrics before selecting the final model.

## 6\. MVP Languages

* Hindi
* English
* Hinglish

## 7\. Important Limitation

The AI system is a support and risk-indication tool.

It is not a medical or psychiatric diagnostic system and must not be used as a replacement for trained human assessment.

## 8\. Human-in-the-Loop

AI predictions should support human review rather than independently determining the final action or decision.

## 9\. Expected Pipeline

Text Input
→ Preprocessing
→ Feature Extraction
→ ML Model
→ Prediction
→ SVI Mapping
→ Risk Category
→ Structured Output

