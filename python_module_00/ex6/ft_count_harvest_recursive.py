def ft_countdown(num: int) -> None:
    if num < 1:
        return
    print(f"Day {num}")
    ft_countdown(num - 1)


def ft_count_harvest_recursive() -> None:
    num = input("Days until harvest: ")
    ft_countdown(int(num))
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_recursive()
