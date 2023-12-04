import datetime
from pydantic import BaseModel, Field

class CreatePlayer(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    pos: str = Field(min_length=1, max_length=2)
    bat: str = Field(min_length=1, max_length=1)
    thw: str = Field(min_length=1, max_length=1)
    age: int = Field(ge=1, le=50)
    ht: str = Field(min_length=5, max_length=6)
    wt: int = Field(ge=1, le=300)
    birth_place: str = Field(max_length=45)
    team_id: int 
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "name": "Peter Gregory",
                "pos": "CF",
                "bat": "R",
                "thw": "R",
                "age": 25,
                "ht": "6\' 3\"",
                "wt": 210,
                "birth_place": "Miami, FL",
                "team_id": 5 
                }
            ]
            
        }
    }
class UpdatePlayer(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    pos: str = Field(min_length=1, max_length=2)
    bat: str = Field(min_length=1, max_length=1)
    thw: str = Field(min_length=1, max_length=1)
    age: int = Field(ge=1, le=50)
    ht: str = Field(min_length=5, max_length=5)
    wt: int = Field(ge=1, le=300)
    birth_place: str = Field(max_length=45)
    team_id: int = Field()
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "name": "Peter Gregory",
                "pos": "CF",
                "bat": "R",
                "thw": "R",
                "age": 25,
                "ht": "6\' 3\"",
                "wt": 210,
                "birth_place": "Miami, FL",
                "team_id": 5 
                }
            ]
            
        }
    }
    
