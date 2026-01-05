from __future__ import annotations
import argparse, json, random
from pathlib import Path
from .utils import sentence_split, tokenize

def _target_sentence_len(style: dict) -> float:
    return float(style.get("avg_sentence_length", 12.0) or 12.0)

def _apply_length_style(sentences: list[str], target_len: float) -> list[str]:
    # merge or split sentences to move toward target length (simple heuristic)
    out = []
    buf = ""
    for s in sentences:
        if not buf:
            buf = s
        else:
            if len(tokenize(buf)) < target_len * 0.7:
                buf = buf + " " + s
            else:
                out.append(buf)
                buf = s
    if buf:
        out.append(buf)

    # split overly long sentences
    final = []
    for s in out:
        toks = s.split()
        if len(toks) > target_len * 1.8 and "," in s:
            parts = [p.strip() for p in s.split(",") if p.strip()]
            final.extend([parts[0] + "."] + [p + "." for p in parts[1:]])
        else:
            final.append(s if s.endswith((".", "!", "?")) else s + ".")
    return final

def rewrite_text(text: str, profile: dict) -> str:
    style = profile.get("style", {})
    topics = profile.get("topics", [])
    bigrams = style.get("top_bigrams", [])
    trigrams = style.get("top_trigrams", [])
    target_len = _target_sentence_len(style)

    sents = sentence_split(text)
    if not sents:
        sents = [text.strip()]

    sents = _apply_length_style(sents, target_len)

    # sprinkle a voice marker (phrase) if available
    markers = [m for m in (trigrams + bigrams) if len(m.split()) >= 2]
    if markers:
        insert = random.choice(markers)
        sents[0] = f"{sents[0].rstrip('.!?')}, {insert}."

    # add a topical keyword gently if available
    if topics:
        kw = random.choice(topics[: min(8, len(topics))])
        sents[-1] = sents[-1].rstrip(".!?") + f" — {kw}."

    # reflect punctuation tendencies (approx.)
    ex = int(style.get("exclamation_count", 0))
    qn = int(style.get("question_count", 0))
    if ex > qn and len(sents) >= 2:
        sents[-2] = sents[-2].rstrip(".") + "!"
    elif qn > ex:
        sents[-1] = sents[-1].rstrip(".") + "?"

    return "\n".join(sents)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", required=True, help="Path to persona_profile.json")
    ap.add_argument("--text", required=True, help="Text to rewrite in-style")
    args = ap.parse_args()

    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    print(rewrite_text(args.text, profile))

if __name__ == "__main__":
    main()
