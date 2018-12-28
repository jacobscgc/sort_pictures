# sort_pictures
Simple script to sort pictures by year and month. 

It creates a 'sorted' directory in the same directory as where the pictures are located to be sorted.
Next, it checks for which years and months there are pictures and creates directories for those in the 'sorted' directory.
Finally, it copies the pictures to the correct directory in the 'sorted' directory (original files are kept). Pictures that do not have exif data are copied to the 'sorted/unsorted' directory.

It acccepts the following file formats:
- .jpg
- .JPG
- .jpeg
- .tiff
- .tif

## Dependancies:
This script uses python and the python package exifread. 

## Windows 10 installation instructions:
Get python if you do not have it already (https://www.python.org/downloads/).
If you are not using the default installation, make sure to also select the install pip option.

Next, run the Command Prompt as Administrator. 
Search for 'cmd', right-click the Command Prompt icon and select 'Run as Administrator'.
In this window type:

 pip install exifread
 
Press Enter. 
You can close the Command Prompt again.

On the top right of the github page, click download. Unpack the sort_pictures.py file to your computer.

## Ubuntu 16.04 / 18.04 installation instructions:
python is available in Ubuntu. 
if pip has not been installed yet, install it from a terminal (Ctrl + Alt + T) with: 

 sudo apt install pip
 sudo apt install python3-tk  # only if you want to use python3

Install the exifread package (also from a terminal):

 pip install exifread
 pip3 install exifread
 
The terminal can be closed.

On the top right of the github page, click download. Unpack the sort_pictures.py file to your computer.
 
## Running the script:

### Windows:
Simply double click the script. It opens a dialog box to select the folder with pictures to be sorted. The output folder is saved in the same folder as the pictures (output folder is called 'sorted').

### Ubuntu:
Open a terminal (Ctrl + Alt + Delete), go to the directory containing sort_pictures.py and run:

python sort_pictures.py
(python3 sort_pictures.py if you want to use python3)

It does not move the pictures but it copies the pictures. So the original pictures are kept in place. 
