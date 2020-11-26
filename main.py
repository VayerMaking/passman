import config
import hashlib
import random
import enquiries
import json
import subprocess


with open('passwords.txt') as j:
    pass_dict = json.load(j)

with open('.machine_id', 'w') as f:
    process = subprocess.Popen(['cat', '/var/lib/dbus/machine-id'], stdout=f)


def add_password(pass_dict):
    print("enter a site name")
    new_site = str(input())
    print("ender the password")
    new_pass = str(input())
    hashed_pass = hash_password(new_pass)
    #pass_dict[len(pass_dict)+1] = hashed_pass
    pass_dict[new_site] = hashed_pass
    return pass_dict

def get_macine_id():
    process = subprocess.check_output(['cat', '/var/lib/dbus/machine-id'])
    result = str(process)
    result = result[:-3]
    result = result.replace("b'", '')
    return result

def load_machine_id():
    with open('.machine_id', 'r') as m:
        machine_id_loaded = m.read().replace('\n', '')
        #print("check", machine_id_loaded)
    m.close()
    return machine_id_loaded

def auth():
    if get_macine_id() == load_machine_id():
        return True

def hash_password(password):
    password += random.choice(wordlist)
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def save_new_passwords(pass_dict):
    with open("passwords.txt", 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(pass_dict))
        f.close()

def get_password(pass_dict):
    print("enter a site name")
    site_name = str(input())
    # add auth here with master password
    if auth() == True:
        try:
            return pass_dict[site_name]
        except KeyError:
            print("There is no {} site in your passman!".format(site_name))
    else:
        print("unsuccessful auth")


#string = str(input())
#wordlist = ["apple", "qwerty", "asdf"]
#print(string)

print(get_macine_id())
print(load_machine_id())
options = ['add a new password', 'get a password', 'set the machine_id(requires password)']
choice = enquiries.choose('Choose one of these options: ', options)
print("you chose:", choice)

if choice == options[0]:
    print("adding a new password")
    add_password(pass_dict)
    save_new_passwords(pass_dict)
elif choice == options[1]:
    print("getting your password")
    print(get_password(pass_dict))
elif choice == options[2]:
    print("setting machine_id")




#print(pass_dict.items())


#hashed_string = hash_password(string)

#print(hashed_string)
