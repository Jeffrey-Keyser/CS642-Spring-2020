#!/usr/bin/python3

# SBATCH -p wacc
# SBATCH -J cs642
# SBATCH -o cs642.out -e cs642.err
# SBATCH -n 32

import hashlib
import os
import sys
import tqdm

import multiprocessing as mp


def hash(m):
    h = m.encode()
    for i in range(256):
        h = hashlib.sha256(h).digest()
    return h.hex()


expected = "5483d76bc214a60e35a8a068a28912c168ea5aea8d1441559e3568135185d636"
assert hash("ironman,password,84829348943") == expected

filename = "crackstation.txt"
file_size = os.path.getsize(filename)


def try_password(start, size):
    with open(filename, errors="ignore") as f:
        f.seek(start)
        for p in f.readlines(size):
            if (
                hash(f"bucky,{p},8934029034")
                == "1b2ebfab6e70dcb13f3ff4750d065bab8474dac4dc611df339446071ae3e7977"
            ):
                print(f"====================== {p} ==================")


def chunkify(size):
    with open(filename, errors="ignore") as f:
        end = f.tell()
        while True:
            start = end
            f.seek(start + size)
            f.readline()
            end = f.tell()
            yield start, end - start
            if end > file_size:
                break


pool = mp.Pool(1)
jobs = []
chunks = list(chunkify(size=64 << 10))
pbar = tqdm.tqdm(total=len(chunks))


def log_result(result):
    pbar.update(1)


for start, size in chunks:
    jobs.append(pool.apply_async(try_password, (start, size), callback=log_result))

pool.close()
pool.join()

