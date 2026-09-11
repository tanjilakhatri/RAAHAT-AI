"""
RAAHAT AI - Baseline Multi-Label Model

This module provides a reusable baseline classifier for
predicting multiple emotion labels from TF-IDF features.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier


def create_baseline_model():
    """
    Create the baseline multi-label classification model.

    One-vs-Rest allows the model to independently learn
    each emotion label.
    """

    base_classifier = LogisticRegression(
        max_iter=1000,
        solver="liblinear",
    )

    model = OneVsRestClassifier(base_classifier)

    return model


def train_model(model, X_train, y_train):
    """
    Train the multi-label classifier.
    """

    model.fit(X_train, y_train)

    return model


def predict_labels(model, X):
    """
    Generate binary predictions for each emotion label.
    """

    return model.predict(X)


def predict_probabilities(model, X):
    """
    Generate probability estimates for each emotion label.
    """

    return model.predict_proba(X)