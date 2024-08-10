from typing import Optional

from pydantic import BaseModel

from topdrawersoccer.models.conference import Conference


class School(BaseModel):
    id: int
    name: str
    url: str
    division: Optional[str]
    conference_id: Optional[int]

    def __str__(self):
        return f"Name: {self.name} - Division: {self.division} - URL: '{self.url}' - Conference: {self.conference_id}"
