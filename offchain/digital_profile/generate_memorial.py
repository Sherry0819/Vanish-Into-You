from __future__ import annotations
import argparse, json
from pathlib import Path

def generate_memorial(profile: dict) -> str:
    style = profile.get("style", {})
    topics = profile.get("topics", [])

    lines = []
    lines.append("# Digital Memorial Portrait\n")

    lines.append("## Communication Style")
    lines.append(f"- **Average sentence length**: {style.get('avg_sentence_length'):.2f} words")
    lines.append(f"- **Sentence length variability (std)**: {style.get('sentence_length_std'):.2f}")
    lines.append(f"- **Exclamation usage**: {style.get('exclamation_count')}")
    lines.append(f"- **Question usage**: {style.get('question_count')}")

    lines.append("\n## Frequent Voice Markers")
    for p in style.get("top_trigrams", [])[:6]:
        lines.append(f"- “{p}”")
    for p in style.get("top_bigrams", [])[:6]:
        lines.append(f"- “{p}”")

    lines.append("\n## Core Topics (TF‑IDF)")
    for t in topics:
        lines.append(f"- {t}")

    lines.append("\n## Boundaries")
    lines.append("- This portrait summarizes authorized textual traces.")
    lines.append("- It does **not** claim to replicate consciousness or intent.")
    lines.append("- It should not be used to infer medical/legal states.")

    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", required=True, help="Path to persona_profile.json")
    ap.add_argument("--out", required=True, help="Output portrait markdown path")
    args = ap.parse_args()

    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    md = generate_memorial(profile)

    outp = Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(md, encoding="utf-8")
    print(f"Wrote portrait -> {outp}")

if __name__ == "__main__":
    main()
