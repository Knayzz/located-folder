
import os
from zoneinfo import available_timezones
import psutil
import subprocess
import fnmatch

def find_files(filename, search_path):
    matches = []
    for root, dirnames, filenames in os.walk(search_path):
        for file in filenames:
            if fnmatch.fnmatch(file, filename):
                matches.append(os.path.join(root, file))
    return matches



# List of part disk 
partitions = psutil.disk_partitions()

for partition in partitions:
    device_name = partition.device
    mount_point = partition.mountpoint
    print("Storage Device : {} ".format(device_name))

while True:
    # Extension of file 
    
    extension_file=input("Write name of extension file (exemple : txt) : ")
    extension_file="."+extension_file
    print("PS : Used * in file name or extension name for search all name or extension ")
    #Name of file
    name_file=input("Write name of file : ")
    # Compil of file
    file= name_file+extension_file

    # Confirm to use this file
    use_file=input("Do you use ' " + file + " ' or not (y/n)")
    if use_file=='y':
        available_path=input("Choose path for search : ")
        result = find_files(file, available_path)
        print("Files are located: ")
        if result:
            print("     "+ result)
        else:
            print("Files are not located.")
    else:
        continue
