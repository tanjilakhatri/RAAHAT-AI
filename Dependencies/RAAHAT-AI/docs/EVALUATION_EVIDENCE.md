\# RAAHAT AI - Evaluation Evidence



\## 1. Purpose



This document records the evaluation evidence for the RAAHAT AI emotion classification and stress/distress vulnerability assessment MVP.



The evaluation compares the Logistic Regression baseline with the selected Linear Support Vector Machine model.



The evaluation focuses on Precision, Recall, F1-score, Macro F1, Hamming Loss, class-wise performance, and error analysis.



\---



\## 2. Evaluation Dataset



The models were evaluated using the validation split created from the project consensus dataset.



The project uses a leakage-safe split so that normalized duplicate text groups are not distributed across different dataset splits.



Validation data was not used for model training.



\---



\## 3. Models Evaluated



Two models were evaluated:



1\. Logistic Regression baseline

2\. Linear Support Vector Machine



Both models use:



\- Text preprocessing

\- TF-IDF feature extraction

\- Unigram and bigram features

\- Multi-label classification using OneVsRestClassifier



\---



\## 4. Baseline Model



The baseline model uses:



Logistic Regression



Configuration:



\- OneVsRestClassifier

\- LogisticRegression

\- max\_iter = 1000

\- solver = liblinear



The baseline was established before selecting the final model.



\---



\## 5. Selected Model



The selected model is:



Linear Support Vector Machine



Implementation:



LinearSVC



Multi-label strategy:



OneVsRestClassifier



The selected SVM model is stored as:



models/svm\_model.pkl



The corresponding TF-IDF vectorizer is:



models/svm\_tfidf\_vectorizer.pkl



\---



\## 6. Model Comparison



The saved model comparison produced the following results:



| Metric | Logistic Regression | Linear SVM |

|---|---:|---:|

| Micro Precision | 0.7109 | 0.6485 |

| Micro Recall | 0.2672 | 0.3698 |

| Micro F1 | 0.3884 | 0.4710 |

| Macro F1 | 0.2070 | 0.3332 |

| Hamming Loss | 0.0354 | 0.0349 |



The complete comparison is stored in:



outputs/model\_comparison.csv



\---



\## 7. Micro Precision



Logistic Regression:



0.7109



Linear SVM:



0.6485



Logistic Regression produced higher Micro Precision.



This means that, among the labels predicted by the model, the Logistic Regression baseline had fewer false-positive predictions relative to the SVM.



\---



\## 8. Micro Recall



Logistic Regression:



0.2672



Linear SVM:



0.3698



Linear SVM produced higher Micro Recall.



This indicates that the SVM recovered more of the relevant emotion labels in the validation data.



Recall is important for the current project because missing relevant emotional signals can reduce the usefulness of a downstream vulnerability indicator.



\---



\## 9. Micro F1-score



Logistic Regression:



0.3884



Linear SVM:



0.4710



Linear SVM produced the stronger Micro F1-score.



F1-score provides a balance between Precision and Recall.



The higher SVM Micro F1 indicates a better overall balance between these two measures on the validation data.



\---



\## 10. Macro F1-score



Logistic Regression:



0.2070



Linear SVM:



0.3332



Linear SVM produced the higher Macro F1-score.



Macro F1 gives equal importance to individual classes rather than allowing frequent classes to dominate the overall score.



This result supports the use of SVM for the current MVP because the model showed stronger overall class-level performance.



\---



\## 11. Hamming Loss



Logistic Regression:



0.0354



Linear SVM:



0.0349



Lower Hamming Loss is better.



The Linear SVM produced a slightly lower Hamming Loss than Logistic Regression.



This indicates that the SVM produced fewer individual label prediction errors according to this metric.



\---



\## 12. Model Selection Decision



The Linear SVM was selected for the current MVP.



The decision was not based on a single metric.



The SVM showed:



\- Higher Micro Recall

\- Higher Micro F1

\- Higher Macro F1

\- Lower Hamming Loss



Logistic Regression showed higher Micro Precision.



Because the RAAHAT MVP requires useful recall of relevant emotion signals while maintaining reasonable overall classification performance, the SVM was selected as the current model.



\---



\## 13. Class-wise Evaluation



Class-wise metrics were generated separately for the models.



The saved evaluation files are:



outputs/baseline\_classwise\_metrics.csv



outputs/svm\_classwise\_metrics.csv



These files contain class-level evaluation results and are used to identify stronger and weaker emotion classes.



Class-wise evaluation is important because the overall metrics can hide poor performance on less frequent classes.



\---



\## 14. Class Imbalance Consideration



The emotion dataset contains classes with different frequencies.



Therefore, accuracy alone is not considered sufficient for model selection.



The evaluation considers:



\- Precision

\- Recall

\- F1-score

\- Macro F1

\- Hamming Loss

\- Class-wise performance

\- Error analysis



This provides a more useful view of model behavior across multiple emotion categories.



\---



\## 15. Error Analysis



Error analysis was performed for the baseline model.



The saved error analysis file is:



outputs/baseline\_error\_analysis.csv



The analysis was used to identify examples where the baseline model produced incorrect or incomplete emotion predictions.



This helps identify areas where the model may require improvement.



\---



\## 16. Weak Class Analysis



Class-wise performance was reviewed to identify weaker emotion classes.



Low-frequency emotion categories can be more difficult to predict because the model has fewer examples from which to learn.



This is an important limitation when interpreting individual emotion predictions.



The current MVP therefore does not treat every emotion prediction as equally reliable.



\---



\## 17. Evaluation Artifacts



The following evaluation artifacts are currently available:



| Artifact | Purpose |

|---|---|

| outputs/model\_comparison.csv | Model-level comparison |

| outputs/baseline\_classwise\_metrics.csv | Baseline class-wise metrics |

| outputs/svm\_classwise\_metrics.csv | SVM class-wise metrics |

| outputs/baseline\_error\_analysis.csv | Baseline error analysis |



\---



\## 18. Validation Results Summary



The final validation comparison is:



Linear SVM:



Micro Precision = 0.6485



Micro Recall = 0.3698



Micro F1 = 0.4710



Macro F1 = 0.3332



Hamming Loss = 0.0349



Logistic Regression:



Micro Precision = 0.7109



Micro Recall = 0.2672



Micro F1 = 0.3884



Macro F1 = 0.2070



Hamming Loss = 0.0354



\---



\## 19. Interpretation of Results



The results show that the Linear SVM provides better recall and F1-based performance than the Logistic Regression baseline.



However, the results should not be interpreted as clinical performance.



The validation data comes from the GoEmotions-derived dataset, which represents general emotional language.



The results therefore describe model behavior on the project evaluation dataset only.



\---



\## 20. Important Model Limitation



The current model predicts emotion-related signals.



It does not directly predict:



\- Psychological diagnosis

\- Clinical stress

\- Trauma diagnosis

\- Mental illness

\- Medical condition



The Stress Vulnerability Index is a project-defined non-clinical risk indicator derived from selected emotion signal groups.



\---



\## 21. Signal Strength Limitation



The SVM inference pipeline uses decision scores and applies a sigmoid transformation to produce bounded signal-strength values.



These values are not calibrated probabilities.



They must not be described as:



\- Model confidence

\- Probability of an emotion

\- Clinical probability

\- Diagnostic certainty



They are model-derived signal strengths used by the downstream RAAHAT risk-mapping process.



\---



\## 22. Reproducibility



The evaluation can be traced to:



\- Project consensus dataset

\- Leakage-safe dataset split

\- Text preprocessing module

\- TF-IDF feature configuration

\- Model configuration

\- Saved model artifacts

\- Saved evaluation CSV files



The model and preprocessing versions are documented in:



docs/MODEL\_VERSIONING.md



\---



\## 23. Responsible AI Interpretation



The evaluation metrics describe machine learning performance on the available dataset.



They do not prove that the system can accurately assess real-world stress or trauma.



Real-world use would require additional representative data, domain-expert review, appropriate validation, and safety evaluation.



The current system must therefore be treated as a decision-support prototype.



Human review remains required.



\---



\## 24. Future Evaluation Improvements



Future versions should evaluate:



\- More representative complaint/victim language

\- Hindi and Hinglish examples

\- Domain-specific validation data

\- More balanced class coverage

\- Calibration of model scores if required

\- Additional model comparisons

\- Human/domain-expert review

\- Robustness across different language patterns



Any future evaluation should be documented separately and should not replace the current evidence without comparison.



\---



\## 25. Current Status



Status: COMPLETED FOR MVP



The RAAHAT AI model evaluation has been completed using the available validation data.



The baseline Logistic Regression model was compared with Linear SVM.



The Linear SVM was selected as the current MVP model based on stronger Micro Recall, Micro F1, Macro F1, and Hamming Loss results.



The evaluation artifacts are saved in the outputs directory.



The results are documented for model selection, backend handover, and responsible interpretation.

