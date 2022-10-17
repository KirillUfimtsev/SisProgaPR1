# coding=windows-1251
class EmptyFileError(Exception):
    pass
try:
    with open("FirstScript/file.txt", "r", encoding='utf-8') as file:
        data : list = [line.strip().split() for line in file]
    if not data: raise EmptyFileError

    print("%-10s%-10s%-10s%-10s" % ("���", "�������", "��������", "���� ��������"))
    for line in data:
        print("%-10s%-10s%-10s%-10s" % (line[0], line[1], line[2], line[3]))
except FileNotFoundError: print("���� �� ������!")
except EmptyFileError: print("���� ����!")
except UnicodeError: print("������ ���������!")