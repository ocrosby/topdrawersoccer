"""
This module contains the Team model.
"""

from pydantic import BaseModel


class Team(BaseModel):
    """
    Team model
    """
    id: int
    name: str
    url: str
    gender: str
    division: str
    conference_id: int

    def __str__(self):
        """
        This function returns a string representation of the team.

        :return: The string representation of the team
        """
        return f"Name: {self.name} - Gender: {self.gender} - Division: {self.division} - URL: '{self.url}' - Conference ID: {self.conference_id}"
