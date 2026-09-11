\# RAAHAT AI - FastAPI Integration Interface



\## 1. Purpose



This document defines the interface between the RAAHAT AI inference module and the FastAPI service.



The FastAPI service will receive user text, call the AI inference pipeline, and return a structured JSON response.



\## 2. Endpoint



Method:



POST



Endpoint:



/predict



\## 3. Input



Example request:



{

&#x20; "text": "I am scared and confused about what happened."

}



The `text` field is required and must contain non-empty text.



\## 4. Output



Example response:



{

&#x20; "predicted\_emotions": \[

&#x20;   "fear",

&#x20;   "confusion"

&#x20; ],

&#x20; "emotion\_signal\_strengths": {

&#x20;   "fear": 0.31,

&#x20;   "confusion": 0.54

&#x20; },

&#x20; "svi\_score": 30.46,

&#x20; "risk\_category": "Moderate",

&#x20; "signal\_groups": {

&#x20;   "fear\_threat": 0.31,

&#x20;   "sadness\_loss": 0.21,

&#x20;   "anger\_frustration": 0.17,

&#x20;   "confusion\_uncertainty": 0.54

&#x20; },

&#x20; "human\_review\_required": true,

&#x20; "diagnostic": false

}



\## 5. Validation



The service must reject:



\- Empty text

\- Missing text field

\- Invalid request format



\## 6. Error Handling



Invalid input should return an appropriate validation error.



The AI service must not return a medical or psychiatric diagnosis.



\## 7. AI Responsibility



The AI module is responsible for:



1\. Text preprocessing

2\. TF-IDF feature extraction

3\. Model inference

4\. Emotion signal generation

5\. SVI calculation

6\. Risk category mapping

7\. Structured output generation



\## 8. Backend Responsibility



The FastAPI/backend integration is responsible for:



1\. Receiving API requests

2\. Validating input

3\. Calling the AI inference function

4\. Returning the structured response

5\. Handling API errors

6\. Connecting the AI response with the application workflow



\## 9. Important Safety Rule



The AI output is a non-clinical support and prioritization indicator.



It must not be presented as a medical, psychiatric, or trauma diagnosis.



Human review is required for decisions involving victim or complainant support.

