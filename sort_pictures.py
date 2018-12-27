#!/usr/bin/env python
"""
This script sorts all pictures in a folder (jpg files) by reading the EXIF information and extracting the Date and Time the picture was taken.
It sorts the pictures by year and month by creating a folder for each year from which pictures are present and for each month and putting the picture in
the correct folder.

This script depends on exifread (pip install exifread).

Run the script with:
	python sort_pictures.py -f input_picture_folder -o sorted_picture_folder
	
Output folder cannot exist. Choose a different output folder name or delete the existing output folder first.
"""

import exifread
import argparse
import os
from shutil import copyfile

# Deal with command line options:
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--folder', default=None, help="Enter the directory containing the pictures here: Example: ~/Documents/Pictures")
parser.add_argument('-o', '--output_folder', default='Pictures_sorted', help="Enter the name of the output folder, which is created in the file from which this script is called. Example: Pictures_sorted")
args = parser.parse_args()

mypath = os.path.expanduser(args.folder)
cwd = os.getcwd()
output_folder = cwd + '/' + args.output_folder

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
		
# put all filenames in a list:
files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

def _create_directories(output_folder, year):
	"""
	Helper function to create the directory structure for the output.
	
	:param output_folder = the folder to write the output to.
	"""

	# Create the directory structure:
	january = output_folder + '/' + year + '/01_January'
	february = output_folder + '/' + year + '/02_February'
	march = output_folder + '/' + year + '/03_March'
	april = output_folder + '/' + year + '/04_April'
	may = output_folder + '/' + year + '/05_May'
	june = output_folder + '/' + year + '/06_June'
	july = output_folder + '/' + year + '/07_July'
	august = output_folder + '/' + year + '/08_August'
	september = output_folder + '/' + year + '/09_September'
	october = output_folder + '/' + year + '/10_October'
	november = output_folder + '/' + year + '/11_November'
	december = output_folder + '/' + year + '/12_December'

	os.mkdir(january)
	os.mkdir(february)
	os.mkdir(march)
	os.mkdir(april)
	os.mkdir(may)
	os.mkdir(june)
	os.mkdir(july)
	os.mkdir(august)
	os.mkdir(september)
	os.mkdir(october)
	os.mkdir(november)
	os.mkdir(december)

def _convert_month(month):
	"""
	Helper function to translate the months from 01-12 to January - December.
	
	:param month: Month in numbers 01-12
	return month in January - December.
	"""
	month_dict = {'01':'01_January', '02':'02_February', '03':'03_March', '04':'04_April', '05':'05_May', '06':'06_June', '07':'07_July', '08':'08_August', '09':'09_September', '10':'10_October', '11':'11_November', '12':'12_December'}
	return month_dict[month]

years = []
# First, check for which years pictures are present:
for file_name in files:
	# Open image file for reading (binary mode)
	f = open(mypath + '/' + file_name, 'rb')
	# Return Exif tags
	tags = exifread.process_file(f)
	date_taken = tags['EXIF DateTimeOriginal']
	year = str(date_taken).split(':')[0]
	if year not in years:
		years.append(year)

# Create the directories for each year:
for year in years:
	os.mkdir(output_folder + '/' + year)
	_create_directories(output_folder, year)

# Loop through the files, copy each file in the correct directory:
counter = 0
for file_name in files:
	# Open image file for reading (binary mode)
	fileloc = mypath + '/' + file_name
	f = open(fileloc, 'rb')
	# Return Exif tags
	tags = exifread.process_file(f)
	date_taken = tags['EXIF DateTimeOriginal']
	year = str(date_taken).split(':')[0]
	month = str(date_taken).split(':')[1]
	month = _convert_month(month)
	copy_loc = output_folder + '/' + year + '/' + month + '/' + file_name
	copyfile(fileloc, copy_loc)
	counter += 1

print('Done, sorted {0} pictures over a period of {1} years.'.format(counter, len(years)))
