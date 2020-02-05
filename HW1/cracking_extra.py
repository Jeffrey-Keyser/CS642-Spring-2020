import hashlib
import itertools
import multiprocessing as mp
import tqdm


def hash(m):
    h = m.encode()
    for i in range(256):
        h = hashlib.sha256(h).digest()
    return h.hex()


expected = "5483d76bc214a60e35a8a068a28912c168ea5aea8d1441559e3568135185d636"
assert hash("ironman,password,84829348943") == expected


expected = "1b2ebfab6e70dcb13f3ff4750d065bab8474dac4dc611df339446071ae3e7977"

def try_password(p):
    if hash(f"bucky,{p},8934029034") == expected:
        return p

# # Downloaded from https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm
with mp.Pool() as p, open("crackstation-human-only.txt", errors="ignore") as f:
    print(next(password for password in p.imap_unordered(try_password, f) if password)