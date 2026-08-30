#!/usr/bin/env python3

import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []
        self.rank: int = 0
        self.total_processed: int = 0

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
                self.total_processed += 1
        else:
            self.storage.append(str(data))
            self.total_processed += 1


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
                self.total_processed += 1
        else:
            self.storage.append(data)
            self.total_processed += 1


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
                self.total_processed += 1
        else:
            self.storage.append(data)
            self.total_processed += 1


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            flag = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    flag = True
                    break
            if not flag:
                print(
                    f"DataStream error - Can't process element in "
                    f"stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        for proc in self.processors:
            proc_name: str = proc.__class__.__name__
            total_processed: int = proc.total_processed
            total_remein: int = len(proc.storage)
            print(
                f"{proc_name}: total {total_processed} items processed, "
                f"remaining {total_remein} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    datastream = DataStream()
    datastream.print_processors_stats()
    print()
    numericprocessor = NumericProcesor()
    datastream.register_processor(numericprocessor)
    print("Registering Numeric Processor")
    print()
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil isconnected',
            },
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch}")
    print()
    datastream.process_stream(batch)
    print()
    datastream.print_processors_stats()
    print()
    textprocessor = TextProcessor()
    logprocessor = LogProcessor()
    datastream.register_processor(textprocessor)
    datastream.register_processor(logprocessor)
    print("Registering other data processors")
    datastream.process_stream(batch)
    print("Send the same batch again")
    datastream.print_processors_stats()
    print()
    print(
        "Consumue some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        rank, extract = numericprocessor.output()
    for _ in range(2):
        rank, extract = textprocessor.output()
    for _ in range(1):
        rank, extract = logprocessor.output()
    datastream.print_processors_stats()
