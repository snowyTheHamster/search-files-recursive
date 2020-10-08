# Python GUI - search files recursively

This Python script find files recursively by file extension or filesize;

You can then copy those files into one folder.

## Use Case

- Your sd card fails, you use a recovery app but it saves the images across multiple folders.
- Search for files with certain file extensions.
- Search for large files taking up disk space.

## How to Install

- clone this repo: `git clone https://github.com/snowyTheHamster/search-files-recursive .`
- create a virtual environment: `python -m venv .venv`
- install required modules: `pip install -r requirements.txt`
- launch the gui script: `python gui.py`

A gui app should open for you to use.

## Executable

You can make the script executable with pyinstaller.


## Issues / Possible Milestones

- ~~Search results displayed in popup not 1 result per line~~
- ~~Search results overflows window and no way to reach close button~~
- ~~Add checkboxs for common file extensions~~
- Update results textbox size depending on length of results
- Display all file extension types in search result
- Add option to search for filename (regex) ?
- Print out total combined filesizes of search result ? 
- Show progress bar
- use tuple instead of list for file_extensions (performance)
- use loop only for search logic (performance)
- copy logic uses results from search logic (performance)
- separate extension, filesize logics



### using tuple instead of list for matching file extensions:
```
for root, dirs, files in os.walk("path/to/directory"):
    for file in files:
        if file.endswith((".py", ".json")): # The arg can be a tuple of suffixes to look for
            # do stuff
```