"""
RAAHAT AI - Linear SVM Model

This module provides a Linear Support Vector Machine
baseline for multi-label emotion classification.
"""

from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier


def create_svm_model():
    """
    Create the Linear SVM multi-label classifier.
    """

    base_classifier = LinearSVC(
        C=1.0,
        max_iter=2000
    )

    model = OneVsRestClassifier(
        base_classifier
    )

    return model


def train_svm_model(model, X_train, y_train):
    """
    Train the Linear SVM model.
    """

    model.fit(
        X_train,
        y_train
    )

    return model


def predict_svm_labels(model, X):
    """
    Generate multi-label predictions.
    """

    return model.predict(X)