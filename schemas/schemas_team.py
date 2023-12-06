from pydantic import BaseModel, Field

class CreateTeam(BaseModel):
    name: str = Field(max_length=45)
    logo:str = Field(max_length=200)
    city:str  = Field(max_length=45)
    league_id:int  = Field(ge=1)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "name": "Kansas City Royals",
                "logo": "https://a.espncdn.com/i/headshots/mlb/players/full/38106.png",
                "city": "Kansas",
                "league_id": 1,
                }
            ]
            
        }
    }
    
class UpdateTeam(BaseModel):
    name: str  = Field(max_length=45)
    city:str = Field(max_length=200)
    logo:str = Field(max_length=200)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "name": "Kansas City Royals",
                "logo": "https://a.espncdn.com/i/headshots/mlb/players/full/38106.png",
                "city": "Kansas",
                }
            ]
            
        }
    }