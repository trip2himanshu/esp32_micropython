# main.py
# micropython for esp32s3 devkitc-1 v0.1
# Himanshu Tripathi

# the basic operations one can perform to access
# and manipulate files on the ESP32 file system
# following are the functions demonstrated here :
# 1. listing of files and directories
# 2. creating new directory
# 3. change directory
# 4. Write, Read and append files
# 5. checking if file or directory already exists
# 6. renaming a file or directory
# 7. getting file or diectory information
# 8. removing or deleting the file or directory 

import os
import time

# list files and directories in the current directories 
def list_files():
    file_list = os.listdir()
    for file in file_list:
        print(file)

def create_dir():
    os.mkdir("/new_dir")
    list_files()

def file_ops():
    # change directory
    os.chdir("/new_dir")
    time.sleep(1)
    # create and write file in new directory
    with open ("filename.txt","w") as file:
        file.write("Hello, ESP32S3 file system")
    time.sleep(1)
    # open and read the file
    with open ("filename.txt", "r") as file:
        content = file.read()
    print(content)
    time.sleep(1)
    # append the content in file
    with open ("filename.txt", "a") as file:
        file.write("\nNow appending this line into the file")
    time.sleep(1)
    # again read the file to verify the append
    with open ("filename.txt", "r") as file:
        content = file.read()
    print(content)
    time.sleep(1)
    # check if a file or directory exists
    if "filename.txt" in os.listdir():
        print("File exists")
    time.sleep(1)
    # rename a file
    os.rename("filename.txt", "newfilename.txt")
    time.sleep(1)
    # get file or directory information
    file_info = os.stat("newfilename.txt")
    print("File Size: ", file_info[6], "Bytes")
    time.sleep(1)
    # remove a file
    os.remove("newfilename.txt")
    print(os.listdir())
    time.sleep(1)
    # remove an empty directory
    os.chdir("/")
    os.rmdir("new_dir")
    print(os.listdir())
    
    
    

print("Following files and directories are present in esp32s3: \n")    
list_files()
time.sleep(2)
print("create new directory and print the list of files and directories present\n")
create_dir()
time.sleep(2)
print("showing the basic file operations\n")
file_ops()

        
