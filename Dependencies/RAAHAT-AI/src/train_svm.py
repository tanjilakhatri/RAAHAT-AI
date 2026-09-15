"""
RAAHAT AI - Linear SVM Training

This script trains a multi-label Linear SVM model
using the same TF-IDF representation as the baseline.
"""

import joblib
import pandas as pd

from preprocessing import preprocess_text
from features import fit_tfidf
from svm_model import create_svm_model, train_svm_model


# --------------------------------------------------
# 1. Load training dataset
# --------------------------------------------------

train_df = pd.read_csv("data/goemotions/train.csv")

print("Training dataset loaded.")
print(f"Training rows: {len(train_df)}")


# --------------------------------------------------
# 2. Preprocess text
# --------------------------------------------------

train_texts = train_df["text"].apply(preprocess_text)

print("Text preprocessing completed.")


# --------------------------------------------------
# 3. Prepare multi-label targets
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


y_train_df = pd.DataFrame(
    0,
    index=train_df.index,
    columns=label_columns
)


for index, emotions in train_df["emotions"].items():

    for emotion in str(emotions).split(","):

        emotion = emotion.strip()

        if emotion in label_columns:
            y_train_df.loc[index, emotion] = 1


y_train = y_train_df.values

print(f"Label matrix shape: {y_train.shape}")


# --------------------------------------------------
# 4. Create TF-IDF features
# --------------------------------------------------

vectorizer, X_train = fit_tfidf(train_texts)

print("TF-IDF feature extraction completed.")
print(f"Feature matrix shape: {X_train.shape}")


# --------------------------------------------------
# 5. Create SVM model
# --------------------------------------------------

model = create_svm_model()

print("Linear SVM model created.")


# --------------------------------------------------
# 6. Train SVM
# --------------------------------------------------

model = train_svm_model(
    model,
    X_train,
    y_train
)

print("Linear SVM training completed successfully.")


# --------------------------------------------------
# 7. Save SVM model and vectorizer
# --------------------------------------------------

joblib.dump(
    model,
    "models/svm_model.pkl"
)

joblib.dump(
    vectorizer,
    "models/svm_tfidf_vectorizer.pkl"
)

print("SVM model saved: models/svm_model.pkl")
print("SVM TF-IDF vectorizer saved: models/svm_tfidf_vectorizer.pkl")