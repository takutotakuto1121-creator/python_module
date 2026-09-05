#!/usr/bin/env python3

import sys


def main() -> None:
    av = sys.argv
    ac = len(av)

    if ac == 1:
        print("usage ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    for file in av[1:]:
        print(f"Accessing file {file}")
        try:
            f = open(file)
            content = f.read()

            print("---")
            print()
            print(content)
            print()
            print("---")

            f.close()
            print(f"File '{file}' closed.")
        except OSError as e:
            print(f"Error opening file '{file}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
