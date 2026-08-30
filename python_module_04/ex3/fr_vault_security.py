#!/usr/bin/env python3


def secure_archive(file: str, mode: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if mode == "r":
        try:
            with open(file, mode) as f:
                data = f.read()
            return (True, data)
        except OSError as e:
            return (False, e.strerror if e.strerror
                    is not None else "Unknown Error")

    elif mode == "w":
        try:
            with open(file, mode) as f:
                f.write(content)
                return (True, content)
        except OSError as e:
            return (False, e.strerror if e.strerror
                    is not None else "Unknown Error")

    else:
        return (False, "Invalid mode")


if __name__ == "__main__":
    success, result = secure_archive("test.txt")
    print("=== Test1 Read exisiting file ===")
    print(success)
    print(result)
    print()

    success, result = secure_archive("non.txt")
    print("=== Test2 Read nonexisiting file ===")
    print(success)
    print(result)
    print()

    success, result = secure_archive("write.txt", mode="w",
                                     content="test3\ntest3")
    print("=== Test3-1 Write to file with w===")
    print(success)
    print(result)
    print()

    success, result = secure_archive("write.txt")
    print("=== Test3-2 Read file written by w ===")
    print(success)
    print(result)
    print()

    success, result = secure_archive("test.txt", mode="nonexist")
    print("=== Test4 Read with nonexisiting mode ===")
    print(success)
    print(result)
    print()
