#!/usr/bin/env python3

def input_temperature(temp_str):
	return int(temp_str)

def test_temperature():
	print("=== Garden Temperature ===")
	print()
	test_data = ["25", "abc"]
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
