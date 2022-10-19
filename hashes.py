import hashlib
from Crypto.Hash import RIPEMD160


def sha256hash(string: str) -> str:
    bytes = string.encode('utf-8')
    hash = hashlib.sha256(bytes)
    return hash.hexdigest()


def ripemd160hash(string: str) -> str:
    hash = RIPEMD160.new()
    bytes = string.encode('utf-8')
    hash.update(bytes)
    return hash.hexdigest()
