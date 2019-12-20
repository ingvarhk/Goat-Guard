from tkinter import *

def window():
    root = Tk()
    root.title("Goat Guard - Password Manager")
    root.geometry("1000x500")
    root.resizable(height = False, width = False)
    root.configure(bg="#00b38c")

    servicesText = Label(root, text="Services")
    servicesText.pack(anchor="nw")

    root.mainloop()

def test():
    window = Tk()
    window.title("Goat Guard - Add login")
    window.geometry("250x300")
    window.resizable(height = False, width = False)
    #window.configure(bg="#00b38c")

    nameText = Label(window, text="Add login", font=("", 20))
    nameText.pack(anchor="nw")


    nameText = Label(window, text="Name")
    nameText.pack(anchor="nw")

    nameInput = Entry(window)
    nameInput.pack(anchor="nw")

    favoriteCheckbutton = Checkbutton(window, text="Favorite")
    favoriteCheckbutton.pack(anchor="nw")

    urlText = Label(window, text="Web Address")
    urlText.pack(anchor="nw")

    urlInput = Entry(window)
    urlInput.pack(anchor="nw")

    usernameText = Label(window, text="Username")
    usernameText.pack(anchor="nw")

    usernameInput = Entry(window)
    usernameInput.pack(anchor="nw")

    passwordText = Label(window, text="Password")
    passwordText.pack(anchor="nw")

    passwordInput = Entry(window, show="*")
    passwordInput.pack(anchor="nw")

    okButton = Button(window, text="Add login")
    okButton.pack(anchor="nw")

    window.mainloop()
