"""Практичне завдання 4.5. Генератори, функції вищого порядку, декоратори, частина 2."""


# Завдання 1
def primes_in_range(start, end):
    """Генератор: усі прості числа в діапазоні [start, end]."""
    for n in range(max(start, 2), end + 1):
        if all(n % d for d in range(2, int(n ** 0.5) + 1)):
            yield n


# Завдання 2
def armstrong_numbers(start, end):
    """Генератор: числа Армстронга в діапазоні [start, end]."""
    for n in range(max(start, 1), end + 1):
        digits = str(n)
        if n == sum(int(d) ** len(digits) for d in digits):
            yield n


# Завдання 3 (функції вищого порядку)
def find_min(items):
    result = items[0]
    for item in items[1:]:
        if item < result:
            result = item
    return result


def find_max(items):
    result = items[0]
    for item in items[1:]:
        if item > result:
            result = item
    return result


def find_min_or_max(list_to_check, function_to_call):
    return function_to_call(list_to_check)


# Завдання 4: піца, збирається декораторами
def pizza_base():
    return ["тісто", "томатний соус"]


def with_ingredients(*ingredients):
    """Декоратор-фабрика: додає інгредієнти до піци."""
    def decorator(func):
        def wrapper():
            return func() + list(ingredients)
        return wrapper
    return decorator


def named(name):
    """Декоратор: підписує піцу назвою та виводить склад."""
    def decorator(func):
        def wrapper():
            ingredients = func()
            print(f"Піца «{name}»: {', '.join(ingredients)}")
            return ingredients
        return wrapper
    return decorator


@named("Маргарита")
@with_ingredients("моцарела", "базилік")
def margherita():
    return pizza_base()


@named("Чотири сири")
@with_ingredients("моцарела", "горгонзола", "пармезан", "дор блю")
def four_cheeses():
    return pizza_base()


@named("Капричоза")
@with_ingredients("моцарела", "шинка", "печериці", "артишоки", "оливки")
def capricciosa():
    return pizza_base()


@named("Гавайська")
@with_ingredients("моцарела", "шинка", "ананас")
def hawaiian():
    return pizza_base()


def main():
    print("Завдання 1:", list(primes_in_range(1, 50)))
    print("Завдання 2:", list(armstrong_numbers(1, 10000)))

    print("Завдання 3:")
    numbers = [14, 3, 99, -5, 42, 7]
    print("Список:", numbers)
    choice = input("Що знайти (мінімум/максимум): ").strip().lower() or "мінімум"
    func = find_min if choice.startswith("мін") else find_max
    print("Результат:", find_min_or_max(numbers, func))

    print("Завдання 4:")
    for pizza in (margherita, four_cheeses, capricciosa, hawaiian):
        pizza()


if __name__ == "__main__":
    main()
