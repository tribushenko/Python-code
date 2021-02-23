import os

print(os.listdir("../../Downloads")) # выводит все файлы внутри директории

print(os.getcwd()) # текущая рабочая директория

print(os.path.exists("files.py")) # узнать существует ли файл

print(os.path.exists("random.py")) # True

print(os.path.isfile("files.py")) # проверить является ли указанный файл файлом или нет

print(os.path.isdir("../Machine_Learning")) # проверить является ли в данном пути файл Machine_Learning директорией

print(os.path.abspath("namespaces.py")) # узнать абсолютный путь к указанному файлу

os.chdir("../Machine_Learning") # сменяем текущую директорию на указанную
print(os.getcwd()) # выводим текущую директорию в консоль

for current_dir, dirs, files in os.walk("../"): # начиная с указанного пути функцию os.walk() 
    # проходит по текущей директории, заходит в поддиректории и берёт список всех файлов которые есть в данной поддиректории  
    print(current_dir, dirs, files)

import shutil  

shutil.copy("/home/artem/Programming/Python-code/test.txt", "/home/artem/Programming/Python-code/test1.txt") # копирование с test.txt в test1.txt
shutil.copytree("/home/artem/Programming/Python-code", "/home/artem/Programming/Python-code/Python-code") # полное копирование папки Python-code 
# с добавленим этой папки в папку Python-code

