import passwd
import json

masterPasswordInput = input("Master password: ")
key = passwd.generateKey(masterPasswordInput)
print(key)
