# coding=windows-1251
class IncompleteDataError(Exception):
    pass

while True:
    try:
        line : str = input("������� ������ (�������, ���, ��������, ��� ��������): ")
        data : list = line.split()
        
        if len(data) != 4: raise IncompleteDataError

        with open("file.txt", "a", encoding="UTF-8") as f:
            f.write(f"{data[0]} {data[1]} {data[2]} {data[3]}\n")
        print("������ ���������")

    except UnicodeError: print("�������� ��������� �����")
    except FileNotFoundError: print("������ ����� ���")
    except IncompleteDataError: print("�� ��� ������ ���������!")
    except KeyboardInterrupt:
        print("\n���� ��������!")
        break
