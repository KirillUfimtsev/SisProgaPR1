# coding=windows-1251
class IncompleteDataError(Exception):
    pass

while True:
    try:
        line : str = input("Введите данные (фамилия, имя, отчество, год рождения): ")
        data : list = line.split()
        
        if len(data) != 4: raise IncompleteDataError

        with open("file.txt", "a", encoding="UTF-8") as f:
            f.write(f"{data[0]} {data[1]} {data[2]} {data[3]}\n")
        print("Запись добавлена")

    except UnicodeError: print("Неверная кодировка файла")
    except FileNotFoundError: print("Такого файла нет")
    except IncompleteDataError: print("Не все данные заполнены!")
    except KeyboardInterrupt:
        print("\nВвод завершен!")
        break
