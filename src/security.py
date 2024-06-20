import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

import random
import string

import console

def generatePassword(lenght):
    choose_from = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(choose_from, k=lenght))

def generateKey(masterPassword):

    hashed = hashlib.sha3_256(masterPassword.encode()).digest()
    #print("Hashed master password: " + str(hashed) + ". Length: " + str(len(hashed)))
    key = base64.urlsafe_b64encode(hashed)
    #print("Encryption/decryption key: " + key.decode())

    return key

def decryptStuff(toDecrypt, key):

    f = Fernet(key)
    try:
        decrypted = f.decrypt(toDecrypt.encode())
    except InvalidToken:
        decrypted = b"Access denied."

    return decrypted

def encryptStuff(toEncrypt, key):

    f = Fernet(key)
    encrypted = f.encrypt(toEncrypt.encode())

    return encrypted
