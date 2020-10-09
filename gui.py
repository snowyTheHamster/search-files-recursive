import os
import pickle
import PySimpleGUI as sg
from typing import Dict
sg.theme("Dark Blue 17")

# list of extensions
extensions = [
    'gif',
    'png',
    'jpg',
    'avi',
    'mp4',
]


class Gui:

    def __init__(self):
        self.layout: list = [
            [sg.Text('')],
            [sg.Text('RECURSIVE FILE SEARCH & COPY:')],
            [sg.Text('Search folder'), sg.Input(key='_DIRINPUT_'), sg.FolderBrowse(), sg.Button("Index", size=(10, 1), key='_INDEX_')],
            [sg.Text('')],
            [sg.Text('FILTER FILES BY EXTENSION:', font=(22))],
            [sg.Checkbox(f'{i}', key=f'{i}') for i in extensions],
            [sg.Text('or specify own extension: zip'), sg.InputText(key='_CUSTOM_EXT_')],
            [sg.Text('multiple extensions: zip, tar')],
            [sg.Text('')],
            [sg.Text('FILTER BY FILE SIZE', font=(22))],
            [sg.Radio('off', "_RADIO_FILESIZE_", default=True, key='Radio_filesize_1'), sg.Radio('less than', "_RADIO_FILESIZE_", key='Radio_filesize_2'), sg.Radio('greater than', "_RADIO_FILESIZE_", key='Radio_filesize_3')],
            [sg.Text('Filesize (MB)'), sg.InputText(key='_CUSTOM_FILESIZE_')],
            [sg.Button("Search", size=(10, 1), key='_SEARCH_')],
            [sg.Output(size=(100,30))],
            [sg.Text('')],
            [sg.Text('COPY FILES', font=(22))],
            [sg.Text('Copy files in result to Output Folder. PLEASE DOUBLE-CHECK search_results.txt')],
            [sg.Text('Select Output Folder'), sg.Input(key='_DIROUTPUT_'), sg.FolderBrowse(),],
            [sg.Text('( If Output Folder empty, nothing happens. )')],
            [sg.Button("Copy Files", size=(10, 1),  key='_COPY_')],
        ]

        self.window: object = sg.Window('Recursive Search Engine', self.layout, element_justification='left')

class SearchEngine:
    def __init__(self):
        self.file_index = [] # directory listing from os.walk
        self.results = [] # search results from search method
        self.matchs = 0 # no of records matched 
        self.records = 0 # no of records searched


    def create_new_index(self, values: Dict[str, str]) -> None:
        ''' Create a new file index of the root; then save to self.file_index and to pickle file '''
        root_path = values['_DIRINPUT_']
        self.file_index: list = [(root, files) for root, dirs, files in os.walk(root_path) if files]


    def load_existing_index(self) -> None:
        ''' Load an existing file index into the program '''
        try:
            with open('file_index.pkl','rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = []

    
    def search(self, values: Dict[str, str]) -> None:
        ''' Search for the term based on the type in the index; the types of search
            include: contains, startswith, endswith; save the results to file '''
        self.results.clear()
        self.matches = 0
        self.records = 0
        
        selected_extensions = []

        custom_ext = values['_CUSTOM_EXT_']
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


        # search for matches and count results
        for path, files in self.file_index:
            for file in files:
                self.records +=1

                if selected_extensions:
                    for s_ext in selected_extensions:
                        if file.endswith(s_ext):
                            result = path.replace('\\','/') + '/' + file
                            self.results.append(result)
                            self.matches +=1
                        else:
                            continue
                else:
                            result = path.replace('\\','/') + '/' + file
                            self.results.append(result)
                            self.matches +=1

        
        # save results to file
        with open('search_results.txt','w') as f:
            for row in self.results:
                f.write(row + '\n')

def main():
    ''' The main loop for the program '''
    g = Gui()
    s = SearchEngine()
    s.load_existing_index() # load if exists, otherwise return empty list

    while True:
        event, values = g.window.read()

        if event is None:
            try:
                os.remove('file_index.pkl')
                os.remove('search_results.txt')
            except:
                print('temporary files not found')
            break
        if event == '_INDEX_':
            s.create_new_index(values)
            print()
            print(">> New index created")
            print()
        if event == '_SEARCH_':
            s.search(values)

            # print the results to output element
            print()
            for result in s.results:
                print(result)
            
            print()
            print(">> Searched {:,d} records and found {:,d} matches".format(s.records, s.matches))
            print(">> Results saved in working directory as search_results.txt.")


if __name__ == '__main__':
    print('Starting program...')
    main() 