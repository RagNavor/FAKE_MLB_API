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
    status: bool
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
    status: bool
    team_id: int
