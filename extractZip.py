import os, zipfile

dir_name = 'D:\Corrector\Lab_3\MessedUp'
extension = ".zip"

dir_target = "D:\Corrector\Lab_3\Target1"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if os.path.isdir(item):
        print(item)
        subdir = os.path.join(dir_name, item)
        for folder in os.listdir(subdir):
            print(folder)
            if folder.endswith(extension): # check for ".zip" extension
                file_name = os.path.join(dir_name, item, folder) # get full path of files
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(dir_target) # extract file to dir
                zip_ref.close() # close file
        
    