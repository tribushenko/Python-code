""" ads asd asd """
import os
os.chdir("../../Downloads/main/")
directories = []
mod_dirs = []
for current_dir, dirs, files in os.walk("."): # начиная с указанного пути функцию os.walk() 
    for i in files:
        if i.endswith(".py"):
            directories.append(current_dir)
directories = list(set(directories))
directories.sort()
for i in directories:
    i = i.replace(".", "main")
    mod_dirs.append(i)
#print(directories)
os.chdir("../../Programming/Python-code")
with open("test.txt", "w") as f:
    f.write("\n".join(mod_dirs))