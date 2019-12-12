import passwd
import files
import gui

import sys

def decryptPassword():
    passwd.decrypt()

def encryptPassword():
    passwd.encrypt()

def getService(type, searchFor):
    services = files.getServicesFile()
    for service in services["services"]:
        if service["type"] == "website":
            if service["webaddress"] == searchFor:
                return service
        elif service["type"] == "email":
            if service["email"] == searchFor:
                return service

def addService(type, webaddress, email, username, password):
    newService =  {
        "type": type,
        "webaddress": webaddress,
        "username": username,
        "email": email,
        "password": password
    }
    files.addToServicesFile(newService)

def main():
    print("\n------- LOADING FILES AND SETTING UP -------\n")

    setupFileContent = files.getSetupFile()
    servicesFileContent = files.getServicesFile()
    print("Finished.")

    print("\n------- GOAT GUARD -------\n")

    while True:
        userInput = input("## ")

        if userInput == "add":
            print("Add service")
            addService("Website", "google.com", "test@gmail.com", "", "qwerty")
        elif userInput == "remove":
            print("Remove service")
        elif userInput == "help":
            print("Help")
        elif userInput == "exit":
            print("Exiting..")
            sys.exit()

        else:
            print("Unvalid command. Try 'help'")

    #decryptPassword()
    #encryptPassword()

    #gui.window()

if __name__ == "__main__":
    print("Launching Goat Guard..")
    main()



#masterPasswordInput = input("Master password: ")
#key = passwd.generateKey(masterPasswordInput)
#print(key)
