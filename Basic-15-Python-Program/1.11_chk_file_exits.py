#importing os path reader module 
import os.path


print("check file exits or not")
#file paths (file names)
path1="abc.py"
path2="abc.txt"

#print wheather file exists or not
print(f"file {path1} existance {os.path.isfile("abc.py")} ")

print(f"file {path2} existance {os.path.isfile("abc.txt")} ")



 



