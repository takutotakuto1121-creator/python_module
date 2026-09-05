#!/usr/bin/env python3


import sys


def add_hash(content: str) -> str:
    new_content = ""
    for char in content:
        if char == "\n":
            new_content += "#\n"
        else:
            new_content += char
    if len(content) > 0 and content[len(content) - 1] != "\n":
        new_content += "#"
    return new_content


def strip_linebreak(content: str) -> str:
    new_content = ""
    for char in content:
        if char == "\n":
            pass
        else:
            new_content += char
    return new_content


def main() -> None:
    av = sys.argv
    ac = len(av)

    if ac == 1:
        print("usage ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")

    file = av[1]
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
        print(f"[STDERR]Error opening file '{file}': {e}", file=sys.stderr)
        sys.exit(1)

    print("Transform data:")
    new_content = add_hash(content)

    print("---")
    print()
    print(new_content)
    print()
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_file_origin = sys.stdin.readline()
    new_file = strip_linebreak(new_file_origin)
    if new_file == "":
        print("Not saving data.")
        sys.exit(0)
    try:
        f = open(new_file, "w")
    except OSError as e:
        print(f"[STDERR]Error opening file '{new_file}': {e}", file=sys.stderr)
        sys.exit(1)
    print(f"Saving data to '{new_file}'")
    f.write(new_content)
    print(f"Data saved in file '{new_file}'")
    f.close()


if __name__ == "__main__":
    main()
