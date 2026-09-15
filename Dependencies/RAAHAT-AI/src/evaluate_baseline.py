"""
RAAHAT AI - Baseline Model Evaluation

This script evaluates the trained baseline multi-label
emotion classification model on the validation dataset.
"""

import joblib
import pandas as pd

from preprocessing import preprocess_text
from features import transform_tfidf

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    hamming_loss,
)


# --------------------------------------------------
# 1. Load validation dataset
# --------------------------------------------------

val_df = pd.read_csv("data/goemotions/validation.csv")

print("Validation dataset loaded.")
print(f"Validation rows: {len(val_df)}")


# --------------------------------------------------
# 2. Load trained model and vectorizer
# --------------------------------------------------

model = joblib.load("models/baseline_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

print("Trained model loaded.")
print("TF-IDF vectorizer loaded.")


# --------------------------------------------------
# 3. Preprocess validation text
# --------------------------------------------------

val_texts = val_df["text"].apply(preprocess_text)

print("Validation text preprocessing completed.")


# --------------------------------------------------
# 4. Prepare validation labels
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


y_val_df = pd.DataFrame(
    0,
    index=val_df.index,
    columns=label_columns
)


for index, emotions in val_df["emotions"].items():

    for emotion in str(emotions).split(","):

        emotion = emotion.strip()

        if emotion in label_columns:
            y_val_df.loc[index, emotion] = 1


y_val = y_val_df.values

print(f"Validation label matrix shape: {y_val.shape}")


# --------------------------------------------------
# 5. Transform validation text
# --------------------------------------------------

X_val = transform_tfidf(
    vectorizer,
    val_texts
)

print(f"Validation feature matrix shape: {X_val.shape}")


# --------------------------------------------------
# 6. Generate predictions
# --------------------------------------------------

y_pred = model.predict(X_val)

print("Validation predictions generated.")


# --------------------------------------------------
# 7. Calculate evaluation metrics
# --------------------------------------------------

precision_micro = precision_score(
    y_val,
    y_pred,
    average="micro",
    zero_division=0
)

recall_micro = recall_score(
    y_val,
    y_pred,
    average="micro",
    zero_division=0
)

f1_micro = f1_score(
    y_val,
    y_pred,
    average="micro",
    zero_division=0
)

f1_macro = f1_score(
    y_val,
    y_pred,
    average="macro",
    zero_division=0
)

hamming = hamming_loss(
    y_val,
    y_pred
)

exact_accuracy = accuracy_score(
    y_val,
    y_pred
)


# --------------------------------------------------
# 8. Display results
# --------------------------------------------------

print()
print("=" * 55)
print("RAAHAT AI - BASELINE MODEL EVALUATION")
print("=" * 55)

print(f"Micro Precision : {precision_micro:.4f}")
print(f"Micro Recall    : {recall_micro:.4f}")
print(f"Micro F1 Score  : {f1_micro:.4f}")
print(f"Macro F1 Score  : {f1_macro:.4f}")
print(f"Hamming Loss    : {hamming:.4f}")
print(f"Exact Accuracy  : {exact_accuracy:.4f}")

print("=" * 55)
# --------------------------------------------------
# 9. Class-wise evaluation
# --------------------------------------------------

from sklearn.metrics import classification_report

report = classification_report(
    y_val,
    y_pred,
    target_names=label_columns,
    zero_division=0,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

print()
print("=" * 75)
print("RAAHAT AI - CLASS-WISE PERFORMANCE")
print("=" * 75)

print(
    report_df[
        ["precision", "recall", "f1-score", "support"]
    ].to_string()
)

print("=" * 75)

# --------------------------------------------------
# 10. Save class-wise evaluation results
# --------------------------------------------------

report_df.to_csv(
    "outputs/baseline_classwise_metrics.csv"
)

print()
print("Class-wise metrics saved:")
print("outputs/baseline_classwise_metrics.csv")