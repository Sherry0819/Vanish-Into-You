# Design Overview

Vanish Into You splits the problem into two layers:

1) **On-chain policy + execution** (when and to whom)
2) **Off-chain encrypted delivery + representation** (what and how)

## On-chain Layer
- `InheritanceVault`: liveness checks, claim initiation, challenge window, execution
- `LegacyRegistry`: stores encrypted bundle pointers + emits access-release events

## Off-chain Layer
- Legacy bundles are encrypted locally.
- Decryption keys are released (as encrypted keys per beneficiary) when the vault executes.
- `Digital Profile` builds an interpretable portrait and a style writer from authorized text.

## Trust & Safety
- Challenge windows prevent immediate malicious execution.
- Off-chain files are never stored in plaintext on-chain.
- The Digital Profile module does **not** claim consciousness replication.
