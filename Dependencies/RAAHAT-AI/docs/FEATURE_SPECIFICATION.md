# RAAHAT AI - Feature Specification



## 1. Purpose



This document defines the features used by the RAAHAT AI stress and distress vulnerability assessment module.



The current MVP uses text-based Natural Language Processing (NLP) features generated from user-provided text.



The feature specification is based on the implemented preprocessing and TF-IDF feature engineering pipeline.



---



## 2. Current Feature Pipeline



The current feature pipeline is:



User Text

&#x20;   ->

Text Preprocessing

&#x20;   ->

TF-IDF Vectorization

&#x20;   ->

Unigram and Bigram Features

&#x20;   ->

One-vs-Rest Linear Support Vector Machine

&#x20;   ->

Emotion Signal Outputs

&#x20;   ->

Stress/Distress Signal Mapping

&#x20;   ->

Stress Vulnerability Index (SVI)



---



## 3. Primary Input Feature



| Feature | Meaning | Type | Source | Transformation | Reason | Status |

|---|---|---|---|---|---|---|

| text | User-provided textual statement describing the person's situation, feelings, or experience | String/Text | User input | Strip leading/trailing spaces and normalize repeated whitespace | Provides the language signal required for emotion-related prediction | Included |



---



## 4. Text Preprocessing



The current preprocessing performs lightweight normalization.



### Operations



1\. Convert the input into string representation when required.

2\. Remove leading and trailing whitespace.

3\. Replace repeated whitespace characters with a single space.

4\. Preserve the semantic content of the original text.



The preprocessing module does not intentionally remove emotional words because these words can contain important information for emotion prediction.



---



## 5. TF-IDF Features



The current model uses Term Frequency-Inverse Document Frequency (TF-IDF) vectorization.



Configuration:



| Parameter | Current Value |

|---|---|

| lowercase | True |

| ngram\_range | (1, 2) |

| min\_df | 2 |

| max\_features | 10,000 |



The resulting feature representation contains up to 10,000 vocabulary features.



---



## 6. Feature Types



### 6.1 Unigram Features



Unigrams represent individual words.



Examples:



- scared

- confused

- angry

- worried

- sad



These features allow the model to learn associations between individual words and emotion labels.



### 6.2 Bigram Features



Bigrams represent two-word sequences.



Examples:



- very scared

- feeling helpless

- extremely worried

- can't sleep



Bigrams provide limited local context that individual words may not capture.



---



## 7. Feature Representation



Each input text is converted into a sparse numerical TF-IDF vector.



The current training feature matrix contains:



- Training samples: 43,412

- Maximum vocabulary features: 10,000

- Representation: Sparse matrix



The same fitted TF-IDF vectorizer must be used during inference.



A new vectorizer must not be fitted separately on validation, test, or production input.



---



## 8. Feature Source



The current feature source is text.



No demographic, medical, physiological, financial, or other sensitive personal attributes are required by the current MVP model.



The current MVP therefore focuses on linguistic signals from the supplied text.



---



## 9. Feature Inclusion Rationale



Text-based TF-IDF features are included because:



1\. The MVP is text-first.

2\. They can be generated directly from user input.

3\. They provide a simple and reproducible baseline representation.

4\. They work with the selected Linear SVM model.

5\. They are computationally lightweight compared with large transformer-based models.

6\. They are suitable for an initial hackathon MVP.



---



## 10. Features Not Currently Used



The following features are not currently part of the implemented MVP model:



- Age

- Gender

- Location

- Caste

- Religion

- Medical history

- Mental health diagnosis

- Income

- Education

- Physiological signals

- Heart rate

- Facial expression

- Camera-based emotion features

- Manually assigned clinical scores



These features are excluded because they are not required by the current text-based MVP and may introduce unnecessary privacy, fairness, or data-governance concerns.



---



## 11. Feature Leakage Prevention



The TF-IDF vocabulary and feature weights are fitted using the training data only.



Validation and test data are transformed using the already-fitted training vectorizer.



Production inference uses the saved training vectorizer.



This prevents information from validation or test data from being used to construct the training representation.



---



## 12. Feature Consistency



The same preprocessing and TF-IDF configuration must be used during:



- Model training

- Validation

- Testing

- Standalone inference

- FastAPI prediction requests



A mismatch between the training vectorizer and inference vectorizer can produce incompatible feature representations.



---



## 13. Feature Versioning



The feature specification should be versioned together with the model and preprocessing configuration.



Current conceptual version:



- Feature specification: v1

- TF-IDF configuration: v1

- Model: Linear SVM

- Feature representation: TF-IDF unigram + bigram



Future changes to feature extraction should create a new feature version and require re-evaluation of the model.



---



## 14. Limitations



TF-IDF features represent text statistically and do not provide full semantic understanding.



The current feature representation may have difficulty with:



- Very short text

- Sarcasm

- Ambiguous language

- Unseen vocabulary

- Code-switching

- Complex trauma descriptions

- Context that requires information outside the supplied text



The model output must therefore be treated as a support/risk indicator rather than a clinical diagnosis.



---



## 15. Current Feature Specification Status



Status: IMPLEMENTED FOR MVP



The current feature pipeline is:



Text

-> Preprocessing

-> TF-IDF

-> Unigram + Bigram Features

-> Linear SVM

-> Emotion Signals

-> SVI Risk Mapping



This specification should be updated whenever the implemented feature pipeline changes.


