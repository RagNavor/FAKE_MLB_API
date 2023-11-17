from pydantic import BaseModel
from datetime import datetime


class CreateLeague(BaseModel):
    name:str
    country: str

class UpdateLeague(BaseModel):
    name:str
    country: str

    
    