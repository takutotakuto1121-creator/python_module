def ft_count_harvest_iterative() -> None:
    num = input("Days until havest: ")
    for i in range(1, int(num) + 1):
        print("Day", i)
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_iterative()
