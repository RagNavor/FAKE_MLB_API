from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import Session, engine, Base
from models.player import Player
from models.team import  Team
from models.league import League
from schemas.schemas_player import CreatePlayer, UpdatePlayer 
from schemas.schemas_league import CreateLeague, UpdateLeague 
from schemas.schemas_team import CreateTeam, UpdateTeam


app = FastAPI()
app.title = "FAKE_MLB_API"
Base.metadata.create_all(bind=engine)

@app.get('/players/get_all_players', tags=['PLAYERS'])
def get_all_players():
    db = Session()
    result = db.query(Player).all()
    '''if not result:
        return JSONResponse(status_code=404, content='Players not found')'''
    return JSONResponse(status_code=200, content=jsonable_encoder(result))