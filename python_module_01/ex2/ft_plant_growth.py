#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, p_age: int) -> None:
        self.name = name
        self.height = height
        self.p_age = p_age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.p_age} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.p_age += 1


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {i} ===")
        rose.show()
    print("Growth this week: 5.6cm")


if __name__ == "__main__":
    ft_plant_growth()


{

}

struct.value
