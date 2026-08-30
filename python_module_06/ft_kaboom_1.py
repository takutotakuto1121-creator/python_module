#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbokk.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire import dark_spellbook
    result = dark_spellbook.dark_spell_record("Curse", "bats and frogs")
    print(f"Testing record light spell: {result}")
