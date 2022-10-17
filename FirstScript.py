# coding=windows-1251
class IncompleteDataError(Exception):
    pass

while True:
    try:
        line : str = input("������� ������ (�������, ���, ��������, ��� ��������): ")
        raw_data : list = line.split()
        
        if len(raw_data) != 4: raise IncompleteDataError

        with open("file.txt", "a", encoding="UTF-8") as f:
            f.write(f"{raw_data[0]} {raw_data[1]} {raw_data[2]} {raw_data[3]}\n")
        print("������� ��������")

    except UnicodeError: print("������ ���������!")
    except FileNotFoundError: print("���� ��� ������ �� ������!")
    except IncompleteDataError: print("������� �� ��� ����������� ������")
    except KeyboardInterrupt:
        print("\n���� ��������!")
        break
