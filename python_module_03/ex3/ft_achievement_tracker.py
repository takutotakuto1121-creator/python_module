#!usr/bin/env python3

import random

def ft_set_to_list(set):
	result = []
	for item in set:
		result += [item]
	return result

def gen_player_achievements():
	achievements =set( {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',\
					'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',\
					'Untouchable', 'Sharp Mind', 'Boss Slayer'})
	ac_len = len(achievements)
	num = random.randint(1, ac_len)
	part = random.sample(ft_set_to_list(achievements), num)
	return set(part)

def main():
	achievements =set( {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor',\
					'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme',\
					'Untouchable', 'Sharp Mind', 'Boss Slayer'})
	
	alice = gen_player_achievements()
	bob = gen_player_achievements()
	charlie = gen_player_achievements()
	dylan = gen_player_achievements()

	print("=== Achievement Tracker System ===\n")
	print(f"Player Alice: {alice}")
	print(f"Player Bob: {bob}")
	print(f"Player Charlie: {charlie}")
	print(f"Player Dylan: {dylan}")
	print(f"ALl distinct achievements: {achievements}\n")

	common = alice.intersection(bob, charlie, dylan)
	print(f"Common achievements: {common}\n")

	only_alice = alice.difference(bob, charlie, dylan)
	only_bob = bob.difference(alice, charlie, dylan)
	only_charlie = charlie.difference(alice, bob, dylan)
	only_dylan = dylan.difference(alice, bob, dylan)

	print(f"Only Alice has: {only_alice}")
	print(f"Only Bob has: {only_bob}")
	print(f"Only Charlie has: {only_charlie}")
	print(f"Only Dylan has: {only_dylan}\n")

	miss_alice = achievements.difference(alice)
	miss_bob = achievements.difference(bob)
	miss_charlie = achievements.difference(charlie)
	miss_dylan = achievements.difference(dylan)

	print(f"Alice is missing: {miss_alice}")
	print(f"Bob is missing: {miss_bob}")
	print(f"Charlie is missing: {miss_charlie}")
	print(f"Dylan is missing: {miss_dylan}")

if __name__ == "__main__":
	main()

