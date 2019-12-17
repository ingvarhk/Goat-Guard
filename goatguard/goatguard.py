import security
import files
import gui

from getpass import getpass
import os, sys, platform

# CATEGORIES: Login, Email, Credit Card, Computer, Note, File
# TAGS (Login only): Social Media, Entertainment, Travel, Shopping, Other

# Login: Name, Favorite, Tag, URL, Username, Password
# Email: Name, Favorite, Emailaddress, Password, Provider
# Credit Card: Name, Favorite, Owner, Type, Number, CVC, Expire
# Computer: Name, Favorite, Username, Password
# Note: Name, Favorite, Favorite, Content
# File: Name, Favorite, Size, Preview, Date, Content

def clearScreen():
    global operatingSystem

    if operatingSystem == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def newToGoatGuard():

    passwordMatch = True

    while True:

        clearScreen()
        print("------- NEW TO GOAT GUARD -------\n")
        print("Before going bananas you will have to create a master password.\nThis will be hashed and used as a key for encrypting/decrypting passwords.\n")

        if not passwordMatch:
            print("WARNING: Passwords does not match. Try again.\n")

        passwordInput = getpass("Master password: ")
        passwordInputRepeat = getpass("Repeat: ")

        if passwordInput == passwordInputRepeat:
            print("Succes! The passwords are matching.\n")
            break
        else:
            passwordMatch = False

    files.setNewToFalseSettings()

def setup():
    global settings

    files.fileSetup()
    settings = files.getSettings()

    clearScreen()

    if settings["newToGoatGuard"] == True:
        security.genSaltAndSave()
        print("INFO: Salt genrated.")

        newToGoatGuard()

def getItem(path, name):

    category = os.path.basename(path).replace(".json", "")

    try:
        content = files.getJsonFile(path, category)

        for item in content[category]:
            if item["name"] == name:
                    return item
        print("WARNING: Could not find " + name)
    except:
        pass

def main():
    global operatingSystem
    print("\n------- LOADING FILES AND SETTING UP -------\n")

    if platform.system() == "Windows":
        operatingSystem = "Windows"
    else:
        operatingSystem = "Other"

    setup()


    print("------- GOAT GUARD -------\n")

    masterpassword = getpass("Master password: ")
    print("Loading...")
    key = security.generateKey(masterpassword)

    while True:
        userInput = input("## ")

        if userInput == "add":

            files.Add.login("Exampel", True, "Shopping", "login.exampel.com", "testUsername", "1234")
            #files.Add.email("My email", False, "test@exampel.com", "qwerty", "gmail")

        elif userInput == "get":
            print(getItem("secure/logins.json", "Exampel"))

        elif userInput == "remove":
            pass

        elif userInput == "help":
            print("""
COMMANDS
    add - new login, email, creditcard, note or file
    remove - delete login, email, creditcard, note or file
    get - get login, email, creditcard, note or file

    clear - clear screen
    exit - exit goat guard
INFO
    Made by Ingvar Hahn Kristensen 2019
    Website: http://ingvar.xyz
            """)

        elif userInput == "clear":
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')

        elif userInput == "exit":
            print("Exiting..")
            sys.exit()

        elif userInput == "" or userInput.isspace():
            pass
        else:
            print("WARNING: Unvalid command. Try 'help'")

    #decryptPassword()
    #encryptPassword()

    #gui.window()

if __name__ == "__main__":
    print("Launching Goat Guard..")
    main()



#masterPasswordInput = input("Master password: ")
#key = passwd.generateKey(masterPasswordInput)
#print(key)
