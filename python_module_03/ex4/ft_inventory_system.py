#!usr/bin/env python3

import sys

class RedundantError(Exception):
	def __init__(self):
		super().__init__()

def ft_is_base(c, base):
	for char in base:
		if c == char:
			return 1
	return 0

def ft_int(str):
	i = 0
	sign = 1
	base = "0123456789"
	result = 0
	len_s = len(str)
	map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	while i < len_s and (str[i] == ' ' or str[i] == '\t'):
		i += 1
	if i < len_s and str[i] == '-':
		sign = -1
		i += 1
	if i < len_s and str[i] == '+':
		i += 1
	while i < len_s:
		if ft_is_base(str[i], base):
			result = result*10 + map[str[i]]
			i += 1
		else:
			raise ValueError(f"invalid literal for int() with base 10: '{str}'")
	return result*sign

def add_to_dict(dict, av):
	pos = 0
	flag = 0
	for char in av:
		if char == ':':
			flag = 1
			break
		pos += 1
	if flag == 0:
		print(f"Error - invalid parameter '{av}'")
	else:
		try:
			key = av[:pos]
			value = ft_int(av[pos + 1:])
			if key in dict:
				raise RedundantError
			dict.update({key:value})
		except ValueError as e:
			print(f"Quantity error for '{key}': {e}")
		except RedundantError as e:
			print(f"Redundant item '{key}' - discarding")

def get_inventory():
	av = sys.argv
	dict = {}
	for str in av[1:]:
		add_to_dict(dict, str)
	return dict

def main():
	print("=== Inventory System Analysis ===")
	dict = get_inventory()
	print(f"Got inventory: {dict}")
	item_s = dict.keys()
	item = list(item_s)
	print(f"Item list: {item}")
	value_s = dict.values()
	value = list(value_s)
	total = sum(value)
	print(f"Total quantiti of the 5 items: {total}")
	
	min = value[0]
	max = value[0]
	for key in item:
		print(f"Item {key} represents {round(dict[key]/total*100, 1)}%")
		if dict[key] < min:
			min = dict[key]
		if dict[key] > max:
			max = dict[key]

	print(f"Item most abundant: position with quantity {max}")
	print(f"Item least abundant: sword quantity {min}")
	
	dict.update({"magic_item": 1})
	print(f"Updated inventory: {dict}")
	
if __name__ == "__main__":
	main()
