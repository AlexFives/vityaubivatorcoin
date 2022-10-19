import time
import base58
import ecdsa
from typing import Tuple

from hashes import sha256hash, ripemd160hash


def generate_pkh(secret: str = None) -> str:
    if secret is None:
        secret = str(time.time())
    sha256_hashed_secret = sha256hash(secret)
    pkh = ripemd160hash(sha256_hashed_secret)
    return pkh


def generate_keys_pair() -> Tuple[str, str]:
    ...


def base58encode(string: str) -> str:
    bytes_ = string.encode('utf-8')
    encoded = base58.b58encode(bytes_)
    return encoded.decode('utf-8')


def base58decode(string: str) -> str:
    bytes = string.encode('utf-8')
    decoded = base58.b58decode(bytes)
    return decoded.decode('utf-8')
