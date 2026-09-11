"""
RAAHAT AI - Linear SVM Evaluation

This script evaluates the trained Linear SVM model
using the validation dataset.
"""

import joblib
import pandas as pd

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    hamming_loss,
    accuracy_score,
    classification_report,
)

from preprocessing import preprocess_text


# --------------------------------------------------
# 1. Load validation dataset
# --------------------------------------------------

validation_df = pd.read_csv(
    "data/goemotions/validation.csv"
)

print("Validation dataset loaded.")
print(f"Validation rows: {len(validation_df)}")


# --------------------------------------------------
# 2. Load trained SVM model and vectorizer
# --------------------------------------------------

model = joblib.load(
    "models/svm_model.pkl"
)

vectorizer = joblib.load(
    "models/svm_tfidf_vectorizer.pkl"
)

print("SVM model loaded.")
print("SVM TF-IDF vectorizer loaded.")


# --------------------------------------------------
# 3. Preprocess validation text
# --------------------------------------------------

validation_texts = validation_df["text"].apply(
    preprocess_text
)

print("Validation text preprocessing completed.")


# --------------------------------------------------
# 4. Prepare multi-label targets
# --------------------------------------------------

label_columns = [
    "admiration",
    "amusement",
    "anger",
    "annoyance",
    "approval",
    "caring",
    "confusion",
    "curiosity",
    "desire",
    "disappointment",
    "disapproval",
    "disgust",
    "embarrassment",
    "excitement",
    "fear",
    "gratitude",
    "grief",
    "joy",
    "love",
    "nervousness",
    "optimism",
    "pride",
    "realization",
    "relief",
    "remorse",
    "sadness",
    "surprise",
    "neutral",
]


y_validation_df = pd.DataFrame(
    0,
    index=validation_df.index,
    columns=label_columns
)


for index, emotions in validation_df["emotions"].items():

    for emotion in str(emotions).split(","):

        emotion = emotion.strip()

        if emotion in label_columns:
            y_validation_df.loc[
                index,
                emotion
            ] = 1


y_validation = y_validation_df.values

print(
    f"Validation label matrix shape: "
    f"{y_validation.shape}"
)


# --------------------------------------------------
# 5. Transform validation text
# --------------------------------------------------

X_validation = vectorizer.transform(
    validation_texts
)

print("Validation TF-IDF transformation completed.")
print(
    f"Validation feature matrix shape: "
    f"{X_validation.shape}"
)


# --------------------------------------------------
# 6. Generate predictions
# --------------------------------------------------

y_pred = model.predict(
    X_validation
)

print("SVM predictions generated.")


# --------------------------------------------------
# 7. Calculate overall metrics
# --------------------------------------------------

micro_precision = precision_score(
    y_validation,
    y_pred,
    average="micro",
    zero_division=0
)

micro_recall = recall_score(
    y_validation,
    y_pred,
    average="micro",
    zero_division=0
)

micro_f1 = f1_score(
    y_validation,
    y_pred,
    average="micro",
    zero_division=0
)

macro_f1 = f1_score(
    y_validation,
    y_pred,
    average="macro",
    zero_division=0
)

hamming = hamming_loss(
    y_validation,
    y_pred
)

exact_accuracy = accuracy_score(
    y_validation,
    y_pred
)


# --------------------------------------------------
# 8. Display overall evaluation
# --------------------------------------------------

print()
print("=" * 70)
print("RAAHAT AI - LINEAR SVM VALIDATION RESULTS")
print("=" * 70)

print(
    f"Micro Precision : {micro_precision:.4f}"
)

print(
    f"Micro Recall    : {micro_recall:.4f}"
)

print(
    f"Micro F1        : {micro_f1:.4f}"
)

print(
    f"Macro F1        : {macro_f1:.4f}"
)

print(
    f"Hamming Loss    : {hamming:.4f}"
)

print(
    f"Exact Accuracy  : {exact_accuracy:.4f}"
)

print("=" * 70)


# --------------------------------------------------
# 9. Class-wise evaluation
# --------------------------------------------------

report = classification_report(
    y_validation,
    y_pred,
    target_names=label_columns,
    output_dict=True,
    zero_division=0
)

report_df = pd.DataFrame(report).transpose()


print()
print("=" * 70)
print("CLASS-WISE SVM PERFORMANCE")
print("=" * 70)

print(
    report_df[
        ["precision", "recall", "f1-score", "support"]
    ].loc[label_columns].to_string()
)

print("=" * 70)


# --------------------------------------------------
# 10. Save class-wise metrics
# --------------------------------------------------

report_df.to_csv(
    "outputs/svm_classwise_metrics.csv"
)

print()
print("Class-wise SVM metrics saved:")
print(
    "outputs/svm_classwise_metrics.csv"
)