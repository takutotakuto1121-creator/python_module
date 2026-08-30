def ft_print_age() -> None:
    age = input("Enter plant age in days: ")
    if int(age) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


if __name__ == "__main__":
    ft_print_age()
