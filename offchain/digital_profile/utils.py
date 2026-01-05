from __future__ import annotations
import re
from collections import Counter

_WORD_RE = re.compile(r"[A-Za-z']+")

def tokenize(text: str) -> list[str]:
    return [t.lower() for t in _WORD_RE.findall(text or "")]

def sentence_split(text: str) -> list[str]:
    # simple heuristic split
    parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
    return [p.strip() for p in parts if p.strip()]

def top_ngrams(tokens: list[str], n: int, k: int) -> list[str]:
    if len(tokens) < n:
        return []
    grams = [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
    c = Counter(grams)
    return [g for g, _ in c.most_common(k)]
