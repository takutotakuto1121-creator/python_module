#!bin/usr/env python3

import random

def ft_capitalize(strs):
	map = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
        'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
        's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
        'y': 'Y', 'z': 'Z'
    }

	result = []
	for str in strs:
		if str == "":
			result += [str]
		elif 'a' <= str[0] <= 'z':
			result += [map[str[0]] + str[1:]]
		else:
			result += [str]
	return result

def make_capitalized_only(strs):
	map = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
        'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
        's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
        'y': 'Y', 'z': 'Z'
    }

	result = []
	for str in strs:
		if str != "":
			if 'A' <= str[0] <= 'Z':
				result += [str]
	return result

def make_dict(strs):
	dict = {}
	for i in range(len(players_capitalized)):
		dict += {str[i]:random.randint(1, 1000)}
	return dict, nums

def make_dict_high(dict, ave):
	dict_high = {}
	for key in dict:
		if dict[key] > ave:
			dict_high += {key:dict[key]}
	return (dict_high)

def main():
	print("=== Game Data Alchemist ===")
	print()

	players_init = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'John', 'kevin', 'Liam']
	players_capitalized = ft_capitalize(players_init)
	players_capitalized_only = make_capitalized_only(players_init)
	print(f"Initial list of players: {players_init}")
	print(f"New list with all names capitalized: {players_capitalized}")
	print(f"New list of capitalized names only: {players_capitalized_only}")
	print()

	dict = make_dict(players_capitalized)
	print(f"Score dict: {dict}")
	total = 0
	for key in dict:
		total += sum(dict[key])
	ave = round(total/len(dict), 2)
	print(f"Score average is {ave}")

	dict_high = make_dict_high(dict, ave)
	print(f"High scores: {dict_high}")

if __name__ == "__main__":
	main()
