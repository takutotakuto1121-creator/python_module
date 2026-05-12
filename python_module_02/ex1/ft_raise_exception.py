#!/usr/bin/env python3

def input_temperature(temp_str):
	nb = int(temp_str)
	if nb > 40:
		raise ValueError(f"{nb}°C is too hot for plants (max 40°C)")
	elif nb < 0:
		raise ValueError(f"{nb}°C is too cold for plants (min 0°C)")
	else:
		return nb

def test_temperature():
	print("=== Garden Temperature Checker ===")
	print()
	test_data = ["25", "abc", "100", "-50"]
	for data in test_data:
		print(f"Input data is '{data}'")
		try:
			temp = input_temperature(data)
			print(f"Temperature is now {data}°C")
		except ValueError as e:
			print(f"Caught input_temperature error: {e}")
		print()
	print("ALL tests completed - program didn't crash!")

if __name__ == "__main__":
	test_temperature()
