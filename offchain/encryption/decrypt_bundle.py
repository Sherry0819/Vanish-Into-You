from __future__ import annotations
import argparse, base64
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="Encrypted bundle file (nonce+ciphertext)")
    ap.add_argument("--key", required=True, help="Base64 key file")
    ap.add_argument("--out", required=True, help="Output path for decrypted plaintext")
    args = ap.parse_args()

    blob = Path(args.inp).read_bytes()
    nonce, ct = blob[:12], blob[12:]
    key = base64.b64decode(Path(args.key).read_text(encoding="utf-8").strip())
    aes = AESGCM(key)
    pt = aes.decrypt(nonce, ct, associated_data=None)
    Path(args.out).write_bytes(pt)
    print("Decrypted bundle written.")

if __name__ == "__main__":
    main()
