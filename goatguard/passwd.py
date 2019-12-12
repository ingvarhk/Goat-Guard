import bcrypt
#from cryptography import Fernet

def generateKey(masterPassword):
    salt = b'$2b$12$TdPNd/2AOHaqBIZTjzHEFe93486..3434(erh84-23?__hEC7293jdhe&'
    key = bcrypt.hashpw(masterPassword.encode(), salt)
    return key

def decrypt():
    print("decrypting")

def encrypt():
    print("encrypting")
