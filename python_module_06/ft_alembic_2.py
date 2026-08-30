#!/usr/bin/env python3


import alchemy.elements


if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements,py using "
        "'import alchemy.elements' structure"
    )
    earth = alchemy.elements.create_earth()
    print(f"Testing create_earth: {earth}")
