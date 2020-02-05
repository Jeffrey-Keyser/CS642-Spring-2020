import hashlib
import itertools


def hash(m):
    return hashlib.sha256(m.encode()).hexdigest()


expected = "c50603be4fedef7a260ef9181a605c27d44fe0f37b3a8c7e8dbe63b9515b8e96"
assert hash("user,12345,999999") == expected

expected = "61ef437ca1493baf5ce815a8ca13ec1fba31645f7d85edebac7c60e0aa98b5c6"
print(next(p for p in itertools.count() if hash(f"bucky,{p},20200128") == expected))

# password is 11235813
