#!/usr/bin/env python3


from elements import create_water


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print(
        "Using 'from elements import create_water' "
        "structure to access elements.py"
    )
    water = create_water()
    print(f"Testing create_water: {water}")
