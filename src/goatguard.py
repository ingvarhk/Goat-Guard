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

def main():
    global operatingSystem

    print(console.cyan + "\n------- LOADING FILES AND SETTING UP -------\n" + console.reset)

#   Get OS
    if platform.system() == "Windows":
        operatingSystem = "Windows"
    else:
        operatingSystem = "Other"

    files.fileSetup()
    settings = files.getSettings()

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
                            if len(rawNumber) <= 16:
                                number = security.encryptStuff(rawNumber, key)
                                break
                            else:
                                console.warning("The number is over 16 digits long.")

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
                print("ADD - HELP:\n - l [login]\n - e [email]\n - c [credit card]\n - p [pc]\n - n [note]\n\nEXAMPEL:\n - add l\n - add p")

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

        elif userInput.startswith("get"):

            choice = userInput.replace("get ", "").replace("get", "")

            if choice == "" or choice.isspace():
                console.warning("Missing argument. Try 'get h' for help.")


            elif choice.startswith("l"):
                print(console.cyan + "\nGet login" + console.reset)
                items = files.getJsonFile("secure/logins.json", "logins")

                if not items == None:
                    number = 1

                    for login in items["logins"]:
                        print(console.pink + "[" + str(number) + "] " + console.reset + login["name"])
                        number += 1

                    if number != 1:
                        loginNumberInput = input("\nLogin number: ")

                        if loginNumberInput.isdigit() and loginNumberInput != "":
                            newNumber = 1
                            for login in items["logins"]:
                                if newNumber == int(loginNumberInput):
                                    print("")
                                    print("Web address: " + login["url"])
                                    if login["tag"] != "":
                                        print("Tag: " + login["tag"])
                                    print("Username: " + login["username"])
                                    print("Password: " + security.decryptStuff(login["password"], key).decode())
                                    print("")
                                newNumber += 1
                    else:
                        console.warning("No logins avaiable.\n")

            elif choice.startswith("e"):
                print(console.cyan + "\nGet email" + console.reset)

                items = files.getJsonFile("secure/emails.json", "emails")

                if not items == None:
                    number = 1
                    for email in items["emails"]:
                        print(console.pink + "[" + str(number) + "] " + console.reset + email["name"])
                        number += 1

                    if number != 1:
                        emailNumberInput = input("\nEmail number: ")
                        if emailNumberInput.isdigit() and emailNumberInput != "":
                            newNumber = 1

                            for email in items["emails"]:
                                if newNumber == int(emailNumberInput):
                                    print("")
                                    print("Email address: " + email["emailaddress"])
                                    if email["tag"] != "":
                                        print("Tag: " + email["tag"])
                                    print("Password: " + security.decryptStuff(email["password"], key).decode())
                                    print("")

                                newNumber += 1
                    else:
                        console.warning("No emails avaiable.\n")

            elif choice.startswith("c"):
                print(console.cyan + "\nGet credit card" + console.reset)

                items = files.getJsonFile("secure/creditcards.json", "creditcards")

                if not items == None:
                    number = 1
                    for card in items["creditcards"]:
                        print(console.pink + "[" + str(number) + "] " + console.reset + card["name"])
                        number += 1

                    if number != 1:
                        cardNumberInput = input("\nCard number: ")
                        if cardNumberInput.isdigit() and cardNumberInput != "":
                            newNumber = 1

                            for card in items["creditcards"]:
                                if newNumber == int(cardNumberInput):
                                    print("")
                                    print("Owner: " + card["owner"])
                                    print("Type: " + card["type"])
                                    print("Number: " + security.decryptStuff(card["number"], key).decode())
                                    print("CVC/CVV: " + security.decryptStuff(card["cvc/cvv"], key).decode())
                                    print("Expiry date: " + security.decryptStuff(card["expiry"], key).decode())
                                    print("")

                                newNumber += 1
                    else:
                        console.warning("No credit cards avaiable.\n")

            elif choice.startswith("p"):
                print(console.cyan + "\nGet computer" + console.reset)
                items = files.getJsonFile("secure/computers.json", "computers")

                if not items == None:
                    number = 1

                    for computer in items["computers"]:
                        print(console.pink + "[" + str(number) + "] " + console.reset + computer["name"])
                        number += 1

                    if number != 1:
                        pcNumberInput = input("\nComputer number: ")

                        if pcNumberInput.isdigit() and pcNumberInput != "":
                            newNumber = 1
                            for computer in items["computers"]:
                                if newNumber == int(pcNumberInput):
                                    print("")
                                    print("Computer name: " + computer["name"])
                                    if computer["tag"] != "":
                                        print("Tag: " + computer["tag"])
                                    print("Username: " + computer["username"])
                                    print("Password: " + security.decryptStuff(computer["password"], key).decode())
                                    print("")
                                newNumber += 1
                    else:
                        console.warning("No computers avaiable.\n")

            elif choice.startswith("n"):
                print(console.cyan + "\nGet note" + console.reset)
                items = files.getJsonFile("secure/notes.json", "notes")

                if not items == None:
                    number = 1

                    for note in items["notes"]:
                        print(console.pink + "[" + str(number) + "] " + console.reset + note["name"])
                        number += 1

                    if number != 1:
                        noteNumberInput = input("\nNote number: ")

                        if noteNumberInput.isdigit() and noteNumberInput != "":
                            newNumber = 1
                            for note in items["notes"]:
                                if newNumber == int(noteNumberInput):
                                    print("")
                                    print("Note name: " + note["name"])
                                    if note["tag"] != "":
                                        print("Tag: " + note["tag"])
                                    print("Content: " + security.decryptStuff(note["content"], key).decode())
                                    print("")
                                newNumber += 1
                    else:
                        console.warning("No notes avaiable.\n")

            elif choice.startswith("h"):
                print("GET - HELP:\n - l [login]\n - e [email]\n - c [credit card]\n - p [pc]\n - n [note]\n\nEXAMPEL:\n - get l\n - get p")

            else:
                console.warning("Unknown argument. Try 'get h' for help.")

        elif userInput == "remove":
            print("Remove")

        elif userInput == "help":
            print("""
COMMANDS
    add  - Options: l [login], e [email], c [credit card], p [computer], n [note]
    remove - Options: l [login], e [email], c [credit card], p [computer], n [note]
    get - Options: l [login], e [email], c [credit card], p [computer], n [note]

    gen - generate password - Arguments: <lenght>

    clear - clear screen
    info - info about Goat Guard
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
