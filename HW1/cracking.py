import hashlib, itertools

hash = "61ef437ca1493baf5ce815a8ca13ec1fba31645f7d85edebac7c60e0aa98b5c6"

print(
    next(
        password
        for password in itertools.count()
        if hashlib.sha256(f"bucky,{password},20200128".encode()).hexdigest() == hash
    )
)

