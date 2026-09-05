#!/usr/bin/env python3


from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    print("=== Testing Creature with healing capability ===")

    healingfactory = HealingCreatureFactory()
    sproutling = healingfactory.create_base()
    bloomelle = healingfactory.create_evolved()

    print("= base =")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print("= evolved =")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())
    print()

    print("=== Testing Creature with transform capability ===")
    transformingfactory = TransformCreatureFactory()
    shiftling = transformingfactory.create_base()
    morphagon = transformingfactory.create_evolved()

    print("= base =")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print("= evolved =")
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())
