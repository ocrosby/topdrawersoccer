from pydantic import BaseModel

from topdrawersoccer.models.conference import Conference


class School(BaseModel):
    id: int
    name: str
    url: str
    division: str
    conference_id: int

    def __str__(self):
        return f"Name: {self.name} - Division: {self.division} - URL: '{self.url}' - Conference: {self.conference_id}"
