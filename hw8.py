# Функция для добавления нового контакта в файл справочника
def add_new_contact(filename, name, phone_number, comment):
    if not name.strip() or not phone_number.strip():
        print("Имя и номер телефона не могут быть пустыми. Контакт не будет добавлен.")
        return
    contacts = read_contacts(filename)
    contacts[name] = {"phone_number": phone_number, "comment": comment}
    write_contacts(filename, contacts)
    print(f"Контакт {name} добавлен в справочник.")


# Функция для просмотра всех контактов из файла справочника
def view_contacts(filename):
    contacts = read_contacts(filename)
    if contacts:
        print("\nХороший выбор!")
        print("\nВот кого удалось найти:")
        for name, data in contacts.items():
            print(f"Имя: {name}")
            print(f'Номер телефона: {data["phone_number"]}')
            print(f'Комментарий: {data["comment"]}')
            print("-" * 30)
    else:
        print("Справочник пуст.")


# Функция для удаления контакта по имени
def delete_contact(filename, name):
    contacts = read_contacts(filename)
    if name in contacts:
        del contacts[name]
        write_contacts(filename, contacts)
        print(f"Контакт {name} удален из справочника.")
    else:
        print(f"Контакт {name} не найден в справочнике.")


# Функция для чтения контактов из файла справочника
def read_contacts(filename):
    contacts = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" - ")
                if len(parts) == 3:
                    name, phone_number, comment = parts
                    contacts[name] = {"phone_number": phone_number, "comment": comment}
    except FileNotFoundError:
        pass
    return contacts


# Функция для записи контактов в файл справочника
def write_contacts(filename, contacts):
    with open(filename, "w", encoding="utf-8") as f:
        for name, data in contacts.items():
            f.write(f'{name} - {data["phone_number"]} - {data["comment"]}\n')


# Функция для обновления существующего контакта в файле справочника
def update_contact(filename, old_name, new_name, phone_number, comment):
    contacts = read_contacts(filename)
    if old_name in contacts:
        updated_contact = {"phone_number": phone_number, "comment": comment}
        if old_name != new_name:
            del contacts[old_name]
            contacts[new_name] = updated_contact
            print(
                f"Контакт {old_name} переименован в {new_name} и обновлен в справочнике."
            )
        else:
            contacts[old_name] = updated_contact
            print(f"Контакт {old_name} обновлен в справочнике.")
        write_contacts(filename, contacts)
    else:
        print(
            f"Контакт {old_name} не найден в справочнике. Вы можете добавить новый контакт."
        )


# Главная функция
def main():
    filename = "contacts.txt"

    while True:
        print("\nПеред Вами справочник контактов! Что будете делать?")
        print("Есть несколько действий на Ваш выбор:\n")
        print("1. Добавить новый контакт")
        print("2. Обновить существующий контакт")
        print("3. Просмотреть все контакты")
        print("4. Удалить контакт")
        print("5. Сбежать!")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            print("\nКого добавляем?")
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            comment = input("Введите комментарий: ")
            add_new_contact(filename, name, phone_number, comment)
        elif choice == "2":
            print("\nКого изменяем?")
            old_name = input("Введите имя контакта для обновления: ")
            new_name = input(
                "Введите новое имя (или оставьте пустым, чтобы оставить без изменений): "
            )
            phone_number = input("Введите новый номер телефона: ")
            comment = input("Введите новый комментарий: ")
            if not new_name:
                new_name = old_name
            update_contact(filename, old_name, new_name, phone_number, comment)
        elif choice == "3":
            view_contacts(filename)
        elif choice == "4":
            print("\nКого удаляем?")
            name = input("Введите имя контакта для удаления: ")
            delete_contact(filename, name)
        elif choice == "5":
            confirm = input("Вы уверены, что хотите выйти? (y/n): ")
            if confirm.lower() == "y" or confirm.lower() == "у":
                print("Поздравляю, вы спаслись!")
                print("Спасибо, что воспользовались справочником!")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")


# Очистка консоли
import os

os.system("cls" if os.name == "nt" else "clear")

# Вызов главного меню
if __name__ == "__main__":
    main()
