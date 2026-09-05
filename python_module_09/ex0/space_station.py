#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    info: dict = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.now(),
        "notes": (
            "add last_maintenance.\n"
            "don't take is_operational because default=True"
        ),
    }
    try:
        station = SpaceStation(**info)
        print("=================================")
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size}")
        print(f"Power: {station.power_level}")
        print(f"Oxygen: {station.oxygen_level}")
        print(f"Maintenance: {station.last_maintenance}")
        print(f"Status{station.is_operational}")
        print(f"Note: {station.notes}")
        print()
        print("=================================")
    except ValidationError as e:
        print("Expected validation error:")
        print(e)

    info2: dict = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 30,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.now(),
        "notes": (
            "add last_maintenance.\n"
            "don't take is_operational because default=True"
        ),
    }
    try:
        station = SpaceStation(**info2)
        print("=================================")
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size}")
        print(f"Power: {station.power_level}")
        print(f"Oxygen: {station.oxygen_level}")
        print(f"Maintenance: {station.last_maintenance}")
        print(f"Status{station.is_operational}")
        print(f"Note: {station.notes}")
        print()
        print("=================================")
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
