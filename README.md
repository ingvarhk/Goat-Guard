# Goat Guard
Goat Guard is a password manager that allows you to store and retrieve passwords, emails, credit cards, notes and logins.

## Installation
1. `pip install -r requirements.txt`


Tkinter isn't distributed through pip; if it didn't come pre-packaged with Python, you have to get it from elsewhere:

* Debian/Ubuntu:
`sudo apt-get install python3-tk`

* Fedora:
`sudo dnf install python3-tkinter`

* MacOS:
`brew install python-tk`

2. On Linux `pyperclip` requires `xclip` to be installed.

## How to use
1. `python3 src/goatguard.py`
2. Create a master password.
3. Add credentials :D


## Commands
```
COMMANDS
    add  - Options: l [login], e [email], c [credit card], p [computer], n [note]
    remove - Options: l [login], e [email], c [credit card], p [computer], n [note]
    get - Options: l [login], e [email], c [credit card], p [computer], n [note]

    gen - Generate password - Arguments: <lenght>

    clear - clear screen
    info - info about Goat Guard
    exit - exit goat guard
```

### Warning - WIP
This project is still in development, please use at your own risk.