import bcrypt
from cryptography.fernet import Fernet

def genSaltAndSave():
    salt = bcrypt.gensalt()

    with open("data/ham/salt.txt", "wb+") as f:
        f.write(salt)

def generateKey(masterPassword):

    with open("data/ham/salt.txt", "rb") as f:
        salt = f.read()

    key = bcrypt.hashpw(masterPassword.encode(), salt)
    return key

def decrypt(key):
    print("decrypting")

def encrypt(key):
    print("encrypting")
