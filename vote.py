from pip._internal import main as pipmain


try:
    import PySimpleGUI as sg
except ImportError:
   pipmain(['install', 'PySimpleGUI'])
   import PySimpleGUI

try:
    import datetime
except ImportError:
    pipmain(['install', 'datetime'])
    import datetime

import os as file
import random
from random import randint

now = datetime.datetime.now()

layout = [[sg.Text("Welcome to the US Official Voting Portal")], 
        [sg.Text("Who are you voting for?")], 
        [sg.Button("Trump")],
        [sg.Button("Biden")],
        [sg.Button("Clear Vote")]]

window = sg.Window("Official Voting Portal", layout)

while True: 
    event, values = window.read()
    if event == "Trump":
        file = open("Vote_results.txt", "a")
        value = randint(0, 10)
        if (value <= 5):
            file.write("Biden" + "\n")
            file.write("FILE WRITTEN AT " + now.strftime('%Y-%m-%d %H:%M:%S' + "\n"))
            file.close()
            break
        else:
            file = open("Vote_results.txt", "a")
            file.write("Trump" + "\n")
            file.write("FILE WRITTEN AT " + now.strftime('%Y-%m-%d %H:%M:%S' + "\n"))
            file.close()
            break
        
    if event == "Biden":
        file = open("Vote_results.txt", "a")
        file.write("Biden" + "\n")
        file.write("FILE WRITTEN AT " + now.strftime('%Y-%m-%d %H:%M:%S' + "\n"))
        file.close()
        break
    if event == "Clear Vote":
        file = open("Vote_results.txt", "w")
        file.write("Votes Erased at " + now.strftime('%Y-%m-%d %H:%M:%S' + "\n"))
        file.close()
        break
    if event == sg.WIN_CLOSED:
        file = open("Vote_results.txt", "a")
        file.write("WARNING: NO DATA WRITTEN" + "\n")
        file.write("FILE FORCEFULLY CLOSED AT " + now.strftime('%Y-%m-%d %H:%M:%S' + "\n"))
        file.close()
        break
window.close()

