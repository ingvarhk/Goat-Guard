import json
import os

def getJsonFile(path, category):
    if os.path.isfile(path):
        with open(path, "r") as f:
            content = f.read()
            print("INFO: Reading file " + path)

            try:
                jsonStuff = json.loads(content)
            except Exception as e:
                print("ERROR: No " + category + " avaiable. ")
                jsonStuff = "ERROR: No " + category + " avaiable"

            return jsonStuff
    else:
        print("WARNING: Couldn't find ", path)
        with open(path, "w") as f:

            toFille = {
                category: []

            }

            f.write(json.dumps(toFille))
            print("INFO: File " + path + " created")
            return toFille

def appendToJsonFile(path, category, new):

    with open(path, "r") as f:
        try:
            content = json.loads(f.read())
            try:
                content[category].append(new)
            except Exception as e:
                print("ERROR: Could not append new " + category.replace("s", ""))

        except Exception as e:
            print("ERROR: Could not load " + category)


    with open(path, "w") as f:
        try:
            f.write(json.dumps(content))
            print("INFO: New " + category.replace("s", "") + " added")

        except Exception as e:
            print("ERROR: Could not save to " + path)

def fileSetup():
    if not os.path.isdir("secure"):
        os.mkdir("secure")
        print("INFO: Folder 'secure' created")
    if not os.path.isdir("secure/files"):
        os.mkdir("secure/files")
        print("INFO: Folder 'secure/files' created")
    if not os.path.isdir("data"):
        os.mkdir("data")
        print("INFO: Folder 'data' created")
    if not os.path.isdir("data/ham"):
        os.mkdir("data/ham")
        print("INFO: Folder 'data/ham' created")

    with open("data/ham/pepper.txt", "w+") as f:
        f.write("Why do sharks swim in salt water?\nCause pepper water makes them sneeze!")


    files = []
    allFiles = ["secure/logins.json", "secure/emails.json", "secure/creditcards.json", "secure/notes.json"]

    for file in os.listdir('secure'):
        path = "secure/" + file

        if os.path.isfile(path):
            files.append(path)

            with open(path, "r") as f:
                content = f.read()
                print("INFO: Checking file " + path)

                try:
                    jsonStuff = json.loads(content)

                except Exception as e:
                    print("WARNING: Could not load file " + path)

                    with open(path, "w") as f:

                        toFile = {
                            file.replace('.json',''): []

                        }

                        f.write(json.dumps(toFile))
                        print("INFO: File " + path + " created")

    for file in files:
        for otherFile in allFiles:
            if file == otherFile:
                allFiles.remove(otherFile)

    for missingFile in allFiles:
        print("WARNING: Could not find file " + missingFile)

        with open(missingFile, "w") as f:

            toFile = {
                os.path.basename(missingFile).replace('.json',''): []

            }

            f.write(json.dumps(toFile))
            print("INFO: " + missingFile + " created")



def getSettings():
    if os.path.isfile("data/settings.json"):
        with open("data/settings.json", "r") as f:
            content = f.read()
            print("INFO: Reading file data/settings.json")

            return json.loads(content)
    else:
        print("WARNING: Could not find settings.json")
        with open("data/settings.json", "w") as f:

            toFile = {
              "newToGoatGuard": True,
              "developer": False
            }
            f.write(json.dumps(toFile))
            print("INFO: File data/settings.json created")
            return toFile

def setNewToFalseSettings():
    with open("data/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["newToGoatGuard"] = False

    with open("data/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

class Add:
    def login(name, favorite, tag, url, username, password):

        newLogin =  {
            "name": name,
            "favorite": favorite,
            "tag": tag,
            "url": url,
            "username": username,
            "password": password
        }

        appendToJsonFile("secure/logins.json", "logins", newLogin)

    def email(name, favorite, emailaddress, password, provider):

        newEmail =  {
            "name": name,
            "favorite": favorite,
            "emailaddress": emailaddress,
            "password": password,
            "provider": provider
        }

        appendToJsonFile("secure/emails.json", "emails", newEmail)

    def creditcard(name, favorite, owner, type, number, cvc, expire):

        newCreditcard =  {
            "name": name,
            "favorite": favorite,
            "owner": owner,
            "type": type,
            "number": number,
            "cvc": cvc,
            "expire": expire
        }

        appendToJsonFile("secure/creditcards.json", "creditcards", newCreditcard)

    def computer(name, favorite, username, password):

        newComputer =  {
            "name": name,
            "favorite": favorite,
            "username": username,
            "password": password
        }

        appendToJsonFile("secure/computers.json", "computers", newComputer)

    def note(name, favorite, content):

        newNote =  {
            "name": name,
            "favorite": favorite,
            "content": content
        }

        appendToJsonFile("secure/newNote.json", "notes", newNote)

    def file():
        print("Not working yet :(")
