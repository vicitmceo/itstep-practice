"""Практичне завдання 6.1. Кортежі (завдання 1-4)."""

FRUITS = ("banana", "apple", "bananamango", "mango", "strawberry-banana", "banana", "kiwi")
CARS = ("BMW", "Audi", "BMW", "Toyota", "Audi", "BMW", "Skoda")
NUMBERS = (5, 12, 7, 345, 22, 8, 1000, 99, 101, 4, 56, 789)


def count_exact(items, name):
    """Завдання 1: скільки разів назва зустрічається як окремий елемент кортежу."""
    return items.count(name)


def count_inside(items, name):
    """Завдання 2: скільки разів назва зустрічається як частина елементів
    (рахуємо кожне входження, в тому числі кілька в одному елементі)."""
    return sum(item.count(name) for item in items)


def replace_in_tuple(items, old, new):
    """Завдання 3: кортеж незмінний, тому будуємо новий. Збіг лише повний."""
    return tuple(new if item == old else item for item in items)


def digits_statistics(numbers):
    """Завдання 4: скільки елементів з однією, двома, трьома... цифрами."""
    stats = {}
    for n in numbers:
        digits = len(str(abs(n)))
        stats[digits] = stats.get(digits, 0) + 1
    return dict(sorted(stats.items()))


def main():
    print("Завдання 1")
    fruit = input("Введіть назву фрукта: ").strip() or "banana"
    print(f"'{fruit}' як окремий елемент: {count_exact(FRUITS, fruit)}")

    print("\nЗавдання 2")
    print(f"'{fruit}' як частина елементів: {count_inside(FRUITS, fruit)}")
    print("Для 'banana, apple, bananamango, mango, strawberry-banana':",
          count_inside(("banana", "apple", "bananamango", "mango", "strawberry-banana"), "banana"))

    print("\nЗавдання 3")
    print("Кортеж:", CARS)
    old = input("Яку назву замінити: ").strip() or "BMW"
    new = input("На яке слово: ").strip() or "Tesla"
    print("Результат:", replace_in_tuple(CARS, old, new))

    print("\nЗавдання 4")
    print("Кортеж:", NUMBERS)
    words = {1: "Одна цифра", 2: "Дві цифри", 3: "Три цифри", 4: "Чотири цифри"}
    for digits, count in digits_statistics(NUMBERS).items():
        print(f"{words.get(digits, str(digits) + ' цифр')} — {count} елементи(ів)")


if __name__ == "__main__":
    main()
