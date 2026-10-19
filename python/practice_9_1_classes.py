"""Практичне завдання 9.1. Класи та об'єкти (завдання 1-4)."""

from math import gcd


class Person:
    """Завдання 1: Людина."""

    def __init__(self):
        self.full_name = ""
        self.birth_date = ""
        self.phone = ""
        self.city = ""
        self.country = ""
        self.address = ""

    def input_data(self):
        self.full_name = input("ПІБ: ")
        self.birth_date = input("Дата народження: ")
        self.phone = input("Телефон: ")
        self.city = input("Місто: ")
        self.country = input("Країна: ")
        self.address = input("Домашня адреса: ")

    def print_data(self):
        print(f"ПІБ: {self.full_name}\nДата народження: {self.birth_date}\n"
              f"Телефон: {self.phone}\nМісто: {self.city}\nКраїна: {self.country}\n"
              f"Адреса: {self.address}")

    def age(self, today_year=2026):
        """Додаткова операція: вік за роком у кінці дати (дд.мм.рррр)."""
        return today_year - int(self.birth_date.split(".")[-1])


class City:
    """Завдання 2: Місто."""

    def __init__(self):
        self.name = ""
        self.region = ""
        self.country = ""
        self.population = 0
        self.postal_code = ""
        self.phone_code = ""

    def input_data(self):
        self.name = input("Назва міста: ")
        self.region = input("Регіон: ")
        self.country = input("Країна: ")
        self.population = int(input("Кількість жителів: "))
        self.postal_code = input("Поштовий індекс: ")
        self.phone_code = input("Телефонний код: ")

    def print_data(self):
        print(f"{self.name}, {self.region}, {self.country}; жителів: {self.population}; "
              f"індекс: {self.postal_code}; код: {self.phone_code}")

    def is_big(self):
        return self.population >= 1_000_000


class Country:
    """Завдання 3: Країна."""

    def __init__(self):
        self.name = ""
        self.continent = ""
        self.population = 0
        self.phone_code = ""
        self.capital = ""
        self.cities = []

    def input_data(self):
        self.name = input("Назва країни: ")
        self.continent = input("Континент: ")
        self.population = int(input("Кількість жителів: "))
        self.phone_code = input("Телефонний код: ")
        self.capital = input("Столиця: ")
        self.cities = [c.strip() for c in input("Міста через кому: ").split(",") if c.strip()]

    def print_data(self):
        print(f"{self.name} ({self.continent}); жителів: {self.population}; "
              f"код: {self.phone_code}; столиця: {self.capital}; міста: {', '.join(self.cities)}")

    def add_city(self, city):
        self.cities.append(city)


class Fraction:
    """Завдання 4: Дріб з арифметичними операціями."""

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def input_data(self):
        self.numerator = int(input("Чисельник: "))
        self.denominator = int(input("Знаменник: "))
        if self.denominator == 0:
            raise ValueError("Знаменник не може бути нулем")

    def print_data(self):
        print(f"{self.numerator}/{self.denominator}")

    def reduce(self):
        d = gcd(self.numerator, self.denominator) or 1
        return Fraction(self.numerator // d, self.denominator // d)

    def add(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator).reduce()

    def subtract(self, other):
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator).reduce()

    def multiply(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator).reduce()

    def divide(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator).reduce()


def main():
    print("Завдання 1")
    p = Person()
    p.input_data()
    p.print_data()

    print("\nЗавдання 2")
    c = City()
    c.input_data()
    c.print_data()

    print("\nЗавдання 3")
    country = Country()
    country.input_data()
    country.print_data()

    print("\nЗавдання 4")
    a, b = Fraction(), Fraction()
    a.input_data()
    b.input_data()
    for sign, result in (("+", a.add(b)), ("-", a.subtract(b)),
                         ("*", a.multiply(b)), ("/", a.divide(b))):
        print(f"{a.numerator}/{a.denominator} {sign} {b.numerator}/{b.denominator} = ", end="")
        result.print_data()


if __name__ == "__main__":
    main()
