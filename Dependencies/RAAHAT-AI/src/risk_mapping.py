"""
RAAHAT AI - Stress Vulnerability Index (SVI)

This module converts detected emotion signals into
an explainable, non-clinical vulnerability indicator.

The SVI is a support-prioritization signal and is
NOT a medical or psychiatric diagnosis.
"""

SIGNAL_GROUPS = {
    "fear_threat": ["fear", "nervousness"],
    "sadness_loss": ["sadness", "grief", "disappointment", "remorse"],
    "anger_frustration": ["anger", "annoyance", "disapproval", "disgust"],
    "confusion_uncertainty": ["confusion", "realization"],
}


def calculate_signal_strength(predictions):
    """
    Calculate the average strength of the
    distress-related signal groups.

    Predictions should be a dictionary containing
    emotion values between 0 and 1.
    """

    group_scores = {}

    for group, emotions in SIGNAL_GROUPS.items():

        values = [
            float(predictions.get(emotion, 0.0))
            for emotion in emotions
        ]

        if values:
            group_scores[group] = sum(values) / len(values)
        else:
            group_scores[group] = 0.0

    return group_scores


def calculate_svi(predictions):
    """
    Convert distress-related signal strength
    into an SVI score from 0 to 100.

    This is an initial MVP design and requires
    future domain validation.
    """

    group_scores = calculate_signal_strength(predictions)

    overall_signal = (
        sum(group_scores.values())
        / len(group_scores)
    )

    svi_score = round(overall_signal * 100, 2)

    svi_score = max(
        0.0,
        min(100.0, svi_score)
    )

    return svi_score, group_scores


def get_risk_category(svi_score):
    """
    Map the SVI score to an initial MVP category.
    """

    if svi_score < 25:
        return "Low"

    elif svi_score < 50:
        return "Moderate"

    elif svi_score < 75:
        return "High"

    else:
        return "Very High"


def generate_svi_result(predictions):
    """
    Generate the complete explainable SVI result.
    """

    svi_score, group_scores = calculate_svi(
        predictions
    )

    risk_category = get_risk_category(
        svi_score
    )

    return {
        "svi_score": svi_score,
        "risk_category": risk_category,
        "signal_groups": group_scores,
        "human_review_required": True,
        "diagnostic": False,
    }


if __name__ == "__main__":

    sample_predictions = {
        "fear": 0.80,
        "nervousness": 0.60,
        "sadness": 0.70,
        "grief": 0.40,
        "disappointment": 0.50,
        "remorse": 0.30,
        "anger": 0.20,
        "annoyance": 0.30,
        "disapproval": 0.20,
        "disgust": 0.10,
        "confusion": 0.60,
        "realization": 0.40,
    }

    result = generate_svi_result(
        sample_predictions
    )

    print("=" * 70)
    print("RAAHAT AI - SVI MODULE TEST")
    print("=" * 70)

    print(f"SVI Score       : {result['svi_score']}")
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