FILE_PATH = 'file.txt'

def read():
    with open(FILE_PATH, 'r') as f:
        i = 1
        for line in f:
            print(f"{i}: {line.strip()}")
            i += 1

def append():
    with open(FILE_PATH, 'a') as f:
        f.write(f"{input('Введите данные контакта: ')}\n")

def delete():
    with open(FILE_PATH) as f:
        lines = f.readlines()
        del lines[int(input()) - 1]
        for line in lines:
            f.write(line)
     
def search():
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
        search = input("Кого ищем?: ")
        i = 1
        for line in lines:
            if search.lower() in line.lower():
                print(f"{i}: {line.strip()}")
            i += 1

def change():
    with open(FILE_PATH, 'r+') as f:
        user_indexes = []
        lines = f.readlines()
        search = input("Введите данные контакта: ")
        i = 0
        for line in lines:
            if search.lower() in line.lower():
                user_indexes.append(i)
            i += 1
        print(f"Найдено совпадений: {len(user_indexes)}\n")
        for i in user_indexes:
            print(f"{i}: {lines[i].strip()}")
        num = int(input("\nВведите индекс контакта: "))
        while num >= len(lines):
            print('Некорректный индекс\n')
            num = int(input("Введите индекс контакта: "))
        del lines[num]
        lines.insert(num, f"{input('Введите новые данные: ')}\n")
        with open(FILE_PATH, 'w+') as f:
            for line in lines:
                f.write(line)

while (choice := int(input("\n1: Показать справочник\n2: Добавить контакт\n3: Редактировать контакт\n4: Удалить контакт\n5: Найти контакт\n6: Завершить работу\n\nВыберите номер функции: "))) != 6:
    match choice:
        case 1:
            read()
        case 2:
            append()
        case 3:
            change()
        case 4:
            delete()
        case 5:
            search()
        case 6:
            break
        case _: 
            print("\nФункции не существует\n")

