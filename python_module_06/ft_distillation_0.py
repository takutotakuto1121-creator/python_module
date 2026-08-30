#!/usr/bin/env python3


from alchemy.potions import healing_potion, strength_potion


if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    strength = strength_potion()
    print(f"Testing strength_potion: {strength}")
    healing = healing_potion()
    print(f"Testing healing_potion: {healing}")
