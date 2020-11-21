import config
import hashlib
import random

string = str(input())
wordlist = ["apple", "qwerty", "asdf"]
print(string)

def hash_password(password):
    password += random.choice(wordlist)
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

hashed_string = hash_password(string)

print(hashed_string)
