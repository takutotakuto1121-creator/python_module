#!/usr/bin/env python3

import sys


def ft_int(s: str) -> int:
    digits = "0123456789"
    sign = 1
    index = 0
    result = 0

    digit_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }

    if len(s) == 0:
        raise ValueError("empty string")

    if s[index] == '+':
        sign = 1
        index += 1
    elif s[index] == '-':
        sign = -1
        index += 1
    elif s[index] in digits:
        pass
    else:
        raise ValueError("invalid string")

    for c in s[index:]:
        if c not in digits:
            raise ValueError("invalid string")
        else:
            result = result * 10 + digit_map[c]

    return sign * result


def score_analize() -> None:
    i = 1
    j = 0
    argc = len(sys.argv)
    nm: list[int] = [0] * argc
    print("=== Player Score Analytics ===")
    while i < argc:
        try:
            nm[j] = ft_int(sys.argv[i])
            j += 1
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if j == 0:
        print(
            "No scores provided. Usage: python3 "
            "ft_scores_analytics.py <score1> <score2> ..."
        )
    else:
        scores = nm[:j]
        total = sum(scores)
        average = total / (argc - 1)
        high = max(scores)
        low = min(scores)
        range = high - low
        print(f"Score processed : {scores}")
        print(f"Toral players: {argc - 1}")
        print(f"Total score: {total}")
        print(f"Average score: {average:.1f}")
        print(f"High score: {high}")
        print(f"Low score: {low}")
        print(f"Score range: {range}")


if __name__ == "__main__":
    score_analize()
