# def show_menu():
#     print('1. Распечатать справочник'
#           '2. Найти телефон по фамилии'
#           '3. Изменить номер телефона'
#           '4. Удалить запись'
#           '5. Найти абонента по номеру телефона'
#           '6. Добавить абонента в справочник'
#           '7. Закончить работу', sep = '\n')
#     choice=int(input())
#     return choice

# def work_with_phonebook():
	

#     choice=show_menu()

#     phone_book=read_txt('phonebook.txt')

#     while (choice!=7):

#         if choice==1:
#             print_result(phone_book)
#         elif choice==2:
#             last_name=input('lastname ')
#             print(find_by_lastname(phone_book,last_name))
#         elif choice==3:
#             last_name=input('lastname ')
#             new_number=input('new  number ')
#             print(change_number(phone_book,last_name,new_number))
#         elif choice==4:
#             lastname=input('lastname ')
#             print(delete_by_lastname(phone_book,lastname))
#         elif choice==5:
#             number=input('number ')
#             print(find_by_number(phone_book,number))
#         elif choice==6:
#             user_data=input('new data ')
#             add_user(phone_book,user_data)
#             write_txt('phonebook.txt',phone_book)


#         choice=show_menu()

#         def read_txt(filename): 

#             phone_book=[]

#     fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	

#     with open(filename,'r', encoding='utf-8') as phb:

#         for line in phb:

#             	record = dict(zip(fields,    line.split(',')))
	     
#     data.append(record)	

#     return phone_book

# def write_txt(filename , phone_book):

#     with open('phonebook.txt','w',encoding='utf-8') as phout:

#         for i in range(len(phone_book)):

#             s=''
#             for v in phone_book[i].values():
#                 s+=v+','
#             phout.write(f'{s[:-1]}\n')



#             def write_txt(filename , phone_book):

#                 with open('phonebook.txt','w',encoding='utf-8') as phout:

#                  for i in range(len(phone_book)):

#                       s=''
#                  for v in phone_book[i].values():
#                      s+=v+','
#                 phout.write(f'{s[:-1]}\n')


import os, re


def phone_format(n):  # форматирование телефонного номера
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):  # Функция вывода телефонной книги в консоль
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Lastname        Name          Phone Numbers")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "lastName": lastName,
                "name": name,
                "phone": phone_format(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)


def showContacts(fileName):  # Функция открытия телефонной книги
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- press any key ---")


def addContact(fileName):  # Функция добавления нового контакта в телефонную книгу
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Input a Surname of Contact: ") + ","
        res += input("Input a Name of Contact: ") + ","
        res += input("Input a Phone Number of Contact: ")

        file.write(res + "\n")

    input("\nContact was successfully added!\n--- press any key ---")


def findContact(fileName):  # Функция поиска контактов в телефонной книге
    os.system("cls")
    target = input("Input Item of Contact for searching: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"There is no Contact with this Item '{target}'.")

    input("--- press any key ---")


def changeContact(fileName):  # Функция изменения информации в контакте
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Input Number of Contact for changing or 0 for return Main Menu: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Input new Lastname: ")
            newName = input("Input new Name: ")
            newPhone = input("Input new Phone: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nContact was successfully changed!")
                input("\n--- press any key ---")
        else:
            return


def deleteContact(fileName):  # Функция удаления контакта из телефонной книги
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Input Number of Contact for deleting or 0 for return Main Menu: ")
        )
        if numberContact != 0:
            print(f"Deleting record: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- press any key ---")


def drawInterface():  # Функция рисования интерфейса главного меню
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавить контакт")
    print(" [3] -- Найти контакт")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")


def main(file_name):  # Функция реализации главного меню
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите значение от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Cпасибо!")
            return


path = "phonebook.txt"

main(path)
