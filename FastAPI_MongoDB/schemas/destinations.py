from pydantic import BaseModel, Field


class DestinationCreate(BaseModel):
    name: str
    location: str
    description: str
    price: float
    duration: int
    image: str
    activities: list[str] = Field(default_factory=list)


class DestinationResponse(BaseModel):
    id: str
    name: str
    location: str
    description: str
    price: float
    duration: int
    image: str
    activities: list[str]