from __future__ import annotations
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_topics(texts: list[str], top_k: int = 12) -> list[str]:
    # Light, explainable baseline: mean TF-IDF term weights
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2), min_df=1)
    X = vectorizer.fit_transform([t for t in texts if str(t).strip()])
    if X.shape[0] == 0:
        return []
    scores = X.mean(axis=0).A1
    vocab = vectorizer.get_feature_names_out()
    ranked = sorted(zip(vocab, scores), key=lambda x: x[1], reverse=True)
    topics = []
    for w, _ in ranked:
        # avoid very short tokens
        if len(w) >= 3:
            topics.append(w)
        if len(topics) >= top_k:
            break
    return topics
