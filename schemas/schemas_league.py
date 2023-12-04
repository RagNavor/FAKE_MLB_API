from pydantic import BaseModel, Field
from datetime import datetime


class CreateLeague(BaseModel):
    name:str = Field(max_length=45)
    country: str = Field(max_length=45)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "name": "National league",
                "country": "United States",
                }
            ]
            
        }
    }
    
class UpdateLeague(BaseModel):
    name:str = Field(max_length=45)
    country: str = Field(max_length=45)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "name": "National league",
                "country": "United States",
                }
            ]
            
        }
    }

    
    