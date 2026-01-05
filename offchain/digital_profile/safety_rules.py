# Safety rules for posthumous representation / legacy delivery.
# These are *baseline* constraints; production systems should add more robust policies and logging.

BLOCKED_KEYWORDS = [
    "password",
    "private key",
    "seed phrase",
    "2fa",
    "authentication",
    "ssn",
    "bank account",
]

def is_safe(prompt: str) -> bool:
    p = (prompt or "").lower()
    return not any(k in p for k in BLOCKED_KEYWORDS)
