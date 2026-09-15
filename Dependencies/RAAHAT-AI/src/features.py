"""
RAAHAT AI - Feature Engineering Module

This module converts preprocessed text into numerical
TF-IDF features for traditional machine learning models.
"""

from sklearn.feature_extraction.text import TfidfVectorizer


def create_tfidf_vectorizer():
    """
    Create the TF-IDF vectorizer used by the baseline model.
    """

    return TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        min_df=2,
        max_features=10000,
    )


def fit_tfidf(texts):
    """
    Fit the TF-IDF vectorizer on training text
    and transform the text into numerical features.
    """

    vectorizer = create_tfidf_vectorizer()
    features = vectorizer.fit_transform(texts)

    return vectorizer, features


def transform_tfidf(vectorizer, texts):
    """
    Transform new text using an already fitted
    TF-IDF vectorizer.
    """

    return vectorizer.transform(texts)