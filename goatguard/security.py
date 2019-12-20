import bcrypt
import hashlib
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import base64
import os

def generateKey(masterPassword):

    hashed = hashlib.sha256(masterPassword.encode()).digest()
    #print("Hashed master password: " + str(hashed) + ". Length: " + str(len(hashed)))

    key = base64.urlsafe_b64encode(hashed)
    #print("Encryption/decryption key: " + key.decode())

    return key

def decryptStuff(toDecrypt, key):
    print("INFO: Decrypting..")

    f = Fernet(key)
    try:
        decrypted = f.decrypt(toDecrypt)
    except InvalidToken:
        print("WARNING: Could not decrypt. Wrong key.")
        decrypted = b"Wrong key."

    return decrypted

def encryptStuff(toEncrypt, key):
    print("INFO: Encrypting..")

    f = Fernet(key)
    encrypted = f.encrypt(toEncrypt.encode())

    return encrypted
