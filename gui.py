import PySimpleGUI as sg
import os
import shutil

sg.theme('Dark Blue 17') # Add Color

# list of extensions
extensions = [
    'dng',
    'gif',
    'png',
    'jpg',
    'avi',
    'mov',
    'mp4',
    '7z',
    'rar',
    'tar',
    'tar.gz',
    'zip',
]

file_info = [] # file info for popup
selected_extensions = [] # list of selected extensions

# All the stuff inside you window
layout = [
    [sg.Text('')],
    [sg.Text('SEARCH FILES IN THIS FOLDER RECURSIVELY:')],
    [sg.Text('Search folder'), sg.Input(key='_DIRINPUT_'), sg.FolderBrowse(),],
    [sg.Text('')],
    [sg.Text('FILTER FILES BY EXTENSION:', font=(22))],
    [sg.Checkbox(f'{i}', key=f'{i}') for i in extensions],
    [sg.Text('choose own extension: zip'), sg.InputText(key='_CUSTOM_EXT_')],
    [sg.Text('multiple extensions: zip, tar')],
    [sg.Text('extension with 2 dots: tar.gz')],
    [sg.Text('( Leave blank to disable filter )')],
    [sg.Text('FILTER BY FILE SIZE', font=(22))],
    [sg.Radio('off', "_RADIO_FILESIZE_", default=True, key='Radio_filesize_1'), sg.Radio('less than', "_RADIO_FILESIZE_", key='Radio_filesize_2'), sg.Radio('greater than', "_RADIO_FILESIZE_", key='Radio_filesize_3')],
    [sg.Text('Filesize (MB)'), sg.InputText(key='_CUSTOM_FILESIZE_')],
    [sg.Text('')],
    [sg.Button("Search", button_color="yellow on black", size=(10, 2))],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('COPY FILES TO THIS FOLDER:', font=(22))],
    [sg.Text('Select Output Folder'), sg.Input(key='_DIROUTPUT_'), sg.FolderBrowse(),],
    [sg.Text('( If you don\'t select Output Folder, nothing will happen. )')],
    [sg.Button("Copy Files", button_color="yellow on black"), sg.Cancel("Quit", button_color="red on black")],
    [sg.Text('')],
    [sg.Text('Search Results will appear below')],
    [sg.Text('', key='_OUTPUT_SEARCH_RESULTS_', size=(80, 200))],
]

# Create the Window
window = sg.Window('RECURSIVE SEARCH & COPY FILES').Layout([[sg.Column(layout, size=(650, 800), scrollable=True)]])

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event in (None, 'Cancel', 'Quit'):
        break

    dir_input = values['_DIRINPUT_']
    dir_output = values['_DIROUTPUT_']
    custom_ext = values['_CUSTOM_EXT_']


    # add user entered extension to selected_extensions
    if custom_ext:
        if ',' in custom_ext:
            custom_ext = custom_ext.split(",") # becomes a list
            for cext in custom_ext: # get each comma separated entry
                cext = cext.strip() # remove any whitespace
                selected_extensions.append(cext) # add string to selected_extensions
        else:
            selected_extensions.append(custom_ext) # add string to selected_extensions


    # add user ticked extension to selected_extensions
    for i in extensions:
        if values[f'{i}'] == True:
            selected_extensions.append(f'{i}')

    selected_extensions = list(dict.fromkeys(selected_extensions)) # remove duplicates

    # FILESIZE OPTIONS
    # it's off, ignore
    if values['Radio_filesize_1'] == True:
        filesize_filter = 'off'

    # try converting input in float
    elif values['Radio_filesize_2'] == True:
        filesize_filter = 'lt'
        try:
            custom_filesize = float(values['_CUSTOM_FILESIZE_'])
        except:
            custom_filesize = 0.0

    # try converting input in float
    elif values['Radio_filesize_3'] == True:
        filesize_filter = 'gt'
        try:
            custom_filesize = float(values['_CUSTOM_FILESIZE_'])
        except:
            custom_filesize = 0.0

    # show alert if search folder empty
    if not dir_input:    
        sg.popup('Search Folder can\'t be empty')

    else:
        for dirpath, dirnames, filenames in os.walk(dir_input):
            for f in filenames:
                ext = os.path.splitext(f)[-1] # file extension
                ext = ext[1:] # remove the dot
                thefile = (os.path.join(dirpath, f)) # file fullpath
                size = os.stat(thefile).st_size # filesize (bytes)
                sizeinmb = round(size/1000000, 2) #filesize (MB)
                file_input_fullpath = (os.path.join(dirpath, f))
                file_output_fullpath = (os.path.join(dir_output, f))


                # COPY FILES clicked
                if event == 'Copy Files':

                    # output_folder selected
                    if dir_output:

                        # file_size filter ON
                        if filesize_filter != 'off':
                            if selected_extensions: # if user chose extensions
                                if filesize_filter == 'lt':
                                    for s_ext in selected_extensions:
                                        if ext in s_ext and sizeinmb < custom_filesize:
                                            print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                            file_info.append(f'{f} ({sizeinmb}MB)')
                                            shutil.copy2(thefile, file_output_fullpath)
                                elif filesize_filter == 'gt':
                                    for s_ext in selected_extensions:
                                        if ext in s_ext and sizeinmb > custom_filesize:
                                            print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                            file_info.append(f'{f} ({sizeinmb}MB)')
                                            shutil.copy2(thefile, file_output_fullpath)

                            # file_extension filter OFF
                            else:
                                if filesize_filter == 'lt':
                                    if sizeinmb < custom_filesize:
                                        print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                        file_info.append(f'{f} ({sizeinmb}MB)')
                                        shutil.copy2(thefile, file_output_fullpath)
                                elif filesize_filter == 'gt':
                                    if sizeinmb > custom_filesize:
                                        print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                        file_info.append(f'{f} ({sizeinmb}MB)')
                                        shutil.copy2(thefile, file_output_fullpath)
                    
                        # file_size filter OFF
                        else:
                            if selected_extensions: # if user chose extensions
                                for s_ext in selected_extensions:
                                    if ext in s_ext:
                                        print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                        file_info.append(f'{f} ({sizeinmb}MB)')
                                        shutil.copy2(thefile, file_output_fullpath)

                            # file_extension filter OFF
                            else:
                                print(f'copying {thefile} to {file_output_fullpath} filesize: {sizeinmb}MB')
                                file_info.append(f'{f} ({sizeinmb}MB)')
                                shutil.copy2(thefile, file_output_fullpath)


                # SEARCH clicked
                if event == 'Search':

                    # file_size filter ON
                    if filesize_filter != 'off':
                        if selected_extensions: # if user chose extensions
                            if filesize_filter == 'lt':
                                for s_ext in selected_extensions:
                                    if ext in s_ext and sizeinmb < custom_filesize:
                                        file_info.append(f'{f} ({sizeinmb}MB)')

                            elif filesize_filter == 'gt':
                                for s_ext in selected_extensions:
                                    if ext in s_ext and sizeinmb > custom_filesize:
                                        file_info.append(f'{f} ({sizeinmb}MB)')

                        else: # no extensions selected
                            if filesize_filter == 'lt':
                                if sizeinmb < custom_filesize:
                                    file_info.append(f'{f} ({sizeinmb}MB)')
                            elif filesize_filter == 'gt':
                                if sizeinmb > custom_filesize:
                                    file_info.append(f'{f} ({sizeinmb}MB)')
                

                    # file_size filter OFF
                    else:
                        if selected_extensions: # if user chose extensions
                            for s_ext in selected_extensions:
                                if ext in s_ext:
                                    file_info.append(f'{f} ({sizeinmb}MB)')

                        else: # no extensions selected
                            file_info.append(f'{f} ({sizeinmb}MB) \n')


        # Display info when btn clicked
        if (event == 'Search'):
            if not file_info :
                window['_OUTPUT_SEARCH_RESULTS_'].update('no files found for that search')
            else:
                window['_OUTPUT_SEARCH_RESULTS_'].update('\n'.join(file_info))

        if (event == 'Copy Files'):
            if not dir_output:
                window['_OUTPUT_SEARCH_RESULTS_'].update('output directory can\'t be empty')
            elif not file_info :
                window['_OUTPUT_SEARCH_RESULTS_'].update('no files found for that search')
            else:
                window['_OUTPUT_SEARCH_RESULTS_'].update('\n'.join(file_info))

        # Clear Lists
        file_info.clear()
        selected_extensions.clear()

window.close()