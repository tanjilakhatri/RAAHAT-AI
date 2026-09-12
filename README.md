# RAAHAT-AI

## AI-Based Stress, Trauma & Distress Vulnerability Assessment

**Smart India Hackathon 2026 | Problem Statement: SIH 26093**

RAAHAT-AI is an Artificial Intelligence and Machine Learning based system designed to assist in identifying emotional signals related to stress, trauma, distress and vulnerability from user-provided assessment text.

The main purpose of the project is to provide an AI-assisted indication that can support human decision-making. The system is designed as a support tool and is **not intended to replace psychologists, counsellors, doctors, emergency services or other qualified professionals**.

The project focuses on building a practical AI/ML pipeline that starts from emotional-text data preparation and continues through preprocessing, feature engineering, machine learning, evaluation, inference and backend integration.

---

# RAAHAT-AI

## AI-Based Stress, Trauma & Distress Vulnerability Assessment

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-499848?logo=gunicorn&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Project-Active-success)
![SIH 2026](https://img.shields.io/badge/Smart%20India%20Hackathon-2026-orange)

![Data Processing](https://img.shields.io/badge/Data%20Processing-Completed-success)
![ML Pipeline](https://img.shields.io/badge/ML%20Pipeline-Implemented-success)
![Inference](https://img.shields.io/badge/Inference-Implemented-success)
![API](https://img.shields.io/badge/API-FastAPI-success)
![Documentation](https://img.shields.io/badge/Documentation-Complete-blue)

**Smart India Hackathon 2026 | Problem Statement: SIH 26093**
**Smart India Hackathon 2026 | Problem Statement: SIH 26093**

RAAHAT-AI is an Artificial Intelligence and Machine Learning based system
designed to assist in identifying emotional signals related to stress,
trauma, distress and vulnerability from user-provided assessment text.

The system is designed as an AI-assisted support component and is
**not intended to replace psychologists, counsellors, doctors, emergency
services or other qualified professionals.**

# Table of Contents

1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Why RAAHAT-AI Is Required](#3-why-raahatai-is-required)
4. [Proposed Solution](#4-proposed-solution)
5. [Project Objectives](#5-project-objectives)
6. [Key Features](#6-key-features)
7. [Complete System Workflow](#7-complete-system-workflow)
8. [System Architecture](#8-system-architecture)
9. [AI/ML Pipeline](#9-aiml-pipeline)
10. [Role of AI/ML in RAAHAT-AI](#10-role-of-aiml-in-raahatai)
11. [My Role as Member 2](#11-my-role-as-member-2)
12. [Dataset](#12-dataset)
13. [Dataset Preparation](#13-dataset-preparation)
14. [Data Quality Analysis](#14-data-quality-analysis)
15. [Duplicate Analysis](#15-duplicate-analysis)
16. [Text Normalization and Text Grouping](#16-text-normalization-and-text-grouping)
17. [Data Leakage Prevention](#17-data-leakage-prevention)
18. [Train, Validation and Test Split](#18-train-validation-and-test-split)
19. [Feature Engineering](#19-feature-engineering)
20. [Machine Learning](#20-machine-learning)
21. [Model Training](#21-model-training)
22. [Model Validation and Evaluation](#22-model-validation-and-evaluation)
23. [Risk and Vulnerability Indication](#23-risk-and-vulnerability-indication)
24. [Standalone Inference](#24-standalone-inference)
25. [FastAPI Backend](#25-fastapi-backend)
26. [API Endpoints](#26-api-endpoints)
27. [API Request](#27-api-request)
28. [API Response](#28-api-response)
29. [API Error Handling](#29-api-error-handling)
30. [Testing](#30-testing)
31. [Screenshot Documentation](#31-screenshot-documentation)
32. [Project Structure](#32-project-structure)
33. [Technology Stack](#33-technology-stack)
34. [Why These Technologies Were Used](#34-why-these-technologies-were-used)
35. [Installation and Setup](#35-installation-and-setup)
36. [Running the Project](#36-running-the-project)
37. [Running the FastAPI Service](#37-running-the-fastapi-service)
38. [Complete Implementation Process](#38-complete-implementation-process)
39. [Challenges and Solutions](#39-challenges-and-solutions)
40. [Important Engineering Decisions](#40-important-engineering-decisions)
41. [Responsible AI](#41-responsible-ai)
42. [Privacy and Data Safety](#42-privacy-and-data-safety)
43. [Limitations](#43-limitations)
44. [Future Scope](#44-future-scope)
45. [Current Project Status](#45-current-project-status)
46. [Definition of Done](#46-definition-of-done)
47. [Learning Outcomes](#47-learning-outcomes)
48. [Team Contribution](#48-team-contribution)
49. [Conclusion](#49-conclusion)
50. [Disclaimer](#50-disclaimer)

---

# 1. Project Overview

RAAHAT-AI is the Artificial Intelligence and Machine Learning component of the RAAHAT project developed for Smart India Hackathon 2026.

The system focuses on processing textual assessment input and identifying emotional patterns that may indicate stress, distress, trauma-related signals or vulnerability.

Instead of treating the AI output as a final medical or psychological decision, RAAHAT-AI is designed to act as an assistance layer.

The overall idea is:

```text
User Assessment
       |
       v
Input Validation
       |
       v
Text Preprocessing
       |
       v
Feature Extraction
       |
       v
Machine Learning Model
       |
       v
Prediction
       |
       v
Risk / Vulnerability Indication
       |
       v
Backend API
       |
       v
Human Review / Support
