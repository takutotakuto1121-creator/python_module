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
            raise IndexError("No data to output")
        extract = self.storage.pop(0)
        current_rank = self.rank
        self.rank += 1
        return current_rank, extract


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for item in data:
                is_number = isinstance(item, (int, float))
                if isinstance(item, bool) or not is_number:
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | typing.Sequence[int | float]) -> None:
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

    def ingest(self, data: str | list[str]) -> None:
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
            return self._is_valid_entry(data)
        elif isinstance(data, list):
            for item in data:
                if not self._is_valid_entry(item):
                    return False
            return True
        else:
            return False

    @staticmethod
    def _is_valid_entry(item: typing.Any) -> bool:
        if not isinstance(item, dict):
            return False
        for key, value in item.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        elif isinstance(data, list):
            for entry in data:
                self.storage.append(self._format_entry(entry))
        else:
            self.storage.append(self._format_entry(data))

    @staticmethod
    def _format_entry(entry: dict[str, str]) -> str:
        return f"{entry['log_level']}: {entry['log_message']}"


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    bool_42 = numeric.validate(42)
    print(f"Trying to validate input '42': {bool_42}")
    numeric1 = NumericProcessor()
    bool_hello = numeric1.validate("Hello")
    print(f"Trying to validate input 'Hello': {bool_hello}")
    foo = "foo"
    numeric2 = NumericProcessor()
    print(
        f"Test invalid ingestion of string "
        f"'{foo}' without prior validation:"
    )
    try:
        numeric2.ingest(foo)  # type: ignore[arg-type]
    except ValueError as e:
        print(f"Got exception: {e}")
    numeric_data = [1, 2, 3, 4, 5]
    numeric3 = NumericProcessor()
    numeric3.validate(numeric_data)
    numeric3.ingest(numeric_data)
    print(f"Processing data: {numeric_data}")
    print("Extracting 3 values...")
    for _ in range(3):
        rank, extract = numeric3.output()
        print(f"Numeric value {rank}: {extract}")
    print()

    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    text.ingest(text_data)
    print("Extracting 1 value...")
    rank, extract = text.output()
    print(f"Text value {rank}: {extract}")
    print()

    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, extract = log.output()
        print(f"Log entry {rank}: {extract}")


if __name__ == "__main__":
    main()
