"""
RAAHAT AI - Standalone Inference Pipeline

This module connects:
1. Text preprocessing
2. TF-IDF feature extraction
3. Trained Linear SVM model
4. Emotion signal scoring
5. Stress Vulnerability Index (SVI) mapping

The output is a non-clinical support indicator.
It is NOT a medical or psychiatric diagnosis.

Important:
The Linear SVM decision scores are transformed into bounded
signal strengths using a sigmoid function. These values are
NOT calibrated probabilities and must not be interpreted
as model confidence.
"""

from pathlib import Path

import joblib
import numpy as np

from src.preprocessing import preprocess_text
from src.risk_mapping import generate_svi_result


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "svm_model.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "svm_tfidf_vectorizer.pkl"


EMOTION_LABELS = [
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


def load_model_and_vectorizer():
    """Load the trained SVM model and TF-IDF vectorizer."""

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"SVM model not found: {MODEL_PATH}"
        )

    if not VECTORIZER_PATH.exists():
        raise FileNotFoundError(
            f"TF-IDF vectorizer not found: {VECTORIZER_PATH}"
        )

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer

MODEL, VECTORIZER = load_model_and_vectorizer()


def sigmoid(value):
    """Convert an SVM decision score into a bounded signal strength."""

    return 1.0 / (1.0 + np.exp(-value))


def predict_emotion_signals(text, model, vectorizer):
    """
    Preprocess the text, generate TF-IDF features,
    and calculate bounded emotion signal strengths.

    These values are NOT calibrated probabilities.
    """

    processed_text = preprocess_text(text)

    if not processed_text:
        raise ValueError("Input text cannot be empty.")

    features = vectorizer.transform([processed_text])

    decision_scores = model.decision_function(features)[0]

    signal_scores = {}

    for emotion, score in zip(EMOTION_LABELS, decision_scores):
        signal_scores[emotion] = float(sigmoid(score))

    return signal_scores

def run_inference(text):
    """Run complete RAAHAT AI inference pipeline."""
    if text is None or not str(text).strip():
        raise ValueError("Input text cannot be empty.")

    emotion_signals = predict_emotion_signals(
        text,
        MODEL,
        VECTORIZER
    )

    svi_result = generate_svi_result(emotion_signals)

    detected_emotions = [
        emotion
        for emotion, value in emotion_signals.items()
        if value >= 0.50
    ]

    return {
        "input_text": text,
        "predicted_emotions": detected_emotions,
        "emotion_signal_strengths": emotion_signals,
        "svi_score": svi_result["svi_score"],
        "risk_category": svi_result["risk_category"],
        "signal_groups": svi_result["signal_groups"],
        "human_review_required": svi_result["human_review_required"],
        "diagnostic": svi_result["diagnostic"],
    }


if __name__ == "__main__":

    test_text = (
        "I am very scared and confused about what happened. "
        "I don't know what to do."
    )

    print("=" * 70)
    print("RAAHAT AI - REAL INFERENCE PIPELINE TEST")
    print("=" * 70)

    try:

        result = run_inference(test_text)

        print("\nInput Text:")
        print(result["input_text"])

        print("\nPredicted Emotions:")

        if result["predicted_emotions"]:

            for emotion in result["predicted_emotions"]:
                print(f"- {emotion}")

        else:
            print("- No emotion detected")

        print("\nEmotion Signal Strengths:")

        for emotion, value in result["emotion_signal_strengths"].items():

            if value >= 0.50:
                print(f"- {emotion}: {value:.4f}")

        print(f"\nSVI Score       : {result['svi_score']}")
        print(f"Risk Category   : {result['risk_category']}")
        print(
            f"Human Review    : "
            f"{result['human_review_required']}"
        )
        print(
            f"Diagnostic      : "
            f"{result['diagnostic']}"
        )

        print("\nSignal Groups:")

        for group, score in result["signal_groups"].items():
            print(f"{group}: {score:.4f}")

        print("=" * 70)

    except Exception as error:

        print("\nERROR:")
        print(error)

        print("\nPlease check:")
        print("1. SVM model exists in models/")
        print("2. TF-IDF vectorizer exists in models/")
        print("3. Project is being run from RAAHAT-AI root folder")
        print("4. Virtual environment is activated")