#!/usr/bin/env python3

import abc
import typing

class DataProcessor(abc.ABC):
	def __init__(self) -> None:
		self.storage: list[str] = []
		self.rank: int = 0

	@abc.abstractmethod
	def validate(self, data: typing.Any) -> bool:
		pass

	@abc.abstractmethod
	def ingest(self, data: typing.Any) -> None:
		pass

	def output(self) -> tuple[int, str]:
		if not self.storage:
			raise IndexError("NO data to output")
		extract = self.storage.pop(0)
		current_rank = self.rank
		self.rank += 1
		return current_rank, extract


class NumericProcesor(DataProcessor):
	def validate(self, data: typing.Any) -> bool:
		if isinstance(data, (int, float)):
			return True
		elif isinstance(data, list):
			for item in data:
				if not isinstance(item, (int, float)):
					return False
			return True
		else:
			return False

	def ingest(self, data: typing.Any) -> None:
		if not self.validate(data):
			raise ValueError("Improper numeric data")
		elif isinstance(data, list):
			for item in data:
				self.storage.append(str(item))
		else:
			self.storage.append(str(data))


class TextProcessor(DataProcessor):
	def validate(self, data: typing.Any) -> bool:
		if isinstance(data, str):
			return True
		elif isinstance(data, list):
			for item in data:
				if not isinstance(item, str):
					return False
			return True
		else:
			return False

	def ingest(self, data: typing.Any) -> None:
		if not self.validate(data):
			raise ValueError("Improper text data")
		elif isinstance(data, list):
			for item in data:
				self.storage.append(item)
		else:
			self.storage.append(data)

class LogProcessor(DataProcessor):
	def validate(self, data: typing.Any) -> bool:
		if isinstance(data, dict):
			return True
		elif isinstance(data, list):
			for item in data:
				if not isinstance(item, dict):
					return False
			return True
		else:
			return False

	def ingest(self, data: typing.Any) -> None:
		if not self.validate(data):
			raise ValueError("Improper log data")
		elif isinstance(data, list):
			for item in data:
				self.storage.append(item)
		else:
			self.storage.append(data)

def main():
	print("=== Code Nexus - Data Processor ===")
	print()
	print("Testing Numeric Processor...")
	numeric = NumericProcesor()
	bool_42 = numeric.validate(42)
	print(f"Trying to validate input '42': {bool_42}")
	numeric1 = NumericProcesor()
	bool_hello = numeric1.validate("Hello")
	print(f"Trying to validate input '42': {bool_hello}")
	foo = "foo"
	numeric2 = NumericProcesor()
	print(f"Test invalid ingestion of string '{foo}' without prior validation:")
	try:
		numeric2.ingest(foo)
	except ValueError as e:
		print(f"Got exception: {e}")
	data = [1, 2, 3, 4, 5]
	numeric3 = NumericProcesor()
	numeric3.validate(data)
	numeric3.ingest(data)
	print("Extracting 3 values...")
	for _ in range(3):
		rank, extract = numeric3.output()
		print(f"Numeric value {rank}: {extract}")
	print()

	print("Testing Text Processor...")
	text = TextProcessor()
	print(f"Trying to validate input '42': {text.validate(42)}")
	data = ['Hello', 'Nexus', 'World']
	print(f"Processing data: {data}")
	text.ingest(data)
	print("Extracting 1 value...")
	rank, extract = text.output()
	print(f"Text value {rank}: {extract}")

	print("Testing Log Processor...")
	log = LogProcessor()
	print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
	data = [{"log_level": "Notice", "log_message": "Connextion to server"}, {"log_level": "Error", "log_message": "Unauthorized access!!"}]
	print(f"Proccesing data: {data}")
	log.ingest(data)
	print("Extracting 2 values...")
	for _ in range(2):
		rank, extract = log.output()
		print(f"Log entry {rank}: {extract['log_level']}: {extract['log_message']}")

if __name__ == "__main__":
	main()


