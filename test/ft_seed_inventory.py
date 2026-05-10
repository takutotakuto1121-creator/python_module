def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_display = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_display} seeds: {quantity} packets available")
    if unit == "grams":
        print(f"{seed_display} seeds: {quantity} grams total")
    if unit == "area":
        print(f"{seed_display} seeds: convers {quantity} aquare meter")

ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
