import json
import os

def getSetupFile():
    if os.path.isfile("data/setup.json"):
        with open("data/setup.json", "r") as f:
            content = f.read()
            print("Reading file data/setup.json")

            return json.loads(content)
    else:
        print("couldn't find setup.json")
        with open("data/setup.json", "w") as f:

            toFille = {
              "signup": True,
              "developer": False
            }
            f.write(json.dumps(toFille))
            print("setup.json created")
            return toFille

def getServicesFile():
    if os.path.isfile("passwords/services.json"):
        with open("passwords/services.json", "r") as f:
            content = f.read()
            print("Reading file  data/services.json")
            toReturn = json.loads(content)

            return toReturn
    else:
        print("couldn't find setup.json")
        with open("passwords/services.json", "w") as f:

            toFille = {

            }
            f.write(json.dumps(toFille))
            print("services.json created")
            return toFille

def addToServicesFile():
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)

    feeds.append(entry)
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds, indent=2))
