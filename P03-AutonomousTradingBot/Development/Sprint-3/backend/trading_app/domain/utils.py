from hashlib import sha256
from uuid import uuid4

def hash_password(password: str) -> str:
    hashed_pass = str(sha256(password.encode("utf-8")).hexdigest())
    return hashed_pass

def get_random_id() -> str:
    return str(uuid4())