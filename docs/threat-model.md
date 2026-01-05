# Threat Model (High-level)

## Adversaries
- Malicious beneficiary attempting premature execution
- Colluding guardians/beneficiaries
- Compromised devices of the owner
- Compromised off-chain storage (IPFS gateway, cloud account)
- Attester corruption (if attestation triggers are enabled)

## Key Risks & Mitigations
1) **Premature claim** → challenge window + owner cancellation + optional bonds/slashing (future work)
2) **Key leakage** → encrypt bundles; never store plaintext secrets on-chain
3) **Storage tampering** → store content hash on-chain; verify off-chain before decrypting
4) **Hallucinated persona output** → interpretability-first profile + source-bounded generation
