#!usr/bin/env python3

import math

def ft_is_base(c, base):
	for char in base:
		if c == char:
			return 1
	return 0

def ft_len(obj):
	count = 0
	for _ in obj:
		count += 1
	return count

def ft_float(str):
	i = 0
	sign = 1
	base = "0123456789"
	result = 0
	len = ft_len(str)
	map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	while i < len and (str[i] == ' ' or str[i] == '\t'):
		i += 1
	if i < len and str[i] == '-':
		sign = -1
		i += 1
	if i < len and str[i] == '+':
		i += 1
	while i < len and str[i] != '.':
		if ft_is_base(str[i], base):
			result = result*10 + map[str[i]]
			i += 1
		else:
			raise ValueError(f"could not convert string to float: {str}")
	if i < len and str[i] != '.':
		raise ValueError(f"could not convert string to float: {str}")
	elif i < len and str[i] == '.':
		divisor = 10
		i += 1
		while i < len:
			if ft_is_base(str[i], base):
				result = result + map[str[i]]/divisor
				divisor *= 10
				i += 1
			else:
				raise ValueError(f"could not convert string to float: {str}")
	return result*sign

def ft_split(str, c):
	part = ()
	current = ""
	for char in str:
		if char == c:
			part += (current,)
			current = ""
		else:
			current += char
	part += (current,)
	return part

def ft_count_c(str, c):
	count = 0
	for char in str:
		if char == c:
			count += 1
	return count

def get_player_pos():
	while (1):
		coordinate = ()
		line = input("Enter new coordinates as floats in format 'x,y,z': ")
		if ft_count_c(line, ',') != 2:
			print("Invalid syntax")
			continue
		part = ft_split(line, ',')
		for num in part:
			try:
				coordinate += (ft_float(num),)
			except ValueError as e:
				print(f"Error on parameter '{num}': {e}")
		if ft_len(coordinate) == 3:
			return coordinate

def get_distance(x, y, z):
	return math.sqrt(x**2 + y**2 + z**2)

def main():
	print("=== Game Coordinate System ===")
	print()

	print("Get a first set of coordinates")
	pos1 = get_player_pos()
	print(f"Got a first tuple: {pos1}")
	print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
	dist1 = round(get_distance(pos1[0], pos1[1], pos1[2]), 4)
	print(f"Distance to center: {dist1}\n")

	print("Get a sexond set of coordinates")
	pos2 = get_player_pos()
	x = pos1[0] - pos2[0]
	y = pos1[1] - pos2[1]
	z = pos1[2] - pos2[2]
	dist12 = round(get_distance(x, y, z), 4)
	print(f"Distance between the 2 sets of coordinates: {dist12}")

if __name__ == "__main__":
	main()

# if __name__ == "__main__":
# 	print(get_player_pos())

# if __name__ == "__main__":
# 	print(ft_float("123"))
# 	print(ft_float("+123"))
# 	print(ft_float("-123"))
# 	print(ft_float("123.456"))
# 	print(ft_float("+123.456"))
# 	print(ft_float("-123.456"))
# 	print(ft_float("abc"))