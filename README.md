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


## Issues / Future Milestone Ideas

- Search results displayed in popup not 1 result per line
- Search results overflows window and no way to reach close button
- Add checkboxs for common file extensions
- Display all file extension types in search result
- Add option to search for filename
- Add option to search for filename (using regex)
- Print out total combined filesizes of search result