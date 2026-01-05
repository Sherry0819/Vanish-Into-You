from __future__ import annotations
import argparse, json
from pathlib import Path

from .extract_style import extract_style_features
from .topic_model import extract_topics

def load_texts(path: str) -> list[str]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    return [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

def build_profile(texts: list[str]) -> dict:
    return {
        "meta": {
            "module": "digital_profile",
            "version": "0.2",
            "notes": "Interpretability-first (no LLM). Topics via TF-IDF; style via lexical+syntactic features."
        },
        "style": extract_style_features(texts),
        "topics": extract_topics(texts),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to newline-separated English texts")
    ap.add_argument("--out", required=True, help="Output path for persona_profile.json")
    args = ap.parse_args()

    texts = load_texts(args.input)
    profile = build_profile(texts)

    outp = Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(profile, indent=2), encoding="utf-8")
    print(f"Wrote profile -> {outp}")

if __name__ == "__main__":
    main()
