import PySimpleGUI as sg
import os
import time
import shutil


sg.theme('Dark Blue 17') # Add Color


# All the stuff inside you window
layout = [
    [sg.Text('')],
    [sg.Text('FILTER FILES BY EXTENSION:')],
    [sg.Text('e.g: .jpg'), sg.InputText(key='_CUSTOM_EXT_')],
    [sg.Text('( Leave blank to disable filter )')],
    [sg.Text('')],
    [sg.Text('SEARCH FILES IN THIS FOLDER RECURSIVELY:')],
    [sg.Text('Search folder'), sg.Input(key='_DIRINPUT_'), sg.FolderBrowse(),],
    [sg.Button("Search")],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('COPY FILES TO THIS FOLDER:')],
    [sg.Text('Select Output Folder'), sg.Input(key='_DIROUTPUT_'), sg.FolderBrowse(),],
    [sg.Text('( If you don\'t select Output Folder, nothing will happen. )')],
    [sg.Button("Copy Files"), sg.Cancel("Exit")],
    [sg.Text('')]
]

# Create the Window
window = sg.Window('RECURSIVE SEARCH & COPY FILES', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event in (None, 'Cancel', 'Quit'):
        break

    # get start time
    starttime = time.time()

    dir_input = values['_DIRINPUT_']
    dir_output = values['_DIROUTPUT_']
    custom_ext = values['_CUSTOM_EXT_']
    

    # show alert if search folder empty
    if not dir_input:    
        sg.popup('Search Folder can\'t be empty')

    else:
        file_info = []
        for dirpath, dirnames, filenames in os.walk(dir_input):
            for f in filenames:
                ext = os.path.splitext(f)[-1] # file extension
                files = (os.path.join(dirpath, f)) # file fullpath
                size = os.stat(files).st_size # filesize (bytes)
                sizeinmb = round(size/1000000, 2) #filesize (MB)
                file_input_fullpath = (os.path.join(dirpath, f))
                file_output_fullpath = (os.path.join(dir_output, f))


                # copy files btn (clicked)
                if event == 'Copy Files':
                    if dir_output: # output_folder selected

                        # file_extension filter
                        if custom_ext: 
                            if ext == custom_ext:
                                print(f'copying {files} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                shutil.copy2(files, file_output_fullpath)
                        
                        # no filter
                        else:
                            print(f'copying {files} to {file_output_fullpath} filesize: {sizeinmb}MB')
                            shutil.copy2(files, file_output_fullpath)


                # search btn (clicked)
                if event == 'Search':

                    # file_extension filter
                    if custom_ext:
                        if ext == custom_ext:
                            file_info.append(f'{f} ({sizeinmb}MB)')

                    # no filter
                    else:
                        file_info.append(f'{f} ({sizeinmb}MB)')
        

        # Displays file info when search is clicked
        if event == 'Search':
            sg.popup(file_info)


        # time taken to run script
        endtime = time.time()
        totaltime = endtime - starttime
        totaltime = round(totaltime, 1)
        print(f'Done processing in: {totaltime} seconds. \n')

window.close()