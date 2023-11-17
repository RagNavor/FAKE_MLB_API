from hmac import new
from tkinter import SE
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.player import Player, Leagues,Teams
from schemas.schemas import Player as SPlayer 
from schemas.schemas import League as SLeague 
from schemas.schemas import Team as STeam

from config.database import Session, engine, Base

app = FastAPI()
app.title = "FAKE_MLB_API"

Base.metadata.create_all(bind=engine)


#PLAYERS
@app.get('/players/get_players', tags=['PLAYERS'])
def get_players():
    db = Session()
    db.query()
    return 

@app.get('/players/get_players/{id}', tags=['PLAYERS'])
def get_player(id:int):
    db = Session()
    db.query()

@app.post('/players/create',tags=['PLAYERS'])
def create_player(player: SPlayer):
    db = Session()
    new_player = Player(**player.model_dump())
    db.add(new_player)
    db.commit()
    

@app.put('/players/update/{id}',tags=['PLAYERS'])
def update_player(id:int,player: SPlayer):
    db = Session()
    pass

@app.patch('/players/partial_update/{id}',tags=['PLAYERS'])
def partial_update_player(id:int,player: SPlayer):
    db = Session()
    pass

@app.delete('/players/delete/{id}',tags=['PLAYERS'])
def delete_player(id:int,player: SPlayer):
    db = Session()
    pass
#PLAYERS




#TEAMS
@app.get('/teams/{id}', tags=['TEAMS'])   
def get_team(id: int):
    return id
@app.post('/teams/create/',tags=['TEAMS'])
def create_team(team:STeam):
    db = Session()
    pass
@app.put('/teams/update/{id}/',tags=['TEAMS'])
def update_team(id:int,team:STeam):
    db = Session()
    pass
@app.patch('/teams/partial_update/{id}/{part}/', tags=['TEAMS'])
def patch_team(id:int,team:STeam):
    '''Queda pendiente determinar como vamos a capturar el valor especifico que se desea actualizar'''
    db = Session()
    pass
@app.delete('/teams/delete/{id}',tags=['TEAMS'])
def delete_team(id:int):
    db=Session
    pass
#TEAMS

#LEAGUES
@app.get('/leagues', tags=['LEAGUES'])
def get_league():
    return 'hello Word'

@app.post('/leagues/create', tags=['LEAGUES'])
def create_league(league:SLeague):
    db = Session()
    new_league = Leagues(**league.model_dump())
    db.add(new_league)
    db.commit()
    return JSONResponse(status_code=201,content='league created succesfull')
@app.put('/leagues/update/{id}', tags=['LEAGUES'])
def update_league(id:int, league:SLeague):
    db = Session()
    
    pass
@app.patch('/leagues/partial_update/{id}', tags=['LEAGUES'])
def partial_update_league(id:int, league:SLeague):
    db = Session()
    pass
@app.delete('/leagues/delete/{id}', tags=['LEAGUES'])
def delete_league(id:int):
    db = Session()
    
#LEAGUES