from pydantic import BaseModel


class CreateLeague(BaseModel):
    name:str
    country: str
        
class UpdateLeague(BaseModel):
    name:str
    country: str

    
    