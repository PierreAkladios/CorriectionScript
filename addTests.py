import os, zipfile
import shutil

dir_target = "D:\Corrector\Lab_3\Target"
dir_tests = "D:\Corrector\Lab_3\JUnit"
dir_lib = "D:\Corrector\libs"

os.chdir(dir_target) # change directory from working dir to dir with files

java = ".java"

for item in os.listdir(dir_target):
    #copy lib files
    for file_name in os.listdir(dir_lib):
        # construct full file path
        source = os.path.join(dir_lib, file_name)
        destination = os.path.join(dir_target, item)
        print(destination)
        shutil.copy2(source, destination)
    #copy test files
    for file_name in os.listdir(dir_tests):
        if file_name.endswith(java):
            # construct full file path
            source = os.path.join(dir_tests, file_name)
            destination = os.path.join(dir_target, item)
            shutil.copy2(source, destination)

       