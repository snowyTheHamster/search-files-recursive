# traverse_files_and_transfer_files
This Python script searches files recursively by extension in a directory and copy/pastes them into one folder.

# Problem

Just recovered a failed drive or sd card? Some recovery softwares dump the recovered files across multiple folders making it troublesome to organize.

These python scripts will help you find all the scattered files and paste them into one folder.

# Usage

- **get_files_info.py** saves a list of data about your files to a txt file.
- **copy_files_over.py** copy/pastes the desired files into an output folder.

### get_files_info.py

**get_files_info.py** will list out all files in the source to a text file. You can choose to filter by filetype, filesize and also choose the location of your source folder.

Near the top of the script (#1) is a list of file extensions, add or edit them to your needs.

Change the parameter at (#3) to select filetype, filesize, source location etc.

Near the bottom of the script (#4a, #4b) choose whether to filter just by 'filetype' or 'filetype & filesize' by commenting/uncommenting the **if** conditions.

run the script:

```
py get_files_info.py
```

You should now have a text file with a list of information based on your filter.

This info can help you decide whether to copy/paste all files at once or separate by filesizes in the next step.

### copy_files_over.py

**copy_files_over.py** is similar to the first script but instead will copy/paste the files to your desired destination.

You need to select filetype, filesize and folder locations just like the first script.

run the script with:

```
py copy_files_over.py
```

You should now have the selected files copied over to your destination folder.

If not, check you have selected the correct file extensions, filesizes and whether you want the filesize '<' or '>' than the desired size. Also check that the folder locations are correct.