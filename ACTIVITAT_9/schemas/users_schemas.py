from pydantic import BaseModel, Field

class Direction(BaseModel):
    city: str
    country: str
    addres: str

class User(BaseModel):
    name: str
    last_name: str
    age: int = Field(gt=0, description="The age must be positve")
    email: str = Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: int
    direction: Direction

class Column(BaseModel):
    key: str
    value: str