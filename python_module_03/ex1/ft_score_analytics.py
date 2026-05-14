#!usr/bin/env python3

import sys

def score_analize():
	i = 1
	j = 0
	argc = len(sys.argv)
	nm = [None]*argc
	while i < argc:
		try :
			nm[j] = int(sys.argv[i])
			j += 1
		except ValueError:
			print(f"Invalid parameter: '{sys.argv[i]}'")
		i += 1
	if j == 0:
		print("No scores provided. Usage: python3 ft_scores_analytics.py <score1> <score2> ...")
	else:
		scores = nm[:j]
		total = sum(scores)
		average = total/(argc - 1)
		high = max(scores)
		low = min(scores)
		range = high - low
		print("=== Player Score Analytics ===")
		print(f"Score processed : {scores}")
		print(f"Toral players: {argc - 1}")
		print(f"Total score: {total}")
		print(f"Average score: {average:.1f}")
		print(f"High score: {high}")
		print(f"Low score: {low}")
		print(f"Score range: {range}")

if __name__ == "__main__":
	score_analize()