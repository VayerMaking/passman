import config
import hashlib
import random
import enquiries

def add_password(pass_dict):
    new_pass = str(input())
    hashed_pass = hash_password(new_pass)
    pass_dict[len(pass_dict)+1] = hashed_pass
    return pass_dict

def hash_password(password):
    password += random.choice(wordlist)
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

wordlist = ["apple", "qwerty", "asdf"]
pass_dict = {"1" : "qwerty"}


options = ['add a new password', 'get a password']
choice = enquiries.choose('Choose one of these options: ', options)
print("you chose:", choice)

if choice == options[0]:
    print("adding a new password")
    add_password(pass_dict)
elif choice == options[1]:
    print("getting your password")




print(pass_dict.items())
