import tkinter as tk

currentLang = 'english'

def set_langDE():
    currentLang = "Dutch"
    label.config(text="Language set to " + currentLang)

def set_langGE():
    currentLang = "German"
    label.config(text="Language set to " + currentLang)

def set_langCE():
    currentLang = "Chinese"
    label.config(text="Language set to " + currentLang)

def set_langFE():
    currentLang = "French"
    label.config(text="Language set to " + currentLang)

root = tk.Tk()
# entry = tk.Entry(root)
# entry.pack()

title = tk.Label(root, text="Choose the language you want to translate to \n")
title.pack()

DutchButton = tk.Button(root, text="Dutch", command = set_langDE)
GermanButton = tk.Button(root, text="German", command = set_langGE)
ChineseButton = tk.Button(root, text="Chinese", command = set_langCE)
FrenchButton = tk.Button(root, text="French", command = set_langFE)
DutchButton.pack()
GermanButton.pack()
ChineseButton.pack()
FrenchButton.pack()

label = tk.Label(root)
label.pack()

root.mainloop()