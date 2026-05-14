#!/usr/bin/env python3

class GardenError(Exception):
	def __init__(self, message = "Unknown garden error"):
		self.message = message
		super().__init__(self.message)

class PlantError(GardenError):
	def __init__(self, message = "Unknown plant error"):
		self.message = message
		super().__init__(self.message)

class WaterError(GardenError):
	def __init__(self, message = "Unknown water error"):
		self.message = message
		super().__init__(self.message)

def raise_errors():
	print("=== Custom Garden Errors Demo ===\n")

	print("=== Testing PlantError...")
	try:
		raise PlantError("The tomato plant is wilting!")
	except PlantError as e:
		print(f"Caught WaterError: {e}\n")

	print("=== Testing Water Error...")
	try:
		raise WaterError("Not enough water in the tank!")
	except WaterError as e:
		print(f"Caught Error: {e}\n")

	print("=== Testing catching all garden errors...")
	errors = [PlantError("The tomato plant is wilting!"),
				WaterError("Not enough water in the tank!")]
	for error in errors:
		try:
			raise error
		except GardenError as e:
			print(f"Caught GardenError: {e}")
	print()

	print("All custom error types work correctly!")

if __name__ == "__main__":
	raise_errors()
