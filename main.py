from tkinter import *
from tkinter import messagebox

root = Tk()

# GUI Initial settings
root.title("Subtitle Finder")
root.geometry("800x600")

# Functions for menu

def open_file():
    print("WORK IN PROGRESS")

def quit_app():
    print("WORK IN PROGRESS")

def change_websites():
    print("WORK IN PROGRESS")

def about_us():
    print("WORK IN PROGRESS")
# ------ Menu -----


menuBar = Menu(root)

# ----- FILE MENU -----
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open File", command=open_file)
fileMenu.add_command(label="Quit", command=quit_app)
menuBar.add_cascade(label="File", menu=fileMenu)

# ----- SETTINGS MENU -----
settingsMenu = Menu(menuBar,tearoff=0)
settingsMenu.add_command(label="Select Websites", command=change_websites)
menuBar.add_cascade(label="Settings",menu=settingsMenu)

# ----- Help MENU -----
helpMenu = Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About us", command=about_us)
menuBar.add_cascade(label="Help", menu=helpMenu)

root.config(menu=menuBar)

root.mainloop()

