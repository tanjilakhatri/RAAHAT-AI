\# RAAHAT AI - Preprocessing Documentation



\## 1. Purpose



This document describes the text preprocessing pipeline used by the RAAHAT AI emotion and stress/distress vulnerability assessment MVP.



The preprocessing pipeline converts raw user text into a consistent format before feature extraction and model inference.



The same preprocessing logic is used during model development and standalone inference.



\---



\## 2. Preprocessing Pipeline



The current preprocessing flow is:



Raw Text

&#x20;   |

&#x20;   v

Text Validation

&#x20;   |

&#x20;   v

Whitespace Normalization

&#x20;   |

&#x20;   v

Clean Processed Text

&#x20;   |

&#x20;   v

TF-IDF Feature Extraction

&#x20;   |

&#x20;   v

Machine Learning Model



The preprocessing stage is intentionally lightweight because the current MVP uses TF-IDF with a Linear Support Vector Machine.



\---



\## 3. Input Data



The primary input is:



text



Data type:



String



Example:



I am scared and confused about what happened.



The text is received from the user and passed to the preprocessing module before feature extraction.



\---



\## 4. Text Normalization



The current preprocessing module performs basic text normalization.



The implemented preprocessing function:



1\. Handles None input.

2\. Converts the input to a string.

3\. Removes unnecessary leading and trailing whitespace.

4\. Replaces repeated whitespace characters with a single space.



This produces a consistent text representation for downstream processing.



\---



\## 5. Handling None Input



If the preprocessing function receives a None value, it returns an empty string.



Example:



Input:



None



Output:



""



This prevents the preprocessing function from failing because of a None value.



However, the standalone inference service separately validates user input and rejects empty text instead of generating a prediction.



\---



\## 6. Whitespace Normalization



Repeated whitespace is replaced with a single space.



Example:



Input:



I    am   scared    about   what happened.



Processed text:



I am scared about what happened.



This reduces unnecessary variation caused by spaces, tabs, or line breaks.



\---



\## 7. Leading and Trailing Whitespace



Leading and trailing whitespace is removed.



Example:



Input:



&#x20;   I am scared.



Processed text:



I am scared.



This ensures that unnecessary spaces do not affect the text representation.



\---



\## 8. Preprocessing Implementation



The preprocessing module is located at:



src/preprocessing.py



The main functions are:



normalize\_text()



preprocess\_text()



The preprocessing module is intentionally separated from model training so that the same logic can be reused during standalone inference.



\---



\## 9. Current Preprocessing Code



The implemented preprocessing logic is:



import re



def normalize\_text(text: str) -> str:

&#x20;   if text is None:

&#x20;       return ""



&#x20;   text = str(text).strip()

&#x20;   text = re.sub(r"\\s+", " ", text)



&#x20;   return text





def preprocess\_text(text: str) -> str:

&#x20;   return normalize\_text(text)



\---



\## 10. Training Data Preprocessing



The training dataset was passed through the preprocessing function before TF-IDF feature extraction.



Training dataset size:



43,412 rows



The preprocessing validation showed:



\- Original null values: 0

\- Processed null values: 0

\- Changed text rows: 2,700



The changed rows mainly represent normalization of whitespace or surrounding formatting.



\---



\## 11. Validation Data Preprocessing



The validation dataset uses the same preprocessing logic as the training dataset.



The validation text is processed using the same preprocessing function before applying the already-fitted TF-IDF vectorizer.



The validation dataset is not used to fit the preprocessing or TF-IDF vocabulary.



\---



\## 12. Test Data Preprocessing



The test dataset follows the same preprocessing pipeline.



Test text is processed using the same preprocessing function and transformed using the training-fitted TF-IDF vectorizer.



This maintains consistency between training and evaluation.



\---



\## 13. TF-IDF Feature Extraction



After preprocessing, text is converted into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF).



The implementation uses:



TfidfVectorizer



Configuration:



\- lowercase = True

\- ngram\_range = (1, 2)

\- min\_df = 2

\- max\_features = 10,000



The vectorizer considers both:



\- Unigrams: individual words

\- Bigrams: two-word combinations



\---



\## 14. TF-IDF Training Process



The TF-IDF vectorizer is fitted only on the training text.



The training process is:



Training Text

&#x20;   |

&#x20;   v

Preprocessing

&#x20;   |

&#x20;   v

TF-IDF Vectorizer Fit

&#x20;   |

&#x20;   v

TF-IDF Training Matrix

&#x20;   |

&#x20;   v

Model Training



The fitted vectorizer is saved as a model artifact for later inference.



\---



\## 15. TF-IDF Feature Transformation



Validation, test, and inference text are transformed using the already-fitted training vectorizer.



The vectorizer is not fitted again on validation, test, or user input.



This prevents information leakage.



\---



\## 16. TF-IDF Feature Statistics



The training TF-IDF transformation produced:



Training rows:



43,412



Feature matrix:



43,412 x 10,000



Vocabulary size:



10,000



The resulting matrix is stored as a sparse matrix because most text-feature values are zero.



\---



\## 17. Leakage Prevention



Data leakage was considered during preprocessing and dataset splitting.



The project uses the following rules:



1\. Dataset splitting is performed before model feature fitting.

2\. Text grouping is used to reduce duplicate-text leakage.

3\. TF-IDF is fitted only on training data.

4\. Validation and test data use the training-fitted vectorizer.

5\. Inference uses the saved training-fitted vectorizer.



These rules ensure that evaluation data does not influence the learned feature vocabulary.



\---



\## 18. Consistency Testing



The preprocessing pipeline was tested using repeated inputs.



The same input should produce the same processed representation.



Consistency testing was successfully completed.



The preprocessing module was also tested using real project data.



\---



\## 19. Inference Preprocessing



The standalone inference pipeline follows:



User Text

&#x20;   |

&#x20;   v

Input Validation

&#x20;   |

&#x20;   v

Preprocessing

&#x20;   |

&#x20;   v

Saved TF-IDF Vectorizer

&#x20;   |

&#x20;   v

SVM Model

&#x20;   |

&#x20;   v

Emotion Signals

&#x20;   |

&#x20;   v

Stress Vulnerability Index



The inference service uses the same preprocessing logic used during model development.



\---



\## 20. Empty Input Handling



Empty input is not sent to the model.



The inference service validates the input before preprocessing.



Example:



Input:



""



Result:



Input text cannot be empty.



This prevents meaningless predictions from being generated for empty input.



\---



\## 21. Invalid Input Handling



The API validates the request structure before running inference.



If the required text field is missing, the API returns a validation error.



If the input cannot be processed correctly, the service returns a controlled error instead of exposing internal model details.



\---



\## 22. Preprocessing and Model Consistency



The preprocessing logic and TF-IDF vectorizer used during inference must remain compatible with the trained model.



The following components must remain aligned:



\- Preprocessing logic

\- TF-IDF configuration

\- Saved TF-IDF vectorizer

\- Saved machine learning model



Changing preprocessing or feature configuration without retraining or updating the model can cause inconsistent predictions.



\---



\## 23. Limitations



The current preprocessing pipeline is intentionally simple.



It does not currently perform:



\- Stemming

\- Lemmatization

\- Stop-word removal

\- Spelling correction

\- Translation

\- Advanced language detection

\- Clinical terminology normalization



These methods were not added because the current MVP focuses on a simple and reproducible text classification pipeline.



Future versions may evaluate additional preprocessing methods using validation evidence before adoption.



\---



\## 24. Responsible AI Consideration



Preprocessing does not determine whether a person has a psychological or medical condition.



The pipeline only prepares text for an emotion-signal model.



The resulting RAAHAT output is a non-clinical decision-support indicator.



It must not be presented as a medical or psychological diagnosis.



Human review remains required for the current MVP.



\---



\## 25. Current Status



Status: COMPLETED FOR MVP



The preprocessing pipeline has been:



\- Implemented

\- Tested with sample text

\- Tested with real project data

\- Tested for consistency

\- Integrated with TF-IDF feature extraction

\- Used during model training

\- Reused during standalone inference

\- Validated for empty-input handling

\- Documented for backend integration



The current preprocessing pipeline is considered stable for the RAAHAT AI MVP.

