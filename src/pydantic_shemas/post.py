from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(le=1)
    title: str
    name: str = Field(alias="_name")
