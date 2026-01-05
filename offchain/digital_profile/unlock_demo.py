"""Demo: simulate 'unlock after inheritance execution'

In a full system, beneficiaries would listen to on-chain `AccessReleased` events from `LegacyRegistry`
and then retrieve/decrypt the legacy bundle off-chain.

This script demonstrates the local steps:
1) Encrypt the sample bundle (writes encrypted bytes + demo key file)
2) Decrypt it back (verifies round-trip)
"""

from pathlib import Path
import subprocess, sys

def main():
    enc_dir = Path("reports")
    enc_dir.mkdir(parents=True, exist_ok=True)

    bundle = "data/sample/legacy_bundle.json"
    enc_out = "reports/legacy_bundle.enc"
    key_out = "reports/demo_key_b64.txt"
    dec_out = "reports/legacy_bundle.decrypted.json"

    subprocess.check_call([sys.executable, "offchain/encryption/encrypt_bundle.py", "--in", bundle, "--out", enc_out, "--key-out", key_out])
    subprocess.check_call([sys.executable, "offchain/encryption/decrypt_bundle.py", "--in", enc_out, "--key", key_out, "--out", dec_out])

    print("Unlock demo complete. See reports/")

if __name__ == "__main__":
    main()
