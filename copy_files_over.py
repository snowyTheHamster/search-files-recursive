import os
import shutil

#1 A list of extensions
exts = [
    '.txt',     #0
    '.gif',     #1
    '.jpg',     #2
    '.png',     #3
    '.dng',     #4
    '.nef',     #5
    '.avi',     #6
    '.m4v',     #7
    '.mkv',     #8
    '.mov',     #9
    '.mp4',     #10
    '.mpg',     #11
    '.wmv'      #12
    ]

#2 A list of file sizes
sizes = [
    10000000,     #0 - 10MB
    100000000,    #1 - 100MB
    1000000000,   #2 - 1GB
]

#3 set the variables here
ftype = exts[0] #pick ext from above list
fsize = sizes[0] #pick file size from above list
source = './input' #directory to traverse
destination = './output' #the output directory

for dirpath, dirnames, filenames in os.walk(source): #traverse the source
    for f in filenames:
        ext = os.path.splitext(f)[-1] #get the files extension
        files = (os.path.join(dirpath, f)) #source of files to copy
        newpath = (os.path.join(destination, f)) #destination to save file
        size = os.stat(files).st_size #size info of file
        sizeinmb = round(size/1000000, 2) #round off to 2 decimal places

        if ext == ftype: #4a use this to filter filetype only
        # if ext == ftype and size < fsize: #4b use this to filter filetype & filesize
            print(f'copying {files} to {newpath} filesize: {sizeinmb}MB') #print a generic message
            shutil.copy2(files, newpath) #copy/paste the files into one location
