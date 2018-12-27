# sort_pictures
Simple script to sort pictures by year and month.

# Dependancies:
This script uses python and the python package exifread. 

# Windows 10 installation instructions:
Get python python if you do not have it already (https://www.python.org/downloads/).
make sure to also select the install pip option.

Next, run the Command Prompt as Administrator. 
Search for 'cmd', right-click the Command Prompt icon and select 'Run as Administrator'.
In this window type:
 pip install exifread
Press Enter. 
You can close the Command Prompt again.

# Ubuntu 16.04 / 18.04
python is available in Ubuntu. 
if pip has not been installed yet, install it from a terminal (Ctrl + Alt + T) with: 
 sudo apt install pip

Install the exifread package (also from a terminal):
 pip install exifread
 
# Running the script:
Simply double click the script. It opens a dialog box to select the folder with pictures to be sorted and asks how the output folder should be called. The output folder is saved in the same folder as the pictures.
