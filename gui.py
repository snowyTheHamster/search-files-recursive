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
    [sg.Text('FILTER BY FILE SIZE')],
    [sg.Radio('off', "_RADIO_FILESIZE_", default=True, key='Radio_filesize_1'), sg.Radio('less than', "_RADIO_FILESIZE_", key='Radio_filesize_2'), sg.Radio('greater than', "_RADIO_FILESIZE_", key='Radio_filesize_3')],
    [sg.Text('Filesize (MB)'), sg.InputText(key='_CUSTOM_FILESIZE_')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('SEARCH FILES IN THIS FOLDER RECURSIVELY:')],
    [sg.Text('Search folder'), sg.Input(key='_DIRINPUT_'), sg.FolderBrowse(),],
    [sg.Button("Search")],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('COPY FILES TO THIS FOLDER:')],
    [sg.Text('Select Output Folder'), sg.Input(key='_DIROUTPUT_'), sg.FolderBrowse(),],
    [sg.Text('( If you don\'t select Output Folder, nothing will happen. )')],
    [sg.Button("Copy Files"), sg.Cancel("Quit")],
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
    
    # set filesize option
    if values['Radio_filesize_1'] == True:
        filesize_filter = 'off'
        custom_filesize = 0.0
        custom_filesize = float(custom_filesize)
    elif values['Radio_filesize_2'] == True:
        filesize_filter = 'lt'
        if custom_filesize == '':
            custom_filesize = 0.0
            custom_filesize = float(custom_filesize)
        else:
            custom_filesize = float(values['_CUSTOM_FILESIZE_'])
    elif values['Radio_filesize_3'] == True:
        filesize_filter = 'gt'
        if custom_filesize == '':
            custom_filesize = 0.0
            custom_filesize = float(custom_filesize)
        else:
            custom_filesize = float(values['_CUSTOM_FILESIZE_'])

    # show alert if search folder empty
    if not dir_input:    
        sg.popup('Search Folder can\'t be empty')

    else:
        file_info = []
        for dirpath, dirnames, filenames in os.walk(dir_input):
            for f in filenames:
                ext = os.path.splitext(f)[-1] # file extension
                thefile = (os.path.join(dirpath, f)) # file fullpath
                size = os.stat(thefile).st_size # filesize (bytes)
                sizeinmb = round(size/1000000, 2) #filesize (MB)
                file_input_fullpath = (os.path.join(dirpath, f))
                file_output_fullpath = (os.path.join(dir_output, f))


                # copy files btn (clicked)
                if event == 'Copy Files':

                    if dir_output: # output_folder selected

                        # file_extension filter ON
                        if custom_ext: 
                            if ext == custom_ext:
                                print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                shutil.copy2(thefile, file_output_fullpath)
                        
                        # file_extension filter OFF
                        else:
                            print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                            shutil.copy2(thefile, file_output_fullpath)

                    # get end time
                    endtime = time.time()


                # search btn (clicked)
                if event == 'Search':

                    # file_size filter ON
                    if filesize_filter != 'off':
                        # file_extension filter ON
                        if custom_ext:
                            if filesize_filter == 'lt':
                                if ext == custom_ext and sizeinmb < custom_filesize:
                                    file_info.append(f'{f} ({sizeinmb}MB)')
                            elif filesize_filter == 'gt':
                                if ext == custom_ext and sizeinmb > custom_filesize:
                                    file_info.append(f'{f} ({sizeinmb}MB)')

                        # file_extension filter OFF
                        else:
                            if filesize_filter == 'lt':
                                if sizeinmb < custom_filesize:
                                    file_info.append(f'{f} ({sizeinmb}MB)')
                            elif filesize_filter == 'gt':
                                if sizeinmb > custom_filesize:
                                    file_info.append(f'{f} ({sizeinmb}MB)')
                
                    # file_size filter OFF
                    else:

                        # file_extension filter ON
                        if custom_ext:
                            if ext == custom_ext:
                                file_info.append(f'{f} ({sizeinmb}MB)')

                        # file_extension filter OFF
                        else:
                            file_info.append(f'{f} ({sizeinmb}MB)')

                    # get end time
                    endtime = time.time()
        

        # Displays file info when search is clicked
        if event == 'Search':
            if not file_info :
                sg.popup('no files found for that search')
            else:
                sg.popup(file_info)


        # time taken to run script
        totaltime = endtime - starttime
        totaltime = round(totaltime, 1)
        print(f'Done processing in: {totaltime} seconds. \n')

window.close()