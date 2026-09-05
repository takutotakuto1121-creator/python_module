#!/usr/bin/env python3

from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    return f"Healing potion brewd with '[{create_earth()}]' " \
            f"and '[{create_air()}]'"


def strength_potion() -> str:
    return f"Strength potion brewed with '[{create_fire()}]' " \
            f"and '[{create_water()}]'"


def weaken_potion() -> str:
    return f"Weaken potion brewed with '[{create_fire()}]' " \
            f", '[{create_water()}] ', '[{create_earth()}]'" \
            f"and, '[{create_air()}]'"
