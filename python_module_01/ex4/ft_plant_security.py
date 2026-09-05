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


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created:", end=" ")
    rose.show()

    print()
    rose.set_height(25)
    rose.get_height()

    rose.set_age(30)
    rose.get_age()

    print()
    rose.set_height(-3)
    rose.set_age(-1)
    print()
    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    ft_garden_security()
