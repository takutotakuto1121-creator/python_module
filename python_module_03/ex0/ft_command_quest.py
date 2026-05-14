#!usr/bin/env python3

import sys

def print_argv():
	argc = len(sys.argv)
	argv = sys.argv
	print("=== Command Quest ===")
	print(f"Program name: {argv[0]}")
	if argc == 1:
		print("No arguments provided!")
	else:
		print(f"Argument receives: {argc - 1}")
		i = 1
		while i < argc:
			print(f"Argument {i}: {argv[i]}")
			i += 1
	print(f"Total argument: {argc}")


if __name__ == "__main__":
	print_argv()
		

