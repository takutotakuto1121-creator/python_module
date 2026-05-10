#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, age):
		self._name = name
		self._height = height
		self._age = age

	def show(self):
		print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

	def grow(self):
		self._height = round(self._height + 0.8, 1)

	def age(self):
		self._age += 1

	def set_height(self, height):
		if height < 0:
			print(f"{self._name}:  Error, height can't be negative")
			print("Height update rejected")
		else:
			self._height = height
	
	def set_age(self, age):
		if age < 0:
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")
		else:
			self._age = age

	def get_height(self):
		print(f"Height updated: {self._height}cm")

	def get_age(self):
		print(f"Age updated")

class Flower(Plant):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age)
		self._color = color
		self._isbloom = False
	
	def bloom(self):
		self._isbloom = True
	
	def show(self):
		super().show()
		print(f"Color: {self._color}")
		if self._isbloom:
			print("Rose is blooming beautifully!")
		else:
			print("Rose has not bloomed yet")

class Tree(Plant):
	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self._trunk_diameter = trunk_diameter
	
	def produce_shade(self):
		print(f"Tre Oak now produce a shade of {self._height:.1f} long and {self._trunk_diameter:.1f}cm wide.")

	def show(self):
		super().show()
		print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

class Vegetable(Plant):
	def __init__(self, name, height, age, harvest_season):
		super().__init__(name, height, age)
		self._harvest_season = harvest_season
		self._nutritional_value = 0

	def age(self):
		super().age
		self._nutritional_value += 1

	def grow(self):
		super().grow
		self._nutritional_value += 10

	def show(self):
		super().show()
		print(f"Harvest Season: {self._harvest_season}")
		print(f"Nutritional value: {self._nutritional_value}")

def ft_plant_types():
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose = Flower ("Rose", 15, 10, "red")
	rose.show()
	rose.bloom()
	print("[asking the rose to bloom]")
	rose.show()
	print()

	print("=== Tree")
	oak = Tree("Oak", 200, 365, 5)
	oak.show()
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	print()
	
	print("=== Vegetable")
	tomato = Vegetable("Tomato", 200, 5, "April")
	print("[make tomato grow and age for 20 days]")
	tomato.grow()
	for i in range(20):
		tomato.age()
	tomato.show()

if __name__ == "__main__":
	ft_plant_types()





	

