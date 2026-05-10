def ft_print_age():
	age = input("Enter plant age in days: ")
	if int(age) > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")

ft_print_age()