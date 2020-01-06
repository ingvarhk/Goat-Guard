import json
import os
import console

def getJsonFile(path, category):
    if os.path.isfile(path):
        with open(path, "r") as f:
            content = f.read()
            #console.info("Reading file " + path)

            try:
                jsonStuff = json.loads(content)
            except Exception as e:
                console.error("No " + category + " avaiable. ")
                jsonStuff = None

            return jsonStuff
    else:
        console.warning("Couldn't find " + str(path))
        with open(path, "w") as f:

            toFille = {
                category: []

            }

            f.write(json.dumps(toFille))
            console.info("File " + path + " created")
            return toFille

def appendToJsonFile(path, category, new):

    with open(path, "r") as f:
        try:
            content = json.loads(f.read())
            try:
                content[category].append(new)
            except Exception as e:
                console.error("Could not append new " + category.replace("s", ""))

        except Exception as e:
            console.error("Could not load " + category)


    with open(path, "w") as f:
        try:
            f.write(json.dumps(content))
            console.info("New " + category.replace("s", "") + " added")

        except Exception as e:
            console.error("Could not save to " + path)

def fileSetup():
    if not os.path.isdir("secure"):
        os.mkdir("secure")
        console.info("Folder 'secure' created")
    if not os.path.isdir("secure/files"):
        os.mkdir("secure/files")
        console.info("Folder 'secure/files' created")
    if not os.path.isdir("data"):
        os.mkdir("data")
        console.info("Folder 'data' created")


    files = []
    allFiles = ["secure/logins.json", "secure/computers.json", "secure/emails.json", "secure/creditcards.json", "secure/notes.json"]

    for file in os.listdir('secure'):
        path = "secure/" + file

        if os.path.isfile(path):
            files.append(path)

            with open(path, "r") as f:
                content = f.read()
                console.info("Checking file " + path)

                try:
                    jsonStuff = json.loads(content)

                except Exception as e:
                    console.warning("Could not load file " + path)

                    with open(path, "w") as f:
                        toFile = {
                            file.replace('.json',''): []

                        }

                        f.write(json.dumps(toFile))
                        console.info("File " + path + " created")

    for file in files:
        for otherFile in allFiles:
            if file == otherFile:
                allFiles.remove(otherFile)

    for missingFile in allFiles:
        console.warning("Could not find file " + missingFile)

        with open(missingFile, "w") as f:

            toFile = {
                os.path.basename(missingFile).replace('.json',''): []

            }

            f.write(json.dumps(toFile))
            console.info("File " + missingFile + " created")



def getSettings():
    if os.path.isfile("data/settings.json"):
        with open("data/settings.json", "r") as f:
            content = f.read()
            console.info("Reading file data/settings.json")

            return json.loads(content)
    else:
        console.warning("Could not find settings.json")
        with open("data/settings.json", "w") as f:

            toFile = {
              "developer": False
            }
            f.write(json.dumps(toFile))
            console.info("File data/settings.json created")
            return toFile

def setNewToFalseSettings():
    with open("data/settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["newToGoatGuard"] = False

    with open("data/settings.json", "w") as jsonFile:
        json.dump(data, jsonFile)

class Add:
    def login(name, tag, url, username, password):

        newLogin =  {
            "name": name,
            "tag": tag,
            "url": url,
            "username": username,
            "password": password
        }

        appendToJsonFile("secure/logins.json", "logins", newLogin)

    def email(name, tag, emailaddress, password, provider):

        newEmail =  {
            "name": name,
            "tag": tag,
            "emailaddress": emailaddress,
            "password": password,
            "provider": provider
        }

        appendToJsonFile("secure/emails.json", "emails", newEmail)

    def creditcard(name, tag, owner, type, number, cvcOrCvv, expiry):

        newCreditcard =  {
            "name": name,
            "tag": tag,
            "owner": owner,
            "type": type,
            "number": number,
            "cvc/cvv": cvcOrCvv,
            "expiry": expiry
        }

        appendToJsonFile("secure/creditcards.json", "creditcards", newCreditcard)

    def computer(name, tag, username, password):

        newComputer =  {
            "name": name,
            "tag": tag,
            "username": username,
            "password": password
        }

        appendToJsonFile("secure/computers.json", "computers", newComputer)

    def note(name, tag, content):

        newNote =  {
            "name": name,
            "tag": tag,
            "content": content
        }

        appendToJsonFile("secure/notes.json", "notes", newNote)

    def file():
        console.warning("Not working yet :(")
