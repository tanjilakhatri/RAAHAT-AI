# RAAHAT Dataset Selection

## Objective

Select datasets that can support the development of a text-based stress, distress and emotional vulnerability assessment module for RAAHAT.

## Dataset Requirements

The selected data should ideally provide:

- Text-based examples
- Emotion, stress, distress or related labels
- English and/or Hindi language coverage
- Sufficient number of examples
- Clear label definitions
- Suitable train/test or validation possibilities
- Permitted usage/licensing
- No unnecessary personally identifiable information
- Appropriate ethical considerations

## Important Consideration

A general sentiment or emotion dataset must not automatically be treated as a trauma or clinical stress dataset.

The relationship between dataset labels and the RAAHAT stress/distress target must be explicitly justified.

## Candidate Dataset Categories

1. Emotion classification datasets
2. Stress/distress text datasets
3. Mental-health language datasets
4. Hindi-English or multilingual datasets

## Dataset Selection Process

Each candidate dataset will be evaluated based on:

- Relevance
- Language coverage
- Label quality
- Dataset size
- Class balance
- License and permitted use
- Privacy and ethical considerations
- Suitability for the RAAHAT MVP

## Final Dataset

The final dataset will be selected only after inspection and comparison of candidate datasets.

## Candidate 1: GoEmotions

### Purpose of Evaluation

GoEmotions is being evaluated as a possible source of emotion-level text signals for the RAAHAT AI module.

### Dataset Information

- Dataset size: 58k English Reddit comments
- Emotion categories: 27 emotion categories + Neutral
- Language: English
- Annotation: Manually annotated
- Reported BERT average F1-score: 0.46

### Potential Use in RAAHAT

The dataset may help the AI learn general emotional-language patterns that can contribute to stress/distress-related signals.

### Important Limitation

GoEmotions is an emotion classification dataset. It should not be represented as a direct trauma or clinical stress dataset.

Its suitability for the final RAAHAT model will be evaluated against other candidate datasets.

## Candidate 2: IndieMH
### Purpose of Evaluation

IndieMH is being evaluated as a possible source of mental-health-related text for the RAAHAT AI module.

### Dataset Information

- Language coverage: English and Hindi
- Dataset type: Mental-health-related text
- Data source: Real mental-health therapy session transcripts
- Dataset size: Reported within the 10K–100K range
- License: CC-BY-NC-4.0

### Potential Use in RAAHAT

The dataset may provide more domain-relevant language patterns than a general emotion dataset.

It may help in studying language associated with mental-health-related experiences and emotional distress.

### Important Limitations

IndieMH has significant usage restrictions.

The dataset is intended for non-commercial academic research and has privacy and data-handling requirements.

It must not be treated as a clinical diagnostic dataset.

Its suitability for the RAAHAT hackathon MVP must be verified against its license, intended use, privacy requirements and the project's deployment conditions.

### Selection Status

Candidate only — not selected as the final dataset.

## Candidate 3: PRISM-MH

### Purpose of Evaluation

PRISM-MH is being evaluated as a possible bilingual dataset for the RAAHAT AI module because it contains mental-health-related text in both English and Hindi.

### Dataset Information

- Dataset size: 5,500 passages
- Languages: English and Hindi
- Text type: First-person mental-health-related passages
- Conditions: Anxiety, depression, panic, trauma, burnout and none
- Symptoms: Multiple symptom-level labels
- Severity: Minimal, mild, moderate and severe
- Temporal patterns: Acute, chronic, episodic and related categories
- Context: Work, school, family, relationship, trauma and other life domains
- Impact: Functional impact on daily life
- Care: Help-seeking and care status

### Potential Use in RAAHAT

PRISM-MH is potentially useful because its labels include trauma, symptoms, severity and functional impact.

These characteristics are more closely related to the RAAHAT stress/distress vulnerability objective than a general emotion dataset.

The English-Hindi pairing may also support multilingual experimentation for the RAAHAT MVP.

### Important Limitations

The dataset contains synthetically generated first-person narratives rather than direct real-world victim or complainant conversations.

Therefore, model performance on this dataset must not be interpreted as proof of real-world trauma or distress assessment accuracy.

The dataset's licensing and permitted use must also be verified before inclusion in the final RAAHAT implementation.

### Selection Status

Candidate only — not selected as the final dataset.

## GoEmotions Annotation Structure

### Inspection Findings

The downloaded GoEmotions files contain annotation-level records rather than one independent row per unique comment.

The inspection found:

- Total annotation records: 211,225
- Unique comments: 58,011
- Raters per comment: 1 to 5
- Average raters per comment: 3.64
- Comments with 1 rater: 70
- Comments with 2 raters: 592
- Comments with 3 raters: 37,335
- Comments with 4 raters: 2,104
- Comments with 5 raters: 17,910

### Preprocessing Implication

Duplicate comment IDs must not automatically be treated as erroneous duplicate records.

Multiple records may represent annotations from different raters for the same underlying comment.

Therefore, any model-ready GoEmotions dataset must handle the annotation structure at the unique-comment level and avoid treating repeated annotations as independent training examples.

### RAAHAT Relevance

GoEmotions provides useful emotion-level language information, but its emotion labels should not automatically be interpreted as clinical stress, trauma or mental-health diagnoses.

Further evaluation is required before deciding whether GoEmotions should be used as a baseline dataset, supporting dataset, or excluded from the final RAAHAT model.