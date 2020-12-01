import config
import hashlib
import random
import enquiries
import json
import os
import subprocess
from simplecrypt import encrypt, decrypt
import passman

if passman.load_passwords() != None:
    pass_dict = passman.load_passwords()
else:
    pass_dict = {}



options = [ 'get a password', 'add a new password', 'set the machine_id(requires password)', 'create master password']
choice = enquiries.choose('Choose one of these options: ', options)
print("you chose:", choice)

if choice == options[0]:
    print("getting your password")
    print(passman.get_password(pass_dict))
elif choice == options[1]:
    print("adding a new password")
    passman.add_password(pass_dict)
    passman.save_new_passwords(pass_dict)
elif choice == options[2]:
    print("setting machine_id")
    passman.set_machine_id()
elif choice == options[3]:
    print("creating master password")
    passman.create_master_password()
