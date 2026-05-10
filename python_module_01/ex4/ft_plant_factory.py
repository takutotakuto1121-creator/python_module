#!/usr/bin/env python3

class Plant:
	def __init__(self, name, height, p_age):
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

def ft_garden_security():
	print("=== Garden Security System ===")
	rose = Plant("Rose", 15, 10)
	print(f"Plant created: {rose._height:.1f}cm, {rose._p_age} days old\n")

	rose.set_height(25)
	print(f"Height updated: {rose._height}cm")

	rose.set_age(30)
	print(f"Age updated: {rose._p_age} days\n")

	rose.set_height(-3)
	rose.set_age(-1)
	print()
	print(f"Current state: {rose._name}: {rose._height:.1f}cm, {rose._p_age} days old")

if __name__ == "__main__":
		ft_garden_security()



		
	




