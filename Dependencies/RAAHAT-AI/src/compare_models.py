"""
RAAHAT AI - Model Comparison

Compares the Logistic Regression baseline
with the Linear SVM model using the same
validation dataset and evaluation metrics.
"""

import pandas as pd
import joblib

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    hamming_loss,
)


# --------------------------------------------------
# 1. Load validation dataset
# --------------------------------------------------

validation_df = pd.read_csv(
    "data/goemotions/validation.csv"
)

print("Validation dataset loaded.")
print(f"Validation rows: {len(validation_df)}")


# --------------------------------------------------
# 2. Prepare validation labels
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
# 3. Load Logistic Regression model
# --------------------------------------------------

baseline_model = joblib.load(
    "models/baseline_model.pkl"
)

baseline_vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

print("Logistic Regression model loaded.")


# --------------------------------------------------
# 4. Load Linear SVM model
# --------------------------------------------------

svm_model = joblib.load(
    "models/svm_model.pkl"
)

svm_vectorizer = joblib.load(
    "models/svm_tfidf_vectorizer.pkl"
)

print("Linear SVM model loaded.")


# --------------------------------------------------
# 5. Preprocess validation text
# --------------------------------------------------

from preprocessing import preprocess_text

validation_texts = validation_df["text"].apply(
    preprocess_text
)


# --------------------------------------------------
# 6. Generate Logistic Regression predictions
# --------------------------------------------------

X_baseline = baseline_vectorizer.transform(
    validation_texts
)

baseline_predictions = baseline_model.predict(
    X_baseline
)

print("Logistic Regression predictions generated.")


# --------------------------------------------------
# 7. Generate SVM predictions
# --------------------------------------------------

X_svm = svm_vectorizer.transform(
    validation_texts
)

svm_predictions = svm_model.predict(
    X_svm
)

print("Linear SVM predictions generated.")


# --------------------------------------------------
# 8. Evaluation function
# --------------------------------------------------

def calculate_metrics(y_true, y_pred):

    return {
        "Micro Precision": precision_score(
            y_true,
            y_pred,
            average="micro",
            zero_division=0
        ),

        "Micro Recall": recall_score(
            y_true,
            y_pred,
            average="micro",
            zero_division=0
        ),

        "Micro F1": f1_score(
            y_true,
            y_pred,
            average="micro",
            zero_division=0
        ),

        "Macro F1": f1_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0
        ),

        "Hamming Loss": hamming_loss(
            y_true,
            y_pred
        ),
    }


# --------------------------------------------------
# 9. Calculate metrics
# --------------------------------------------------

baseline_metrics = calculate_metrics(
    y_validation,
    baseline_predictions
)

svm_metrics = calculate_metrics(
    y_validation,
    svm_predictions
)


# --------------------------------------------------
# 10. Create comparison table
# --------------------------------------------------

comparison_df = pd.DataFrame(
    {
        "Metric": baseline_metrics.keys(),
        "Logistic Regression": baseline_metrics.values(),
        "Linear SVM": svm_metrics.values(),
    }
)


# --------------------------------------------------
# 11. Display comparison
# --------------------------------------------------

print()
print("=" * 75)
print("RAAHAT AI - MODEL COMPARISON")
print("=" * 75)

print(
    comparison_df.to_string(
        index=False,
        formatters={
            "Logistic Regression": "{:.4f}".format,
            "Linear SVM": "{:.4f}".format,
        }
    )
)

print("=" * 75)


# --------------------------------------------------
# 12. Save comparison results
# --------------------------------------------------

comparison_df.to_csv(
    "outputs/model_comparison.csv",
    index=False
)

print()
print("Model comparison saved:")
print("outputs/model_comparison.csv")