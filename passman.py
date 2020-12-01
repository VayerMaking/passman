import hashlib
import random
import enquiries
import json
import subprocess
import scrypt, os, binascii
from Crypto.Cipher import AES



def encrypt_password(password, key):
    print("pass", type(password))
    password = password.encode('utf8')
    print("pass", type(password))
    kdfSalt = os.urandom(16)
    secretKey = scrypt.hash(key, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(password)
    print((kdfSalt, ciphertext, aesCipher.nonce, authTag))
    return (kdfSalt, ciphertext, aesCipher.nonce, authTag)

def decrypt_password(encrypted_password, key):
    kdfSalt, ciphertext, nonce, authTag = encrypted_password.decode('utf8')
    secretKey = scrypt.hash(key, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


def load_passwords():
    try:
        with open('passwords.txt') as j:
            pass_dict = json.load(j)
        return pass_dict
    except json.decoder.JSONDecodeError:
        pass_dict = {}
        return pass_dict


def add_password(pass_dict):
    print("enter a site name")
    new_site = str(input())
    print("ender the password")
    new_pass = str(input())
    master_pass = get_master_password().encode('utf-8')
    #pass_dict[len(pass_dict)+1] = hashed_pass
    #pass_dict[new_site] = str(hashed_pass)
    hashed_pass = encrypt_password(new_pass, master_pass)
    result =  (binascii.hexlify(hashed_pass[0]).decode('utf8'),binascii.hexlify(hashed_pass[1]).decode('utf8'),binascii.hexlify(hashed_pass[2]).decode('utf8'),binascii.hexlify(hashed_pass[3]).decode('utf8'))
    #print("redsult", result)
    #print(type(hashed_pass))
    #for i in result:
        #print(type(i))
    #    i = i.decode('utf8')
    #    print(i)
    #print("redsult decoded", result)

    pass_dict.update({new_site: result})
    return pass_dict

def get_machine_id():
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
    if get_machine_id() == load_machine_id():
        return True

def hash_password(password):
    #password += random.choice(wordlist)
    password += get_master_password()
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def set_machine_id():
    with open('.machine_id', 'w') as f:
        process = subprocess.Popen(['cat', '/var/lib/dbus/machine-id'], stdout=f)

def save_new_passwords(pass_dict):
    print(pass_dict)
    with open("passwords.txt", 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(pass_dict))
        f.close()

def get_password(pass_dict):
    print("enter a site name")
    site_name = str(input())
    # add auth here with master password
    if auth() == True:
        try:
            master_pass = get_master_password().encode('utf-8')
            password = decrypt_password(pass_dict[site_name], master_pass)
            return password
        except KeyError:
            print("There is no {} site in your passman!".format(site_name))
    else:
        print("unsuccessful auth")

def create_master_password():
    if os.stat('.master_pass').st_size==0:
        print("avaiable")
        master_pass = str(input())
        with open('.master_pass', 'w') as f:
            f.write(master_pass)
            f.close()
    else:
        print("you have already set a master password")

def get_master_password():
    with open('.master_pass', 'r') as f:
        master_pass = f.read().replace('\n', '')
        f.close()
        print(type(master_pass))
    return master_pass
