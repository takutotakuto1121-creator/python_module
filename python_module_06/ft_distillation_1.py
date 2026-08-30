#!/usr/bin/env python3


import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using 'import alchemy' structure to access potions")
    strength = alchemy.strength_potion()
    heal = alchemy.heal()
    print(f"Testing strength_potion: {strength}")
    print(f"Testing heal alias: {heal}")
