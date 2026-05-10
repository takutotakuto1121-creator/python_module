#!/usr/bin/env python3

class Plant:
	class Stats:
		def __init__(self):
			self.grow_count = 0
			self.age_count = 0
			self.show_count = 0

		def display(self):
			print(f"Stats: {self.grow_count} grow, {self.age_count} age, {self.show_count} show")

	
	def __init__(self, name, height, age):
		self._stats = self.Stats()
		self._name = name
		self._height = height
		self._age = age

	@classmethod

	def create_anonymous(cls):
		return cls("Unknown plant", 0, 0)

	def show(self):
		print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
		self._stats.show_count += 1

	def grow(self):
		self._height = round(self._height + 0.8, 1)
		self._stats.grow_count += 1

	def age(self):
		self._age += 1
		self._stats.age_count += 1

	@staticmethod
	def is_older_than_year(age):
		if age > 365:
			return True
		else:
			return False

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
	class TreeStats(Plant.Stats):
		def __init__(self):
			super().__init__()
			self.shade_count = 0

		def display(self):
			super().display()
			print(f"{self.shade_count} shade")

	def __init__(self, name, height, age, trunk_diameter):
		super().__init__(name, height, age)
		self._trunk_diameter = trunk_diameter
		self._stats = self.TreeStats()
	
	def produce_shade(self):
		print(f"Tre Oak now produce a shade of {self._height:.1f} long and {self._trunk_diameter:.1f}cm wide.")
		self._stats.shade_count += 1

	def show(self):
		super().show()
		print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


class Seed(Flower):
	def __init__(self, name, height, age, color):
		super().__init__(name, height, age, color)
		self._seed_count = 0
	
	def bloom(self):
		super().bloom()
		self._seed_count += 42

	def show(self):
		super().show()
		print(f"Seeds: {self._seed_count}")

def display_stats(plant):
	print(f"[statistics for {plant._name}]")
	plant._stats.display()

def main():
	print("=== Garden statistics ===")
	print("=== Check year-old")
	print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
	print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
	print()
	print("=== Flower")
	rose = Flower("Rose", 15, 10, "red")
	print("[statistics for Rose]")
	rose._stats.display()
	print("[asking the rose to grow and bloom]")
	rose.grow()
	rose.bloom()
	rose._stats.display()
	print()
	print("=== Tree")
	oak = Tree("Oak", 200, 365, 5)
	oak.show()
	print("[statistics for Oak]")
	oak._stats.display()
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	print("[statistics for Oak]")
	oak._stats.display()
	print()
	print("=== Seed")
	sunflower = Seed("Sunflower", 80, 45, "yellow")
	sunflower.show()
	print("[make sunflower grow, age and bloom]")
	sunflower.grow()
	sunflower.bloom()
	print("[statistics for Sunflower]")
	sunflower._stats.display()
	print()
	print("=== Anonymous")
	anonymous = Plant.create_anonymous()
	print("[statistic for Unknoen plant]")
	anonymous._stats.display()

if __name__ == "__main__":
	main()


