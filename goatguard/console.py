red = "\u001b[31m"
pink = "\033[95m"
yellow = "\u001b[33m"
cyan = "\u001b[36m"
reset = "\u001b[0m"

def info(infoInput):
    print(reset + "INFO: " + str(infoInput))

def warning(warningInput):
    print(yellow + "WARNING: " + reset + str(warningInput))

def error(errorInput):
    print(red + "ERROR: " + reset + str(errorInput))
