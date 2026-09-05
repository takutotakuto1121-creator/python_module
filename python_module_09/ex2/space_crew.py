#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime

class CrewRanks(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check(self):
        if not self.mission_id.startswith("M"):
            raise Exception("Mission ID must start with M")
        if not any(m.rank in (CrewRanks.COMMANDER, CrewRanks.CAPTAIN) for m in self.crew):
            raise Exception("Mission must have at least one Commander or Captain")
        if self.duration_days > 365 and not self.check_experienced(self.crew):
            raise Exception("Long missions (> 365 days) need 50% experienced crew (5+ years)")
        if not self.check_active(self.crew):
            raise Exception("All crew members must be active")
        return self

    @staticmethod
    def check_experienced(crew: list[CrewMember]) -> bool:
        experienced_crew = 0
        total_crew = 0
        for crew in crew:
            if crew.years_experience >= 5:
                experienced_crew += 1
            total_crew += 1
        if experienced_crew / total_crew >= 0.5:
            return True
        else:
            return False

    @staticmethod
    def check_active(crew: list[CrewMember]) -> bool:
        for crew in crew:
            if not crew.is_active:
                return False
        return True


def count_crew_size(crew: list[CrewMember]) -> int:
    i = 0
    for _ in crew:
        i += 1
    return i

def main() -> None:
    data = {
    "mission_id": "M2024_TITAN",
    "mission_name": "Solar Observatory Research Mission",
    "destination": "Solar Observatory",
    "launch_date": "2024-03-30T00:00:00",
    "duration_days": 451,
    "crew": [
      {
        "member_id": "CM001",
        "name": "Sarah Williams",
        "rank": "captain",
        "age": 43,
        "specialization": "Mission Command",
        "years_experience": 19,
        "is_active": True
      },
      {
        "member_id": "CM002",
        "name": "James Hernandez",
        "rank": "captain",
        "age": 43,
        "specialization": "Pilot",
        "years_experience": 30,
        "is_active": True
      },
      {
        "member_id": "CM003",
        "name": "Anna Jones",
        "rank": "cadet",
        "age": 35,
        "specialization": "Communications",
        "years_experience": 15,
        "is_active": True
      },
      {
        "member_id": "CM004",
        "name": "David Smith",
        "rank": "commander",
        "age": 27,
        "specialization": "Security",
        "years_experience": 15,
        "is_active": True
      },
      {
        "member_id": "CM005",
        "name": "Maria Jones",
        "rank": "cadet",
        "age": 55,
        "specialization": "Research",
        "years_experience": 30,
        "is_active": True
      }
    ],
    "mission_status": "planned",
    "budget_millions": 2208.1
    }
    try:
        space = SpaceMission(**data)
        print("Space Mission Crew Validation")
        print("=================================")
        print("Valid Mission created")
        print(f"Mission: {space.mission_name}")
        print(f"ID: {space.mission_id}")
        print(f"Destination: {space.destination}")
        print(f"Duration: {space.duration_days} days")
        print(f"Budget: {space.budget_millions}M")
        crew_size = count_crew_size(space.crew)
        print(f"Crew size: {crew_size}")
        print(f"Crew members:")
        for crew in space.crew:
            print(f"- {crew.name} ({crew.rank}) - {crew.specialization}")
        print()
        print("==================================")
    except Exception as e:
        print("Expected validation error:")
        print(f"{e}")

    data1 = {
    "mission_id": "M2024_TITAN",
    "mission_name": "Solar Observatory Research Mission",
    "destination": "Solar Observatory",
    "launch_date": "2024-03-30T00:00:00",
    "duration_days": 451,
    "crew": [
      {
        "member_id": "CM001",
        "name": "Sarah Williams",
        "rank": "cadet",
        "age": 43,
        "specialization": "Mission Command",
        "years_experience": 19,
        "is_active": True
      },
      {
        "member_id": "CM002",
        "name": "James Hernandez",
        "rank": "cadet",
        "age": 43,
        "specialization": "Pilot",
        "years_experience": 30,
        "is_active": True
      },
      {
        "member_id": "CM003",
        "name": "Anna Jones",
        "rank": "cadet",
        "age": 35,
        "specialization": "Communications",
        "years_experience": 15,
        "is_active": True
      },
      {
        "member_id": "CM004",
        "name": "David Smith",
        "rank": "cadet",
        "age": 27,
        "specialization": "Security",
        "years_experience": 15,
        "is_active": True
      },
      {
        "member_id": "CM005",
        "name": "Maria Jones",
        "rank": "cadet",
        "age": 55,
        "specialization": "Research",
        "years_experience": 30,
        "is_active": True
      }
    ],
    "mission_status": "planned",
    "budget_millions": 2208.1
    }
    try:
        space = SpaceMission(**data1)
        print("Space Mission Crew Validation")
        print("=================================")
        print("Valid Mission created")
        print(f"Mission: {space.mission_name}")
        print(f"ID: {space.mission_id}")
        print(f"Destination: {space.destination}")
        print(f"Duration: {space.duration_days} days")
        print(f"Budget: {space.budget_millions}M")
        crew_size = count_crew_size(space.crew)
        print(f"Crew size: {crew_size}")
        print(f"Crew members:")
        for crew in space.crew:
            print(f"- {crew.name} ({crew.rank}) - {crew.specialization}")
        print()
        print("==================================")
    except Exception as e:
        print("Expected validation error:")
        print(f"{e}")



if __name__ == "__main__":
    main()
