from Crypto.Cipher import AES
import scrypt, os, binascii

def encrypt_AES_GCM(msg, password):
    print("pass", type(msg))
    kdfSalt = os.urandom(16)
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (kdfSalt, ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, password):
    (kdfSalt, ciphertext, nonce, authTag) = encryptedMsg
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext
asdf = "asdf"
msg = asdf.encode('utf-8')
with open('.master_pass', 'r') as f:
    master_pass = f.read().replace('\n', '')
    f.close()
password = master_pass.encode('UTF-8')
encryptedMsg = encrypt_AES_GCM(msg, password)
print("encryptedMsg", {
    'kdfSalt': binascii.hexlify(encryptedMsg[0]),
    'ciphertext': binascii.hexlify(encryptedMsg[1]),
    'aesIV': binascii.hexlify(encryptedMsg[2]),
    'authTag': binascii.hexlify(encryptedMsg[3])
})

decryptedMsg = decrypt_AES_GCM(encryptedMsg, password)
print("decryptedMsg", decryptedMsg)
