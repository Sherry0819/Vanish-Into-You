from __future__ import annotations
import argparse, os, base64, json
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="Path to plaintext bundle file (e.g., legacy_bundle.json)")
    ap.add_argument("--out", required=True, help="Output path for encrypted bytes")
    ap.add_argument("--key-out", required=True, help="Output path for base64 key (demo; in practice encrypt per beneficiary)")
    args = ap.parse_args()

    pt = Path(args.inp).read_bytes()
    key = AESGCM.generate_key(bit_length=256)
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ct = aes.encrypt(nonce, pt, associated_data=None)

    Path(args.out).write_bytes(nonce + ct)
    Path(args.key_out).write_text(base64.b64encode(key).decode("utf-8"), encoding="utf-8")
    print("Encrypted bundle written. (Demo key saved; do NOT store raw keys in production.)")

if __name__ == "__main__":
    main()
