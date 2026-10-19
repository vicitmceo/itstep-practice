"""Практичне завдання 9.2. Конструктори та перевантаження методів (завдання 1-6).

У Python немає перевантаження за сигнатурою, тому емулюємо його стандартними
засобами: значення за замовчуванням, *args, functools.singledispatchmethod
та перевизначення операторів (__add__, __eq__, __str__ тощо).
"""

from functools import singledispatchmethod
from math import gcd


class Person:
    """Завдання 1: Людина з конструктором і перевантаженими методами."""

    def __init__(self, full_name="", birth_date="01.01.2000", phone="", city="", country="", address=""):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def __str__(self):
        return f"{self.full_name}, {self.birth_date}, {self.phone}, {self.city}, {self.country}, {self.address}"

    def __eq__(self, other):
        return isinstance(other, Person) and (self.full_name, self.birth_date) == (other.full_name, other.birth_date)

    def __hash__(self):
        return hash((self.full_name, self.birth_date))

    @singledispatchmethod
    def move(self, destination):
        raise TypeError("Очікується місто (str) або (місто, країна)")

    @move.register
    def _(self, destination: str):
        self.city = destination

    @move.register
    def _(self, destination: tuple):
        self.city, self.country = destination


class City:
    """Завдання 2: Місто."""

    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def __str__(self):
        return f"{self.name} ({self.region}, {self.country}), {self.population} жителів"

    def __eq__(self, other):
        return isinstance(other, City) and (self.name, self.country) == (other.name, other.country)

    def __lt__(self, other):
        return self.population < other.population

    def grow(self, amount=1000):
        """Збільшує населення на amount (за замовчуванням 1000)."""
        self.population += amount


class Country:
    """Завдання 3: Країна."""

    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=None):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = list(cities) if cities else []

    def __str__(self):
        return f"{self.name} ({self.continent}), столиця {self.capital}, міст: {len(self.cities)}"

    def __len__(self):
        return len(self.cities)

    def __contains__(self, city):
        return city in self.cities

    def __iadd__(self, city):
        self.cities.append(city)
        return self


class Fraction:
    """Завдання 4: Дріб; операції через перевантаження операторів."""

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем")
        d = gcd(numerator, denominator) or 1
        sign = -1 if denominator < 0 else 1
        self.numerator = sign * numerator // d
        self.denominator = sign * denominator // d

    @staticmethod
    def _coerce(value):
        return value if isinstance(value, Fraction) else Fraction(int(value), 1)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        o = self._coerce(other)
        return Fraction(self.numerator * o.denominator + o.numerator * self.denominator,
                        self.denominator * o.denominator)

    __radd__ = __add__

    def __sub__(self, other):
        o = self._coerce(other)
        return Fraction(self.numerator * o.denominator - o.numerator * self.denominator,
                        self.denominator * o.denominator)

    def __mul__(self, other):
        o = self._coerce(other)
        return Fraction(self.numerator * o.numerator, self.denominator * o.denominator)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self._coerce(other)
        if o.numerator == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return Fraction(self.numerator * o.denominator, self.denominator * o.numerator)

    def __eq__(self, other):
        o = self._coerce(other)
        return (self.numerator, self.denominator) == (o.numerator, o.denominator)

    def __lt__(self, other):
        o = self._coerce(other)
        return self.numerator * o.denominator < o.numerator * self.denominator

    def __float__(self):
        return self.numerator / self.denominator


class Watch:
    """Завдання 5: Годинник."""

    def __init__(self, model="", manufacturer="", year=2000, price=0.0, kind="наручний"):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.kind = kind

    @classmethod
    def from_input(cls):
        return cls(input("Модель: "), input("Виробник: "), int(input("Рік випуску: ")),
                   float(input("Ціна: ")), input("Тип (наручний, настінний...): "))

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year}), {self.kind}, {self.price} грн"

    def __eq__(self, other):
        return isinstance(other, Watch) and (self.model, self.manufacturer, self.year) == \
            (other.model, other.manufacturer, other.year)

    def __lt__(self, other):
        return self.price < other.price

    def discount(self, percent=10):
        """Знижка у відсотках (за замовчуванням 10)."""
        self.price = round(self.price * (100 - percent) / 100, 2)

    def age(self, current_year=2026):
        return current_year - self.year


class Website:
    """Завдання 6: Вебсайт."""

    def __init__(self, name="", address="", description=""):
        self.name = name
        self.address = address
        self.description = description

    @classmethod
    def from_input(cls):
        return cls(input("Назва: "), input("Адреса: "), input("Опис: "))

    def __str__(self):
        return f"{self.name} <{self.address}>: {self.description}"

    def __eq__(self, other):
        return isinstance(other, Website) and self.address == other.address

    def __hash__(self):
        return hash(self.address)

    def __len__(self):
        return len(self.description)

    def is_secure(self):
        return self.address.lower().startswith("https://")


def main():
    print("Завдання 1")
    p = Person("Іван Петренко", "12.05.1999", "+380501112233", "Київ", "Україна", "вул. Хрещатик, 1")
    print(p)
    p.move("Львів")
    print("Після переїзду до міста:", p.city)
    p.move(("Краків", "Польща"))
    print("Після переїзду з країною:", p.city, p.country)
    print("Порівняння:", p == Person("Іван Петренко", "12.05.1999"))

    print("\nЗавдання 2")
    kyiv, lviv = City("Київ", "Київська", "Україна", 2_950_000, "01001", "+38044"), City("Львів", "Львівська", "Україна", 720_000)
    print(kyiv, "|", lviv, "| Київ більший за Львів:", lviv < kyiv)
    lviv.grow()
    lviv.grow(5000)
    print("Населення Львова після росту:", lviv.population)

    print("\nЗавдання 3")
    ua = Country("Україна", "Європа", 38_000_000, "+380", "Київ", ["Київ", "Львів"])
    ua += "Одеса"
    print(ua, "| міст:", len(ua), "| є Одеса:", "Одеса" in ua)

    print("\nЗавдання 4")
    a, b = Fraction(1, 2), Fraction(3, 4)
    print(f"{a} + {b} = {a + b}; {a} - {b} = {a - b}; {a} * {b} = {a * b}; {a} / {b} = {a / b}")
    print("2 + 1/2 =", 2 + a, "| 1/2 < 3/4:", a < b, "| 2/4 == 1/2:", Fraction(2, 4) == a)

    print("\nЗавдання 5")
    w1 = Watch("Seamaster", "Omega", 2018, 85000.0, "наручний")
    w2 = Watch("Wall Classic", "Ikea", 2022, 800.0, "настінний")
    print(w1)
    print(w2)
    w1.discount()
    w2.discount(25)
    print("Після знижок:", w1.price, w2.price, "| w2 дешевший:", w2 < w1, "| вік w1:", w1.age())

    print("\nЗавдання 6")
    s1 = Website("Python", "https://python.org", "Офіційний сайт мови Python")
    s2 = Website("Старий сайт", "http://example.com", "Приклад")
    print(s1, "| захищений:", s1.is_secure())
    print(s2, "| захищений:", s2.is_secure(), "| однакові:", s1 == s2, "| довжина опису:", len(s2))


if __name__ == "__main__":
    main()
