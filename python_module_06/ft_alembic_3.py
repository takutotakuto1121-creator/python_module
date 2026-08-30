#!/usr/bin/env python3


from alchemy.elements import create_air


if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from alchemy.elements import create_air' structure"
    )
    air = create_air()
    print(f"Testing create_air: {air}")
