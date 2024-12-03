# importing extrnal command call 
from subprocess import call

print(f"This command lists the files and directories in the current directory with details.")

#calling external call command 
print(call(["ls","-l"]))
