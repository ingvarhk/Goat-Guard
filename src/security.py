import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

import random

import console

def generatePassword(lenght):
    chooseFrom = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    password = ""

    for i in range(0, lenght):
        password += random.choice(chooseFrom)

    return password

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
