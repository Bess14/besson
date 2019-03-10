# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
import sys

if __name__ == '__main__':

    for i in range(10):
        os.mkdir("dir_" + str(i))

    for i in range(10):
        os.removedirs("dir_" + str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

    file = os.listdir()
    for i in file:
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    file_1 = sys.argv[0]
    shutil.copy(file_1, "easy5.1.py")
    # os.remove("easy5.1.py")

# функции к normal:


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print('Перешел')
        print(os.getcwd() + ' - текущая директория')
    except FileNotFoundError:
        print(dir_path + ' - такой директории нет')


def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
        print(dir_path + ' - успешно создано')
    except FileExistsError:
        print(dir_path + ' - такая директория уже есть')


def del_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.removedirs(dir_path)
        print(dir_path + ' - успешно удалено')
    except FileNotFoundError:
        print(dir_path + ' - такой директории нет')


def list_dir(dir_path):
    for x in os.listdir(dir_path):
        print(x)

