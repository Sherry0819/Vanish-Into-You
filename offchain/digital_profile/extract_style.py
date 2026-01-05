from __future__ import annotations
import statistics
from collections import Counter
from .utils import tokenize, sentence_split, top_ngrams

PRONOUNS = {"i","me","my","mine","you","your","yours","we","us","our","ours","they","them","their","theirs"}

def extract_style_features(texts: list[str]) -> dict:
    sentence_lengths = []
    exclamations = 0
    questions = 0

    all_tokens = []
    for t in texts:
        exclamations += (t or "").count("!")
        questions += (t or "").count("?")
        for s in sentence_split(t):
            toks = tokenize(s)
            if toks:
                sentence_lengths.append(len(toks))
            all_tokens.extend(toks)

    if not sentence_lengths:
        sentence_lengths = [0]

    token_counts = Counter(all_tokens)
    pronoun_counts = {p: token_counts.get(p, 0) for p in PRONOUNS}
    total_tokens = max(1, sum(token_counts.values()))
    pronoun_ratio = {p: pronoun_counts[p]/total_tokens for p in pronoun_counts}

    # common phrases that indicate "voice" (bigrams/trigrams)
    bigrams = top_ngrams(all_tokens, 2, 12)
    trigrams = top_ngrams(all_tokens, 3, 8)

    return {
        "avg_sentence_length": float(statistics.mean(sentence_lengths)),
        "sentence_length_std": float(statistics.pstdev(sentence_lengths)),
        "exclamation_count": int(exclamations),
        "question_count": int(questions),
        "top_words": [w for w, _ in token_counts.most_common(20)],
        "top_bigrams": bigrams,
        "top_trigrams": trigrams,
        "pronoun_ratio": pronoun_ratio,
    }
