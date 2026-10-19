"""Практичне завдання 6.2. Множини та словники (завдання 1-6)."""

CITIES_A = {"Київ", "Львів", "Одеса", "Харків", "Дніпро"}
CITIES_B = {"Львів", "Одеса", "Полтава", "Вінниця", "Суми"}


def countries_menu(countries):
    """Завдання 1: додавання, видалення, пошук за символами, перевірка наявності."""
    menu = ("1 - додати країну\n2 - видалити країну\n3 - пошук за символами\n"
            "4 - чи є країна в множині\n5 - показати всі\n0 - вихід")
    while True:
        print(menu)
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            countries.add(input("Країна: ").strip())
        elif choice == "2":
            name = input("Країна: ").strip()
            if name in countries:
                countries.remove(name)
            else:
                print("Такої країни немає")
        elif choice == "3":
            part = input("Символи: ").strip().lower()
            found = sorted(c for c in countries if part in c.lower())
            print("Знайдено:", found if found else "нічого")
        elif choice == "4":
            print("Є" if input("Країна: ").strip() in countries else "Немає")
        elif choice == "5":
            print(sorted(countries))
        elif choice == "0" or choice == "":
            break


def common(a, b):
    """Завдання 2: назви, які є в обох множинах."""
    return a & b


def only_first(a, b):
    """Завдання 3: є в першій, немає в другій."""
    return a - b


def only_second(a, b):
    """Завдання 4: є в другій, немає в першій."""
    return b - a


def unique_for_each(a, b):
    """Завдання 5: унікальні для кожної множини (симетрична різниця)."""
    return a ^ b


def capitals_menu(capitals):
    """Завдання 6: словник «країна -> столиця»: додавання, видалення, пошук, заміна."""
    menu = ("1 - додати\n2 - видалити\n3 - знайти столицю\n4 - замінити столицю\n"
            "5 - показати всі\n0 - вихід")
    while True:
        print(menu)
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            capitals[input("Країна: ").strip()] = input("Столиця: ").strip()
        elif choice == "2":
            if capitals.pop(input("Країна: ").strip(), None) is None:
                print("Такої країни немає")
        elif choice == "3":
            country = input("Країна: ").strip()
            print(capitals.get(country, "Не знайдено"))
        elif choice == "4":
            country = input("Країна: ").strip()
            if country in capitals:
                capitals[country] = input("Нова столиця: ").strip()
            else:
                print("Такої країни немає")
        elif choice == "5":
            for country, capital in capitals.items():
                print(f"{country} -> {capital}")
        elif choice == "0" or choice == "":
            break


def main():
    print("Завдання 1")
    countries_menu({"Україна", "Польща", "Франція", "Італія"})

    print("\nМножина A:", sorted(CITIES_A))
    print("Множина B:", sorted(CITIES_B))
    print("Завдання 2, спільні:", sorted(common(CITIES_A, CITIES_B)))
    print("Завдання 3, тільки в A:", sorted(only_first(CITIES_A, CITIES_B)))
    print("Завдання 4, тільки в B:", sorted(only_second(CITIES_A, CITIES_B)))
    print("Завдання 5, унікальні:", sorted(unique_for_each(CITIES_A, CITIES_B)))

    print("\nЗавдання 6")
    capitals_menu({"Україна": "Київ", "Польща": "Варшава", "Франція": "Париж"})


if __name__ == "__main__":
    main()
