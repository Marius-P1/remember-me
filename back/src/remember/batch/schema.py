from typing import List
from pydantic import BaseModel, Field
import json
from typing import List


class Person(BaseModel):
    name: str = Field(description="The name of the person")
    relationship: str = Field(description="The relationship of the person to the user")
    age: int = Field(description="The age of the person")
    occupation: str = Field(description="The occupation of the person")
    hobbies: List[str] = Field(default_factory=list, description="The hobbies of the person")
    description: str = Field(description="A description of the person")

    def __str__(self):
        return json.dumps(self.dict(), indent=2)


class Memory(BaseModel):
    person: Person = Field(decription="The writer of the memory")
    place: List[str] = Field(default_factory=list, description="A list of places involved in the memory")
    emotion: List[str] = Field(default_factory=list)
    description: str = Field(description="A description of the memory")

    def __str__(self):
        return json.dumps(self.dict(), indent=2)


class EventMemories(BaseModel):
    """Memories collection about a single event with different perspectives."""
    event: str = Field(description="The specific event being remembered")
    memories: List[Memory] = Field(default_factory=list)

    def __str__(self):
        return json.dumps(self.dict(), indent=2)
    
class DayMemory(BaseModel):
    title: str = Field(description="The title of the memory (between 3 and 10 words)")
    summary: str = Field(description="A summary of the memory")