# coding=windows-1251
class EmptyFileError(Exception):
    pass
try:
    with open("FirstScript/file.txt", "r", encoding='utf-8') as f:
        read_data : list = [line.strip().split() for line in f]
    if not read_data: raise EmptyFileError

    print("%-15s%-15s%-15s%-15s" % ("Имя", "Фамилия", "Отчество", "Дата рождения"))
    for line in read_data:
        print("%-15s%-15s%-15s%-15s" % (line[0], line[1], line[2], line[3]))

except FileNotFoundError: print("Такого файла нет")
except EmptyFileError: print("Файл пустой")
except UnicodeError: print("Неверная кодировка файла")