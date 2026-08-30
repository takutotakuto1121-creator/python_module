#!/usr/bin/env python3


from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    if ingredients.lower() in dark_spell_allowed_ingredients():
        return f"{ingredients} -> VALID"
    else:
        return f"{ingredients} -> INVALID"
