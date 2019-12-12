from tkinter import *

def window():
    root = Tk()
    root.title("Goat Guard - Password Manager")
    root.geometry("1000x500")
    root.resizable(height = False, width = False)
    root.configure(bg="#00b38c")

    servicesText = Label(root, text="Services", bg="#00b38c", font=("", 20))
    servicesText.pack(anchor="nw")
    
    root.mainloop()
