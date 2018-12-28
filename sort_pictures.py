#!/usr/bin/env python
"""
This script sorts all pictures in a folder (jpg files) by reading the EXIF information and extracting the Date and Time the picture was taken.
It sorts the pictures by year and month by creating a folder for each year from which pictures are present and for each month and putting the picture in
the correct folder.

This script depends on exifread (pip install exifread).

Run the script with:
    python sort_pictures.py
    
Output folder cannot exist. Choose a different output folder name or delete the existing output folder first.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import exifread
import os
from shutil import copyfile, copy

root = tk.Tk()
root.withdraw()

mypath = filedialog.askdirectory(title = "Please select the photo folder")
output_folder = mypath + '/sorted'
unsorted_folder = output_folder + '/unsorted'
file_extensions = ['JPG', 'jpg', 'jpeg', 'tiff', 'tif']

# Check whether the image folder exists:
if not os.path.exists(mypath):
    print('Path {0} does not exist, check the location of your images and try again'.format(mypath))
    exit()

# If the output folder already exists, exit:
if os.path.exists(output_folder):
    print('Output folder {0} already exists, use a different output folder or delete the old one first.'.format(output_folder))
    exit()

# Create the output folder:
os.mkdir(output_folder)
# Create a rest folder for the images that cannot be sorted (no exif data)
os.mkdir(unsorted_folder)
        
# put all filenames in a list:
files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.split('.')[-1] in file_extensions]

def _create_directories(output_folder, year, year_month):
    """
    Helper function to create the directory structure for the output.
    
    :param output_folder = the folder to write the output to.
    :param year = list of years present in the set of pictures.
    :param year_month = list of tuples (year, month) present in the set of pictures.
    """

    month_list = ['01_January', '02_February', '03_March', '04_April', '05_May', '06_June', '07_July', '08_August', '09_September', '10_October', '11_November', '12_December']
    for month in month_list:
        if (year, month) in year_month:
            os.mkdir(output_folder + '/' + year + '/' + month)

def _convert_month(month):
    """
    Helper function to translate the months from 01-12 to January - December.
    
    :param month: Month in numbers 01-12
    return month in January - December.
    """
    month_dict = {'01':'01_January', '02':'02_February', '03':'03_March', '04':'04_April', '05':'05_May', '06':'06_June', '07':'07_July', '08':'08_August', '09':'09_September', '10':'10_October', '11':'11_November', '12':'12_December'}
    return month_dict[month]

years = []
year_month = []
# First, check for which years pictures are present:
for file_name in files:
    # Open image file for reading (binary mode)
    f = open(mypath + '/' + file_name, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    if 'EXIF DateTimeOriginal' in tags:
        date_taken = tags['EXIF DateTimeOriginal']
        year = str(date_taken).split(':')[0]
        month = _convert_month(str(date_taken).split(':')[1])
        year_month_tup = (year, month)
        if year not in years:
            years.append(year)
        if year_month_tup not in year_month:
                    year_month.append(year_month_tup)

# Create the directories for each year:
for year in years:
    os.mkdir(output_folder + '/' + year)
    _create_directories(output_folder, year, year_month)

# Loop through the files, copy each file in the correct directory:
counter = 0
for file_name in files:
    # Open image file for reading (binary mode)
    fileloc = mypath + '/' + file_name
    f = open(fileloc, 'rb')
    # Return Exif tags
    tags = exifread.process_file(f)
    if 'EXIF DateTimeOriginal' in tags:
        date_taken = tags['EXIF DateTimeOriginal']
        year = str(date_taken).split(':')[0]
        month = _convert_month(str(date_taken).split(':')[1])
        copy_loc = output_folder + '/' + year + '/' + month + '/' + file_name
        copyfile(fileloc, copy_loc)
    else:
        copy(fileloc, unsorted_folder)
    counter += 1

messagebox.showinfo("", 'Done, sorted {0} pictures over a period of {1} years.'.format(counter, len(years)))
