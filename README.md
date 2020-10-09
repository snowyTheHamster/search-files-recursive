# Python GUI - search files recursively

This Python script find files recursively by file extension or filesize;

You can then copy the files into one folder.

## Use Case

- Search for files with certain file extensions.
- Search for large files taking up disk space.
- copy files over to one folder

## How to Install

- clone this repo: `git clone https://github.com/snowyTheHamster/search-files-recursive .`
- create a virtual environment: `python -m venv .venv`
- install required modules: `pip install -r requirements.txt`
- launch the gui script: `python gui.py`

A gui app should open for you to use.

## Executable

make the script executable with pyinstaller.

## Credit

I cleaned up the code using [Israel Dryer's example](https://github.com/israel-dryer/File-Search-Engine/blob/master/file_search_engine.py)

His video on a very similar project: [https://www.youtube.com/watch?v=IWDC9vcBIFQ](https://www.youtube.com/watch?v=IWDC9vcBIFQ)

## Issues / Possible Milestones

- ~~Search results displayed in popup not 1 result per line~~
- ~~Search results overflows window and no way to reach close button~~
- ~~Add checkboxs for common file extensions~~
- ~~Update results textbox size depending on length of results~~
- ~~use loop only for search logic (performance)~~ use index (serialization)
- ~~add timestamp for print re-index~~
- Display all file extension types in search result
- Show progress bar ?
- use tuple instead of list for file_extensions (performance)
- separate filesize & extension filter logic


### using tuple instead of list for matching file extensions:
```
for root, dirs, files in os.walk("path/to/directory"):
    for file in files:
        if file.endswith((".py", ".json")): # The arg can be a tuple of suffixes to look for
            # do stuff
```