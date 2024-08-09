from pydantic import BaseModel

from typing import Optional


class Transfer(BaseModel):
    id: int
    url: Optional[str]
    name: str
    position: Optional[str]
    outgoing_college_name: Optional[str]
    outgoing_college_url: Optional[str]
    incoming_college_name: Optional[str]
    incoming_college_url: Optional[str]

    def __str__(self):
        part1 = f"Name: {self.name} - Position: {self.position}"
        part2 = f"Outgoing College: {self.outgoing_college_name} - URL: {self.outgoing_college_url}"
        part3 = f"Incoming College: {self.incoming_college_name} - URL: {self.incoming_college_url}"

        return f"{part1} - {part2} - {part3}"
