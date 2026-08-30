def ft_water_reminder() -> None:
    last = input("Days since last watering: ")
    if int(last) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


if __name__ == "__main__":
    ft_water_reminder()
