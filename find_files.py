# Find The Files That are Older Than X Days
# Import OS, SYS, and DATETIME

import os
import sys
import datetime

# Ask the User to Enter the Path of the File 
requested_path = input("Please Enter the Path: ")
age = 3

if not os.path.exists(requested_path):
    print("Please Provide a Valid Path: ")
    sys.exit(1)

if os.path.isfile(requested_path):
    print("Please Provide a Directory Path: ")
    sys.exit(2)

today = datetime.datetime.now()

# FOR Loop
for each_file in os.listdir(requested_path):
    each_file_path = os.path.join(requested_path, each_file)

    if os.path.isfile(each_file_path):
        file_create_date = datetime.datetime.fromtimestamp(
            os.path.getctime(each_file_path))
        print(each_file_path, today-file_create_date)
