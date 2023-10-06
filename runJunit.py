import os
import subprocess

dir_target = "/Corrector/Lab_4/Target"

for item in os.listdir(dir_target):
    #copy lib files
    destination = os.path.join(dir_target, item)
    print(destination) 
    bat = os.path.join(destination, "junit.bat")   
    subprocess.call([bat])