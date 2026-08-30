#!/usr/bin/env python3


import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    air = alchemy.create_air()
    print(f"Testing create_air: {air}")
    print("Now show that not all functions ca be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth")
    earth = alchemy.create_earth()
