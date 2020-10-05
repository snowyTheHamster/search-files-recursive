import PySimpleGUI as sg
import os
import time
import shutil


sg.theme('Dark Blue 3') # Add Color

# All the stuff inside you window
layout = [
    [sg.Text('Find all files scattered in a folder and')],
    [sg.Text('duplicate them into one folder ')],
    [sg.Text('')],
    [sg.Text('HOW TO USE:')],
    [sg.Text('1. Select input folder')],
    [sg.Text('2. Select output folder')],
    [sg.Text('3. Select files extensions (optional)')],
    [sg.Text('4. Select file size (optional)')],
    [sg.Text('5. Click View Results')],
    [sg.Text('6. Click Copy Results')],
    [sg.Text('Select Input Folder'), sg.Input(key='_DIRINPUT_'), sg.FolderBrowse(),],
    [sg.Text('(Don\'t leave blank)')],
    [sg.Text('- - - - - - - - - - - - - - - - -')],
    [sg.Text('Select Output Folder'), sg.Input(key='_DIROUTPUT_'), sg.FolderBrowse(),],
    [sg.Text('- - - - - - - - - - - - - - - - -')],
    [sg.Text('Filter filetype eg: jpg'), sg.InputText(key='_FILEEXT_')],
    [sg.Text('(leave blank to disable filter)')],
    [sg.OK("Generate"), sg.Cancel(), sg.Cancel("Quit")]
]

# Create the Window
window = sg.Window('SEARCH & COPY FILES', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event in (None, 'Cancel', 'Quit'):
        break

    #start time
    stime = time.time()

    dir_input = values['_DIRINPUT_']
    dir_output = values['_DIROUTPUT_']
    file_ext = values['_FILEEXT_']

    for dirpath, dirnames, filenames in os.walk(dir_input):
        for f in filenames:
            ext = os.path.splitext(f)[-1] # gets the file ext
            files = (os.path.join(dirpath, f)) # full path of file
            size = os.stat(files).st_size # filesize info in bytes
            sizeinmb = round(size/1000000, 2) #filesize rounded off to 2 decimal places

            file_input_fullpath = (os.path.join(dirpath, f)) # full path of input file
            file_output_fullpath = (os.path.join(dir_output, f)) # full path of output file

            # print(f'filename: {f}, filetype: {ext}, filesize: {sizeinmb}MB') # display file info
            # print(f'copying {files} to {file_output_fullpath} filesize: {sizeinmb}MB') # print a generic message            
            # shutil.copy2(files, file_output_fullpath) # copy/pasto the files to output folder
            print(file_ext)


    #end time
    etime = time.time()
    
    totaltime = etime - stime
    totaltime = round(totaltime, 1)

    print(f'Done processing in: {totaltime} seconds \n')
    print('You may now close the program...')

window.close()