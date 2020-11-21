import config
import hashlib
import random
<<<<<<< HEAD
import enquiries
import json

with open('passwords.txt') as j:
    pass_dict = json.load(j)

def add_password(pass_dict):
    print("enter a site name")
    new_site = str(input())
    print("ender the password")
    new_pass = str(input())
    hashed_pass = hash_password(new_pass)
    #pass_dict[len(pass_dict)+1] = hashed_pass
    pass_dict[new_site] = hashed_pass
    return pass_dict
=======

string = str(input())
wordlist = ["apple", "qwerty", "asdf"]
print(string)
>>>>>>> 38be06c5707d792a457d2599050b54c56ea33b1e

def hash_password(password):
    password += random.choice(wordlist)
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

<<<<<<< HEAD
def save_new_passwords(pass_dict):
    with open("passwords.txt", 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(pass_dict))
        f.close()

def get_password(pass_dict):
    print("enter a site name")
    site_name = str(input())
    # add auth here with master password
    return pass_dict[site_name])


wordlist = ["apple", "qwerty", "asdf"]


options = ['add a new password', 'get a password']
choice = enquiries.choose('Choose one of these options: ', options)
print("you chose:", choice)

if choice == options[0]:
    print("adding a new password")
    add_password(pass_dict)
    save_new_passwords(pass_dict)
elif choice == options[1]:
    print("getting your password")
    get_password(pass_dict)




print(pass_dict.items())
=======
hashed_string = hash_password(string)

print(hashed_string)
>>>>>>> 38be06c5707d792a457d2599050b54c56ea33b1e
