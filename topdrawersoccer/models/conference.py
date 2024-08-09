from pydantic import BaseModel


class Conference(BaseModel):
    id: int
    name: str
    url: str
    division: str
    gender: str

    def __str__(self):
        return f"Name: {self.name} - Gender: {self.gender} - Division: {self.division} - URL: '{self.url}'"
    