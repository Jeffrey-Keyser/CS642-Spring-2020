# Part A:

## Recovered password

11235813

## Pseudocode for attack

```py
import hashlib
import itertools


def hash(m):
    return hashlib.sha256(m.encode()).hexdigest()

expected = "61ef437ca1493baf5ce815a8ca13ec1fba31645f7d85edebac7c60e0aa98b5c6"
print(next(p for p in itertools.count() if hash(f"bucky,{p},20200128") == expected))
```

## Worst case running time

## Discussion merits of current proposal

## Suggestions for improvement


# Part B:

## Discussion of the current scheme

## Suggestions for improving the scheme


# Extra Credit:

## Recovered password

## Correct pseudocode

