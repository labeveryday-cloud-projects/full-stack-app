# This is a quick backend server to serve the data for the frontend
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Create a database
class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="John", age=20),
    Person(id=2, name="Mary", age=21),
    Person(id=3, name="Bob", age=22),
    Person(id=4, name="Jane", age=23),
    Person(id=5, name="Mike", age=24),
]

@app.get("/api")
def read_root():
    return DB
