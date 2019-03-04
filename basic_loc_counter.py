############################################################
# Dillon Cain
# 1/31/19
# Project 1
# Dr. Koh (CS4800)
############################################################
# Line of Code counter, reads in a file and counts the code.
# v1.0
# GUI built with PySimpleGUI
# Executable file made possible with PyInstaller
############################################################
import PySimpleGUI as sg
import sys


# Added frontend GUI instead of a command prompt
def gui_front():
    wm = "Welcome, to a basic LOC counter!\nWritten by Dillon Cain.\nMake sure you are in the correct directory.\nResults will follow with code and blank line counts.\n"
    sg.Popup(wm, auto_close=True, auto_close_duration=5)

    if len(sys.argv) == 1:
        event, (fname,) = sg.Window('LOC Counter by Dillon Cain').Layout([[sg.Text('Please select a file to count')],
                                                                          [sg.In(), sg.FileBrowse()],
                                                                          [sg.CloseButton('Open'),
                                                                           sg.CloseButton('Cancel')]]).Read()
    else:
        fname = sys.argv[1]

    if not fname:
        sg.Popup("Cancel", "No filename supplied")
        raise SystemExit("Cancelling: no filename supplied")
    print(event, fname)

    # Built in progress bar for fun plus people like status bars.

    for i in range(60):
        sg.OneLineProgressMeter('Counting in progress.....', i + 1, 60, 'key')

    # Start of loc counter
    handle = open(fname)  # Loads file into memory

    code_count = 0  # Init. variables
    line_spaces = 0
    c_line = 0
    for line in handle:
        line = line.rstrip()  # Removes whitespace on right side of line
        if not line.strip():  # Checks if line is empty and if so then it is a blank line
            line_spaces = line_spaces + 1
        elif line.startswith('#'):
            c_line = c_line + 1
        else:  # Last part of if else statement, where else results in there being a coded line
            code_count = code_count + 1

    sg.Popup('Lines that contain code:', code_count, 'Lines that are blank:', line_spaces)
    # High level call that outputs values


# def ask_again():
#     sg.PopupYesNo('Would you like to count another file?', )
# Add feature later that will ask if you would like to run again?
# 2/24/19

# Call function
gui_front()

