"""
RAAHAT AI - Text Preprocessing Module

This module contains the basic text preprocessing functions
that can be reused during model training and inference.
"""

import re


def normalize_text(text: str) -> str:
    """
    Perform basic, reproducible text normalization.

    Operations:
    1. Convert input to string.
    2. Remove leading/trailing whitespace.
    3. Collapse repeated whitespace.
    """

    if text is None:
        return ""

    text = str(text).strip()
    text = re.sub(r"\s+", " ", text)

    return text


def preprocess_text(text: str) -> str:
    """
    Main preprocessing function.

    This function currently applies conservative normalization
    so that meaningful emotional information is not unnecessarily
    removed from the original text.
    """

    return normalize_text(text)


if __name__ == "__main__":
    examples = [
        "  I am really scared.   ",
        "I feel   very helpless!",
        "Thanks!!",
    ]

    for example in examples:
        print(f"Original    : {example}")
        print(f"Preprocessed: {preprocess_text(example)}")
        print("-" * 50)