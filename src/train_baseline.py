"""
RAAHAT AI - Baseline Model Training

This script trains a baseline multi-label emotion
classification model using TF-IDF features.
"""

import pandas as pd
import joblib

from preprocessing import preprocess_text
from features import fit_tfidf
from model import create_baseline_model, train_model


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


# Create an empty binary label matrix
y_train_df = pd.DataFrame(
    0,
    index=train_df.index,
    columns=label_columns
)


# Convert the emotions column into binary labels
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
# 5. Create baseline model
# --------------------------------------------------

model = create_baseline_model()

print("Baseline model created.")


# --------------------------------------------------
# 6. Train model
# --------------------------------------------------

model = train_model(
    model,
    X_train,
    y_train
)

print("Baseline model training completed successfully.")
print(f"Number of labels: {len(label_columns)}")
# --------------------------------------------------
# 7. Save trained model and TF-IDF vectorizer
# --------------------------------------------------

joblib.dump(model, "models/baseline_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("Baseline model saved: models/baseline_model.pkl")
print("TF-IDF vectorizer saved: models/tfidf_vectorizer.pkl")
