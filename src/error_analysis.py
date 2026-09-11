"""
RAAHAT AI - Baseline Error Analysis

Identifies emotion classes where the baseline model
has weaker F1 performance.
"""

import pandas as pd

from evaluate_baseline import (
    report_df,
)


# --------------------------------------------------
# 1. Select emotion classes
# --------------------------------------------------

emotion_metrics = report_df.loc[
    [
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
].copy()


# --------------------------------------------------
# 2. Sort classes by F1 score
# --------------------------------------------------

emotion_metrics = emotion_metrics.sort_values(
    by="f1-score"
)


# --------------------------------------------------
# 3. Display weakest classes
# --------------------------------------------------

print()
print("=" * 70)
print("RAAHAT AI - BASELINE ERROR ANALYSIS")
print("=" * 70)

print("\nLowest-performing emotion classes:\n")

print(
    emotion_metrics[
        ["precision", "recall", "f1-score", "support"]
    ].head(10).to_string()
)

print("=" * 70)


# --------------------------------------------------
# 4. Save error-analysis results
# --------------------------------------------------

emotion_metrics.to_csv(
    "outputs/baseline_error_analysis.csv"
)

print()
print("Error analysis saved:")
print("outputs/baseline_error_analysis.csv")