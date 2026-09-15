from src.inference import run_inference


def test_distress_input():
    text = "I am scared and confused about what happened."
    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["risk_category"] in ["Low", "Moderate", "High", "Very High"]
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 1 - DISTRESS INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print(f"Emotions: {result['predicted_emotions']}")
    print("Result: PASS")
    print()


def test_neutral_input():
    text = "The meeting is scheduled for tomorrow."
    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 2 - NEUTRAL INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print(f"Emotions: {result['predicted_emotions']}")
    print("Result: PASS")
    print()


def test_positive_input():
    text = "I am happy and grateful for the support."
    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 3 - POSITIVE INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print(f"Emotions: {result['predicted_emotions']}")
    print("Result: PASS")
    print()


def test_empty_input():
    try:
        run_inference("")
        assert False, "Empty input should raise ValueError"
    except ValueError:
        pass

    print("=" * 70)
    print("TEST 4 - EMPTY INPUT")
    print("=" * 70)
    print("Result: PASS")
    print()


def test_consistency():
    text = "I am scared and confused about what happened."

    result_1 = run_inference(text)
    result_2 = run_inference(text)

    assert result_1["svi_score"] == result_2["svi_score"]
    assert result_1["risk_category"] == result_2["risk_category"]
    assert result_1["predicted_emotions"] == result_2["predicted_emotions"]

    print("=" * 70)
    print("TEST 5 - CONSISTENCY")
    print("=" * 70)
    print(f"Run 1 SVI: {result_1['svi_score']}")
    print(f"Run 2 SVI: {result_2['svi_score']}")
    print("Result: PASS")
    print()


def test_whitespace_input():
    text = "   I am scared and confused.   "
    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 6 - WHITESPACE INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print("Result: PASS")
    print()


def test_short_input():
    text = "Help."
    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 7 - SHORT INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print("Result: PASS")
    print()


def test_long_input():
    text = (
        "I am feeling scared and confused about what happened. "
        "I need help understanding what I should do next. "
    ) * 20

    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 8 - LONG INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print("Result: PASS")
    print()


def test_special_character_input():
    text = "I am scared!!! @#$% What should I do???"
    result = run_inference(text)

    assert 0 <= result["svi_score"] <= 100
    assert result["human_review_required"] is True
    assert result["diagnostic"] is False

    print("=" * 70)
    print("TEST 9 - SPECIAL CHARACTER INPUT")
    print("=" * 70)
    print(f"SVI: {result['svi_score']}")
    print(f"Risk: {result['risk_category']}")
    print("Result: PASS")
    print()


def test_output_structure():
    text = "I am scared and confused."
    result = run_inference(text)

    required_keys = {
        "input_text",
        "predicted_emotions",
        "emotion_signal_strengths",
        "svi_score",
        "risk_category",
        "signal_groups",
        "human_review_required",
        "diagnostic",
    }

    assert required_keys.issubset(result.keys())

    print("=" * 70)
    print("TEST 10 - OUTPUT STRUCTURE")
    print("=" * 70)
    print("Required output fields: PASS")
    print("Result: PASS")
    print()


if __name__ == "__main__":
    test_distress_input()
    test_neutral_input()
    test_positive_input()
    test_empty_input()
    test_consistency()
    test_whitespace_input()
    test_short_input()
    test_long_input()
    test_special_character_input()
    test_output_structure()

    print("=" * 70)
    print("ALL 10 INFERENCE TESTS PASSED")
    print("=" * 70)