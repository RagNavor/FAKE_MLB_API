import datetime
from pydantic import BaseModel

class CreatePlayer(BaseModel):
    name: str
    pos: str
    bat: str
    thw: str
    age: int
    ht: str
    wt: int
    birth_place: str
    team_id: int
    
class UpdatePlayer(BaseModel):
    name: str
    pos: str
    bat: str
    thw: str
    age: int
    ht: str
    wt: int
    birth_place: str
    team_id: int
    updated_at: None
