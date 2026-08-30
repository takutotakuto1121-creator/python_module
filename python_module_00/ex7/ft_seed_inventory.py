def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_display = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_display} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_display} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_display} seeds: convers {quantity} aquare meter")


if __name__ == "__main__":
    ft_seed_inventory("Tomato", 15, "packets")
    ft_seed_inventory("Carrot", 8, "grams")
    ft_seed_inventory("Lettuce", 12, "area")
