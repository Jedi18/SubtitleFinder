from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import subtitle_downloader

root = Tk()

# GUI Initial settings
root.title("Subtitle Finder")
root.geometry("800x600")

# Functions for menu

# Loop through given directory and list out all file names
file_formats = ['mp4', 'mkv', 'mov', 'avi']
files_found = []
current_file_location = ''

def open_file():
    file_location = fileTextField.get("1.0", 'end-1c')
    filenames = os.listdir(file_location)

    fileListBox1.delete(first=0, last=END)
    files_found.clear()

    for filename in filenames:
        if filename[-3:] in file_formats:
            files_found.append(filename)

    current_file_location = file_location
    populate_listbox()
    downloadSelectedButton['state'] = 'normal'

def quit_app():
    print("WORK IN PROGRESS")


def change_websites():
    print("WORK IN PROGRESS")


def about_us():
    print("WORK IN PROGRESS")

def populate_listbox():
    for file in files_found:
        fileListBox1.insert(END, file)

def download_subtitle():
    print("WORRRK IN PROGRESS")
    subtitle_downloader.get_download_list(fileListBox1.get(fileListBox1.curselection()))

# ------ Menu -----


menuBar = Menu(root)

# ----- FILE MENU -----
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open File", command=open_file)
fileMenu.add_command(label="Quit", command=quit_app)
menuBar.add_cascade(label="File", menu=fileMenu)

# ----- SETTINGS MENU -----
settingsMenu = Menu(menuBar, tearoff=0)
settingsMenu.add_command(label="Select Websites", command=change_websites)
menuBar.add_cascade(label="Settings", menu=settingsMenu)

# ----- Help MENU -----
helpMenu = Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About us", command=about_us)
menuBar.add_cascade(label="Help", menu=helpMenu)

root.config(menu=menuBar)

# ----- MENU END -----

frame = Frame(root)

fileTextField = Text(frame, height=2, width=30)
openButton = Button(frame, text='Open Video File', command=open_file)
fileListBox1 = Listbox(frame, selectmode=SINGLE, width=100)
downloadSelectedButton = Button(frame, text='Download', command=download_subtitle, state=DISABLED)
fileListBox2 = Listbox(frame, selectmode=SINGLE, width=100)

fileTextField.pack()
openButton.pack()
fileListBox1.pack()
downloadSelectedButton.pack()
fileListBox2.pack()
frame.pack()

root.mainloop()

