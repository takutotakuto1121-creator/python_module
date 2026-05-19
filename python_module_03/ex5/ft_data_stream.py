#!/usr/bin/env python3

import typing
import random

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
	players = ['bob', 'alice', 'dylan', 'charlie']
	actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'release', 'use']

	while True:
		yield random.choice(players), random.choice(actions)

def consume_event(events: list) -> typing.Generator[tuple[str,str], None, None]:
	while len(events) > 0:
		events_len = len(events)
		index = random.randint(0, events_len - 1)
		event = events[index]
		events[:] = events[:index] + events[index + 1:]
		yield event

def main():
	print("=== Game Data Stream Processor")
	event_generator = gen_event()

	for i in range(1000):
		player, action = next(event_generator)
		print(f"Event {i}: Player {player} did action {action}")

	events = [next(event_generator) for _ in range(10)]
	print(f"Built list of 10 events: {events}")
	for event in consume_event(events):
		print(f"Got event from list: {event}")
		print(f"Remains in list: {events}")

if __name__ == "__main__":
	main()
