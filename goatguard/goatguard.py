import security
import files
import gui
import console

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

        print(console.cyan + "\n------- NEW TO GOAT GUARD -------\n" + console.reset)
        print("Before going bananas you will have to create a master password.\nThis will be hashed and used as a key for encrypting/decrypting passwords.\n")

        if not passwordMatch:
            console.warning("Passwords does not match. Try again.\n")

        passwordInput = getpass("Master password: ")
        passwordInputRepeat = getpass("Repeat: ")

        if passwordInput == passwordInputRepeat:
            console.info("Succes! The passwords are matching.")
            break
        else:
            passwordMatch = False

    files.setNewToFalseSettings()

def setup():
    global settings

    files.fileSetup()
    settings = files.getSettings()

    if settings["newToGoatGuard"] == True:
        newToGoatGuard()

def getItem(path, name):

    category = os.path.basename(path).replace(".json", "")

    try:
        content = files.getJsonFile(path, category)

        for item in content[category]:
            if item["name"] == name:
                    return item
        console.warning("Could not find " + name)
    except:
        pass

def main():
    global operatingSystem
    print(console.cyan + "\n------- LOADING FILES AND SETTING UP -------\n" + console.reset)

    if platform.system() == "Windows":
        operatingSystem = "Windows"
    else:
        operatingSystem = "Other"

    setup()

    print(console.cyan + "\n------- GOAT GUARD -------\n" + console.reset)

    #gui.test()

    key = security.generateKey(getpass("Master password: "))

    while True:
        userInput = input("## ")

        if userInput == "add":
            print(console.pink + "[1]" + console.reset + " - Login\n" + console.pink + "[2]" + console.reset + " - Email\n" + console.pink + "[3]" + console.reset + " - Credit Card\n" + console.pink + "[4]" + console.reset + " - Computer\n" + console.pink + "[5]" + console.reset + " - Note")
            addType = input("What do you choose: ")

            password = security.encryptStuff("hej", key)

            files.Add.login("Exampel", True, "Shopping", "login.exampel.com", "testUsername", password)
            #files.Add.email("My email", False, "test@exampel.com", "qwerty", "gmail")

        elif userInput == "get":
            print("Get")
            #getItem("secure/logins.json", "Exampel")

        elif userInput == "remove":
            print("Remove")

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
            clearScreen()

        elif userInput == "test":
            #print("\nEncryption/decryption key: " + key.decode())
            print("--------------------------")
            testInput = input("What do you want to encrypt? ")
            encrypted = security.encryptStuff(testInput, key)

            print("Encrypted: " + encrypted.decode())

            testInput2 = input("What do you want to decrypt? ")

            decrypted = security.decryptStuff(testInput2.encode(), key)
            print("Decrypted: " + decrypted.decode())
            print("--------------------------\n")

        elif userInput == "exit":
            print("Exiting..")
            sys.exit()

        elif userInput == "" or userInput.isspace():
            pass
        else:
            console.warning("Unvalid command. Try 'help'")

    #decryptPassword()
    #encryptPassword()

    #gui.window()

if __name__ == "__main__":
    print("Launching Goat Guard..")
    main()



#masterPasswordInput = input("Master password: ")
#key = passwd.generateKey(masterPasswordInput)
#print(key)
