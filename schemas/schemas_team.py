from pydantic import BaseModel

class CreateTeam(BaseModel):
    name: str
    logo:str
    city:str
    league_id:int
    
class UpdateTeam(BaseModel):
    name: str
    city:str
    league_id:int