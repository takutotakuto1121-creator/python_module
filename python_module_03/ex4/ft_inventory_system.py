#!usr/bin/env python3

import sys

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
		key = av[:pos]
		value = ft_int(av[pos + 1:])
		dict.update({key:value})

def get_inventory():
	av = sys.argv
	ac = len(av)
	dict = {}
	for str in av:
		add_to_dict(dict, str)
	return dict

def main():
	print("=== Inventory System Analysis ===")
	dict = get_inventory()
	print(f"Got inventory: {dict}")
	item = dict.keys()
	print(f"Item list: {item}")
	value = dict.values()
	total = sum(value)
	print(f"Total quantiti of the 5 items: {total}")

if __name__ == "__main__":
	main()
