# RAAHAT AI - Data Dictionary

## 1. Purpose

This document describes the dataset fields used during development of the RAAHAT AI text-based emotion and stress/distress vulnerability assessment MVP.

The dataset preparation was based on the GoEmotions dataset and the project-specific consensus-label dataset created from the raw annotation files.

---

## 2. Dataset Source

Dataset: GoEmotions

Source: Google Research / GoEmotions

The dataset contains Reddit comments annotated for emotions.

The original dataset contains 27 emotion categories and a Neutral category.

The dataset is used in this project as a general emotional-language dataset.

It is not a clinical stress or trauma dataset and should not be represented as clinical validation data.

---

## 3. Raw Dataset Structure

The raw data was provided through three CSV files:

- goemotions_1.csv
- goemotions_2.csv
- goemotions_3.csv

The raw files contain individual rater annotations.

The project combined these records by comment ID to construct a consensus-label dataset.

---

## 4. Raw Dataset Fields

| Field | Type | Meaning | Used in Final Model |
|---|---|---|---|
| text | String | Reddit comment text | Yes |
| id | String | Unique comment identifier | Yes, for dataset processing |
| author | String | Reddit author identifier | No |
| subreddit | String | Subreddit associated with the comment | No |
| link_id | String | Reddit link identifier | No |
| parent_id | String | Parent Reddit comment identifier | No |
| created_utc | Numeric | Comment creation timestamp | No |
| rater_id | String | Identifier of the annotator | No |
| example_very_unclear | Boolean/Indicator | Indicates whether the example was considered very unclear | No |
| emotion columns | Binary/Indicator | Individual emotion annotations | Used to construct consensus labels |
| neutral | Binary/Indicator | Neutral emotion annotation | Used during dataset preparation |

---

## 5. Emotion Labels

The raw dataset contains 27 emotion categories plus Neutral.

The project used the emotion annotations to construct consensus emotion labels.

The consensus label represents an emotion when it received at least two votes for a comment.

---

## 6. Project Consensus Dataset

The processed consensus dataset is:

data/goemotions/goemotions_consensus.csv

Current columns:

| Field | Type | Meaning | Purpose |
|---|---|---|---|
| id | String | Comment identifier | Identifies the source comment |
| text | String | Comment text | Primary model input |
| emotions | String | Consensus emotion label or labels | Prediction target |
| num_consensus_emotions | Integer | Number of consensus emotion labels | Dataset analysis |

The consensus dataset contains 54,263 valid rows.

---

## 7. Consensus Label Rule

Consensus labels were created by selecting emotion labels that received at least two annotations for the same comment.

Comments without at least one consensus emotion were not included in the final consensus dataset.

This produced a dataset suitable for the project's multi-label emotion prediction approach.

---

## 8. Dataset Quality Checks

The processed consensus dataset was checked for:

- Missing text
- Missing emotion labels
- Duplicate IDs
- Duplicate text
- Number of consensus emotions
- Emotion-label format
- Class distribution

The final consensus dataset contained:

- Rows: 54,263
- Missing text: 0
- Missing emotions: 0
- Duplicate IDs: 0

---

## 9. Duplicate Text Handling

Duplicate text analysis was performed before model training.

Repeated text can create data leakage if the same or effectively identical text appears across training and validation/test sets.

The project therefore created a normalized text grouping value.

Normalization included:

1. Converting text to lowercase.
2. Collapsing repeated whitespace.
3. Removing unnecessary surrounding whitespace.

The normalized text grouping was used to create leakage-safe dataset splits.

---

## 10. Leakage-Safe Dataset Split

The consensus dataset was divided into:

| Split | Rows |
|---|---:|
| Training | 43,412 |
| Validation | 5,418 |
| Test | 5,433 |
| Total | 54,263 |

Text groups were kept within a single split to reduce the possibility of duplicate or near-identical text appearing across different splits.

The split was created using a reproducible random state.

---

## 11. Model Input

The final model uses:

text

as its primary input.

The text is passed through the project's preprocessing module and then transformed into TF-IDF features.

The other raw metadata fields are not used as model features.

---

## 12. Target Representation

The project uses emotion labels as the prediction targets.

The model predicts emotion-related signals using a multi-label approach.

These emotion signals are subsequently grouped into stress/distress-related signal groups for the RAAHAT Stress Vulnerability Index.

---

## 13. Data Types Used by the AI Pipeline

The main data types are:

| Data | Type |
|---|---|
| Comment text | String |
| Comment ID | String |
| Emotion label count | Integer |
| Emotion indicators | Binary/Indicator |
| Consensus emotion labels | String/List representation |
| TF-IDF features | Sparse numerical matrix |

---

## 14. Fields Excluded from Model Features

The following fields are excluded from the final text-based model features:

- author
- subreddit
- link_id
- parent_id
- created_utc
- rater_id
- annotation metadata

These fields are not required for the current MVP prediction task.

Excluding unnecessary metadata also reduces dependence on information that is not part of the user's textual statement.

---

## 15. Missing-Value Handling

The final consensus dataset was checked for missing values in the primary fields.

Text and emotion labels contained no missing values in the final consensus dataset.

For inference, empty text is rejected by the AI service rather than converted into a model prediction.

---

## 16. Data Leakage Considerations

The TF-IDF feature extractor is fitted using training data only.

Validation and test data are transformed using the fitted training vectorizer.

The same saved vectorizer is used during standalone inference.

This prevents validation, test, or production inputs from being used to fit the training feature representation.

---

## 17. Class Distribution

The dataset contains multiple emotion classes with unequal frequencies.

Therefore, accuracy alone is not sufficient for evaluating the model.

The project uses Precision, Recall, F1-score, class-wise metrics, and confusion/error analysis to evaluate model performance.

---

## 18. Dataset Limitations

The GoEmotions dataset represents general emotional language from Reddit comments.

Important limitations include:

- It is not a clinical stress dataset.
- It is not a trauma-assessment dataset.
- Reddit language may differ from language used by real complainants or victims.
- Emotion labels do not directly represent clinical conditions.
- Text alone may not capture the complete context of a person's situation.
- Language, culture, spelling, and code-switching may affect model performance.
- Model performance on the GoEmotions-derived data does not establish clinical validity.

Therefore, the RAAHAT output must remain a non-clinical decision-support/risk indicator and must not be presented as a diagnosis.

---

## 19. Data Governance Considerations

Only fields required for the current AI task should be used.

Unnecessary personal or metadata fields are excluded from the model feature set.

Dataset source, data dictionary, preprocessing decisions, feature definitions, model version, evaluation results, and limitations should remain documented so that the AI pipeline is reproducible and traceable.

---

## 20. Current Status

Status: COMPLETED FOR MVP

The dataset has been:

- Inspected
- Validated
- Consensus-labelled
- Checked for missing values
- Checked for duplicate IDs
- Analyzed for duplicate text
- Grouped to reduce leakage
- Split into training, validation, and test datasets

The final model uses the processed text field and does not use the original Reddit metadata fields as prediction features.