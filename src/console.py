import platform

if platform.system() == "Windows":
    red = ""
    yellow = ""
    cyan = ""
    reset = ""
    pink = ""
    green = ""

else:
    
    red = "\u001b[31m"
    yellow = "\u001b[33m"
    cyan = "\u001b[36m"
    reset = "\u001b[0m"
    pink = "\033[94m"
    green = "\033[32m"


def info(infoInput):
    print(green + "INFO: " + reset + str(infoInput))

def warning(warningInput):
    print(yellow + "WARNING: " + reset + str(warningInput))

def error(errorInput):
    print(red + "ERROR: " + reset + str(errorInput))
