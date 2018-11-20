# traverse_files_and_transfer_files
This Python script searches all files recursively by extension in a directory and copy/pastes them into one folder.

# Problem

Just recovered a failed harddrive or sd card? Some recovery softwares save recovered files across multiple folders making it difficult to organize.

These python scripts will help you find files by filetype and save them in one folder.

# Usage

- use **get_files_info.py** to get data about your files and save it to a text file.
- use **copy_files_over.py** to copy/paste the desired files to an output folder.

### get_files_info.py

get_files_info.py will list out all files in the source to a text file. You can choose to filter the filetype & filesize as also the location of your source folder.

Near the top of the script (#1) is a list of file extensions, add or edit them to your needs.

Change the parameter to your needs at (#3) to select filetype, filesize, folder locations.

Near the bottom of the script (#4a, #4b) you can choose whether to filter just by filetype or also by filesize by commenting/uncommenting the if conditions.

run the script:

```
py get_files_info.py
```

You should now have a text file with info based on your filter.

This info can help you decide whether to copy/paste all files at once or separate by filesizes.

### copy_files_over.py

copy_files_over.py is very similar to the other script but instead will copy and paste the files to your desired destination.

You also need to select filetype, filesize and folder locations.

run the script with:

```
py copy_files_over.py
```

