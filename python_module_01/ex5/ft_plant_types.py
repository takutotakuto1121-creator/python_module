#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}:  Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self) -> None:
        print(f"Height updated: {self._height}cm")

    def get_age(self) -> None:
        print(f"Age updated: {self._age} days")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._isbloom = False

    def bloom(self) -> None:
        self._isbloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._isbloom is True:
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree Oak now produce a shade of \
{self._height:.1f} long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow()
    for i in range(20):
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
