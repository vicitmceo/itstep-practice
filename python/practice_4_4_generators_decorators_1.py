"""Практичне завдання 4.4. Генератори, функції вищого порядку, декоратори, частина 1."""

from datetime import datetime


# Завдання 1
def even_numbers(start, end):
    """Генератор: усі парні числа в діапазоні [start, end]."""
    first = start if start % 2 == 0 else start + 1
    for n in range(first, end + 1, 2):
        yield n


# Завдання 2
def values_in_range(items, start, end):
    """Генератор: значення зі списку, що потрапляють у діапазон [start, end]."""
    for item in items:
        if start <= item <= end:
            yield item


# Завдання 3 (функції вищого порядку)
def is_even(value):
    return value % 2 == 0


def is_odd(value):
    return value % 2 != 0


def check_value(value_to_check, function_to_call):
    """Перевіряє значення переданою функцією (парність або непарність)."""
    return function_to_call(value_to_check)


# Завдання 4: декорування без синтаксису @
def show_time():
    print(datetime.now().strftime("%H:%M"))


def stars_decorator(func):
    def wrapper():
        print("*" * 27)
        func()
        print("*" * 27)
    return wrapper


# Завдання 5: ще один декоратор, який додає елементи форматування
def frame_decorator(func):
    def wrapper():
        print("=" * 27)
        print("   Поточний час:")
        func()
        print("=" * 27)
    return wrapper


# Завдання 6: синтаксис декораторів
@stars_decorator
def show_time_with_syntax():
    print(datetime.now().strftime("%H:%M"))


def main():
    print("Завдання 1:", list(even_numbers(3, 20)))
    print("Завдання 2:", list(values_in_range([5, 12, 7, 30, 18, 2, 25], 10, 26)))

    print("Завдання 3:")
    choice = input("Що перевіряти (парність/непарність): ").strip().lower() or "парність"
    func = is_even if choice.startswith("пар") else is_odd
    value = int(input("Число: ") or 7)
    print(f"Результат для {value}: {check_value(value, func)}")

    print("Завдання 4:")
    decorated = stars_decorator(show_time)
    decorated()

    print("Завдання 5:")
    stars_decorator(frame_decorator(show_time))()

    print("Завдання 6:")
    show_time_with_syntax()


if __name__ == "__main__":
    main()
