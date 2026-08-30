#!/usr/bin/env python3


from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon
from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()


if __name__ == "__main__":
    print("=== Testing factory ===")
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    flameling = flame_factory.create_base()
    pyrodon = flame_factory.create_evolved()
    aquabub = aqua_factory.create_base()
    torragon = aqua_factory.create_evolved()
    print(flameling.describe())
    print(flameling.attack())
    print()
    print(pyrodon.describe())
    print(pyrodon.attack())
    print()
    print(aquabub.describe())
    print(aquabub.attack())
    print()
    print(torragon.describe())
    print(torragon.attack())
