#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    players_init = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam',
    ]
    print(f"Initial list of players: {players_init}")
    upper_map = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
        'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
        's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
        'y': 'Y', 'z': 'Z'
    }
    players_capitalized = [
        upper_map[name[0]] + name[1:]
        if name != "" and 'a' <= name[0] <= 'z' else name
        for name in players_init
    ]
    print(f"New list with all names capitalized: {players_capitalized}")
    players_capitalized_only = [
        name for name in players_init if name != "" and 'A' <= name[0] <= 'Z'
    ]
    print(f"New list of capitalized names only: {players_capitalized_only}")
    print()
    score_dict = {
        name: random.randint(0, 1000) for name in players_capitalized
    }
    print(f"Score dict: {score_dict}")
    total = sum([score_dict[key] for key in score_dict])
    ave = round(total / len(score_dict), 2)
    print(f"Score average is {ave}")
    dict_high = {
        key: score_dict[key] for key in score_dict if score_dict[key] > ave
    }
    print(f"High scores: {dict_high}")


if __name__ == "__main__":
    main()
