# Research Motivation (Mini Proposal)

## Motivation
As digital life expands across financial and social platforms, individuals accumulate a growing set of assets and identity traces:
crypto holdings, NFTs, creative works, and access to online accounts. Sudden death, incapacity, or prolonged inactivity
can cause these assets and records to become inaccessible, producing avoidable loss and distress for families.

Existing solutions often suffer from one or more limitations:
- **Custodial risk** (a single party must be trusted with secrets),
- **Weak triggering** (pure timeouts are easy to game or too conservative),
- **Poor privacy** (sensitive information is exposed or centralized),
- **Lack of representation** (families receive assets but not context, meaning, or curated works).

## Core Research Questions
1) **Trigger design**: How can smart contracts safely translate off-chain life events into on-chain execution?
   - What combinations of inactivity, attestations, and multi-party notices minimize false positives and abuse?
2) **Secure delivery**: What is the minimal on-chain footprint that still enables verifiable, privacy-preserving off-chain transfer?
   - How should encrypted bundles, hashes, and key-release policies be structured?
3) **Identity representation**: How can a person’s authorized textual traces be transformed into an interpretable “digital profile”
   that supports memorialization without misrepresenting intent?
   - Which linguistic features provide stable, human-understandable markers of voice?

## Method & Prototype
- Implement a minimal vault + registry skeleton on EVM to define the policy surface.
- Build an off-chain pipeline producing:
  - `persona_profile.json` (style + topics)
  - `portrait.md` (memorial portrait)
  - a deterministic style writer for bounded rewriting tasks
- Evaluate robustness with threat modeling and red-team scenarios (premature claim, storage tampering, sensitive prompts).

## Expected Contributions
- A modular protocol architecture separating **on-chain policy** from **off-chain encrypted content**
- A reproducible, ethics-bounded approach to identity representation aligned with privacy-by-design
- A foundation for extending to AA wallets, multi-chain assets, and stronger attestation mechanisms
