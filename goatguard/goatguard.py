import passwd
import files
import gui

def decryptPassword():
    passwd.decrypt()

def encryptPassword():
    passwd.encrypt()

def getService(type, searchFor):
    services = files.getServicesFile()
    for service in services["services"]:
        if service["type"] == "website":
            if service["website"] == searchFor:
                return service
        elif service["type"] == "email":
            if service["email"] == searchFor:
                return service

def addService(type, webaddress, email, username, password):


def main():

    print(getService("website", "google.com"))

    #setupContent = files.getSetupFile()

    #decryptPassword()
    #encryptPassword()

    #gui.window()

if __name__ == "__main__":
    print("Launching Goat Guard..")
    main()



#masterPasswordInput = input("Master password: ")
#key = passwd.generateKey(masterPasswordInput)
#print(key)
