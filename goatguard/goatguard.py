import security
import files
import gui
import console

import validators
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

def setup():
    global settings

    files.fileSetup()
    settings = files.getSettings()

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

#   Get OS
    if platform.system() == "Windows":
        operatingSystem = "Windows"
    else:
        operatingSystem = "Other"

    setup()

#   Get Master password
    print(console.cyan + "\n------- MASTER PASSWORD -------\n" + console.reset)

    print("The master password will be used to encrypt/decrypt.")
    key = security.generateKey(getpass("Master password: "))
    console.info("Key generated.")

#   Ready
    print(console.cyan + "\n------- GOAT GUARD -------\n" + console.reset)

    while True:
        userInput = input(console.pink + "## " + console.reset)

        if userInput.startswith("add"):

            choice = userInput.replace("add ", "").replace("add", "")

            if choice == "" or choice.isspace():
                console.warning("Missing argument. Try 'add help'")

            elif choice.startswith("l"):
                print(console.cyan + "\nAdd login" + console.reset)

                while True:
                    username = input("- Username: ")
                    if username == "" or username.isspace():
                        console.warning("You must enter a username.")
                    else:
                        break

                rawPassword = getpass("- Password (enter for auto): ")
                if rawPassword == "":
                    rawPassword = security.generatePassword(10)

                password = security.encryptStuff(rawPassword, key)


                while True:
                    url = input("- Web address: ")
                    if url == "" or url.isspace():
                        console.warning("You must enter a web address.")
                    else:
                        if not url.startswith("http://") and not url.startswith("https://"):
                            url = "http://" + url

                        if not validators.url(url):
                            console.warning("Not a valid web address.")
                        else:
                            break

                tag = input("- Tag (optional): ")

                print("")
                files.Add.login(url, tag, url, username, password.decode())

            elif choice.startswith("e"):
                print(console.cyan + "\nAdd email" + console.reset)

                while True:
                    emailaddress = input("- Email address: ")
                    if emailaddress == "" or emailaddress.isspace():
                        console.warning("You must enter a email address.")
                    else:
                        if not validators.email(emailaddress):
                            console.warning("Not a valid email address.")
                        else:
                            break

                rawPassword = getpass("- Password (enter for auto): ")
                if rawPassword == "":
                    rawPassword = security.generatePassword(10)

                password = security.encryptStuff(rawPassword, key)

                tag = input("- Tag (optional): ")
                provider = emailaddress.split("@",1)[1]

                print("")

                files.Add.email(emailaddress, tag, emailaddress, password.decode(), provider)

            elif choice.startswith("c"):
                print(console.cyan + "\nAdd credit card" + console.reset)

                while True:
                    owner = input("- Owner: ")
                    if owner == "" or owner.isspace():
                        console.warning("You must enter a owner.")
                    else:
                        break

                while True:
                    rawNumber = input("- Number (no spaces): ")
                    if rawNumber == "" or rawNumber.isspace():
                        console.warning("You must enter a number.")
                    else:
                        if rawNumber.isdigit():
                            if len(rawNumber) == 16:
                                number = security.encryptStuff(rawNumber, key)
                                break
                            else:
                                console.warning("The number is not 16 digits long.")

                        else:
                            console.warning("No letters. Only digits.")

                while True:
                    rawCvcOrCvv = input("- CVC/CVV: ")
                    if rawCvcOrCvv == "" or rawCvcOrCvv.isspace():
                        console.warning("You must enter a CVC or a CVV.")
                    else:
                        if rawCvcOrCvv.isdigit():
                            if len(rawCvcOrCvv) == 4 or len(rawCvcOrCvv) == 3:
                                cvcOrCvv = security.encryptStuff(rawCvcOrCvv, key)
                                break
                            else:
                                console.warning("The CVC/CVV is not 3/4 digits long.")
                        else:
                            console.warning("No letters. Only digits.")

                while True:
                    rawExpiry = input("- Expiry date (e.g. 03/21): ")
                    if rawExpiry == "" or rawExpiry.isspace():
                        console.warning("You must enter a expiry date.")
                    else:
                        if len(rawExpiry) == 5:
                            if "/" in rawExpiry:
                                expiry = security.encryptStuff(rawExpiry, key)
                                break
                            else:
                                console.warning("The expiry date is not valid.")
                        else:
                            console.warning("The expiry date is not valid.")



                type = input("- Type (e.g. Mastercard): ")

                print("")
                files.Add.creditcard(type + " - " + owner, "", owner, type, number.decode(), cvcOrCvv.decode(), expiry.decode())

            elif choice.startswith("p"):
                print(console.cyan + "\nAdd Computer" + console.reset)

                while True:
                    name = input("- Computer name: ")
                    if name == "" or name.isspace():
                        console.warning("You must enter a computer name.")
                    else:
                        break

                while True:
                    username = input("- Username: ")
                    if username == "" or username.isspace():
                        console.warning("You must enter a username.")
                    else:
                        break

                rawPassword = getpass("- Password (enter for auto): ")
                if rawPassword == "":
                    rawPassword = security.generatePassword(10)

                password = security.encryptStuff(rawPassword, key)
                tag = input("- Tag (optinal): ")

                print("")
                files.Add.computer(name, tag, username, password.decode())

            elif choice.startswith("n"):
                print(console.cyan + "\nAdd secret note" + console.reset)

                while True:
                    name = input("- Name: ")
                    if name == "" or name.isspace():
                        console.warning("You must enter a name.")
                    else:
                        break

                tag = input("- Tag (optinal): ")

                rawContent = input("- Content: ")
                content = security.encryptStuff(rawContent, key)

                print("")
                files.Add.note(name, tag, content.decode())

            elif choice.startswith("h"):
                print("- l, login\n- e, email\n- c, credit card\n- p, pc\n- n, note")

            else:
                console.warning("Unknown argument. Try 'add h' for help.")




        elif userInput.startswith("gen"):
            lenght = userInput.replace("gen ", "").replace("gen", "")
            if not lenght == "" and not lenght.isspace():
                if lenght.isdigit():
                    print(security.generatePassword(int(lenght)))
                else:
                    console.warning("Argument is not integer.")
            else:
                console.warning("Missing argument. This requires a number as argument.")

        elif userInput == "get":
            #path input()
            pass

        elif userInput == "remove":
            print("Remove")

        elif userInput == "help":
            print("""
COMMANDS
    add - login, email, credit card, note or file
    remove - delete login, email, creditcard, note or file
    get - get login, email, creditcard, note or file

    gen - genrate password

    clear - clear screen
    exit - exit goat guard
""")

        elif userInput == "info":
            print("""
INFO
    Made by Ingvar Hahn Kristensen 2019
    Website: \033[4mhttp://ingvar.xyz\u001b[0m
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
            console.warning("Exiting..")
            sys.exit()

        elif userInput == "" or userInput.isspace():
            pass

        else:
            console.warning("Unvalid command '" + userInput + "'. Try 'help'.")

if __name__ == "__main__":
    print("Launching Goat Guard..")
    main()
