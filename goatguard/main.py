import passwd
import json
import setup

masterPasswordInput = input("Master password: ")
key = passwd.generateKey(masterPasswordInput)
print(key)
