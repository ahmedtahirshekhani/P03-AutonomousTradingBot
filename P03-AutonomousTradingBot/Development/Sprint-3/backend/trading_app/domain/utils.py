from hashlib import sha256
from uuid import uuid4
import psx

def hash_password(password: str) -> str:
    hashed_pass = str(sha256(password.encode("utf-8")).hexdigest())
    return hashed_pass

def get_random_id() -> str:
    return str(uuid4())

def get_latest_price(symbol: str) -> float:
    return psx.get_latest_price(symbol)
