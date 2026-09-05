#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def more_validate(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("If contact_type is phisical, is_verify should be True")
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("If contact_type is telephatic, witness_count should be greater than or equal 3")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("If signal_strength is more than 7.0, should receive message")
        return self


def main():
    dataset = [
    {
        "contact_id": "AC_2026",
        "timestamp": "2024-01-15T14:30:00",
        "location": "Area 51",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "message",
        "is_verified": False
    },
    {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-01-16T09:15:00",
        "location": "Roswell",
        "contact_type": "telepathic",
        "signal_strength": 6.2,
        "duration_minutes": 30,
        "witness_count": 1,
        "message_received": 'messaaaaaaaaage',
        "is_verified": False
    }
    ]
    for data in dataset:
        try:
            alien = AlienContact(**data)
            print("Alien Contact Log Validataion")
            print("======================================")
            print("Valid contact report:")
            print(f"ID: {alien.contact_id}")
            print(f"Type: {alien.contact_type}")
            print(f"Location: {alien.location}")
            print(f"Signal: {alien.signal_strength}")
            print(f"Duration: {alien.duration_minutes} minutes")
            print(f"Witness: {alien.witness_count}")
            print(f"Message: '{alien.message_received}'")
            print()
            print("======================================")
        except ValueError as e:
            print("Expected validation error:")
            print(f"{e}")


if __name__ == "__main__":
    main()
