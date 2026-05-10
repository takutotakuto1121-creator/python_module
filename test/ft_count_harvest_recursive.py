def ft_harvest_helper(current, total):
	if current > int(total):
		return
	print(f"Day {current}")
	ft_harvest_helper(current + 1, total)

def ft_count_harvest_recursive():
	total = input("Days until harvest: ")
	current = 1
	ft_harvest_helper(current, total)
	print("Harvest time!")

ft_count_harvest_recursive()
