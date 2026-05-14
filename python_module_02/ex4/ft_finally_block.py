#!/usr/bin/env python3

class GardenError(Exception):
	def __init__(self, message = "Unknown garden error"):
		self.message = message
		super().__init__(self.message)

class PlantError(GardenError):
	def __init__(self, message = "Unknown plant error"):
		self.message = message
		super().__init__(self.message)

def water_plant(plant_name):
	if plant_name == plant_name.capitalize():
		print(f"Watering {plant_name} [OK]")
	else:
		raise PlantError("Invalid plant name to water: '{plant_name}'")

def test_watering_system():
	print("=== Garden Watering System ===\n")

	print("Testing valid plants...")
	print("Opening watering system")
	plants = ["Tomato", "Lettuce", "Carrots"]
	try:
		for plant in plants:
			water_plant(plant)
	except PlantError as e:
		print("Caught PlantError: {e}")
		print(".. ending tests and returning to main")
		return
	finally:
		print("Closing watering system")

	print("\nTesting valid plants...")
	print("Opening watering system")
	plants = ["Tomato", "lettuce", "Carrots"]
	try:
		for plant in plants:
			water_plant(plant)
	except PlantError as e:
		print("Caught PlantError: {e}")
		print(".. ending tests and returning to main")
		return
	finally:
		print("Closing watering system")
		print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
	test_watering_system()
