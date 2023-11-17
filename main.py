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
from datetime import datetime


app = FastAPI()
app.title = "FAKE_MLB_API"
Base.metadata.create_all(bind=engine)

#PLAYERS
@app.get('/players/get_all_players', tags=['PLAYERS'])
def get_all_players():
    db = Session()
    result = db.query(Player).all()
    if not result:
        return JSONResponse(status_code=404, content='Players not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/players/create_player', tags=['PLAYERS'])
def create_player(player: CreatePlayer):
    db = Session()
    new_player = Player(**player.model_dump())
    db.add(new_player)
    db.commit()
    db.close()
    return JSONResponse(status_code=201, content='Player Created')
    
@app.put('/players/update_player/{id}',tags=['PLAYERS'])
def update_player(id:int, player:UpdatePlayer):
    db = Session()
    result= db.query(Player).filter(Player.id ==id).first()
    if not result:
        return JSONResponse(status_code=404, content='Player not found')
    result.age = player.age
    result.bat = player.bat
    result.birth_place = player.birth_place
    result.ht = player.ht
    result.name = player.name
    result.thw = player.thw
    result.pos = player.pos
    result.team_id = player.team_id
    result.wt = player.wt
    result.updated_at = datetime.now()
    db.commit()
    db.close()
    
    
    return JSONResponse(status_code=202, content=f'Player {result} has ben updeted')
    
@app.delete('/players/delete_player/{id}',tags=['PLAYERS'])
def delete_player(id:int):
    db = Session()
    result = db.query(Player).filter(Player.id == id).first()
    if not result:
       return JSONResponse(status_code=404, content='Player not found')
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content='Player Deleted')
#PLAYERS

#TEAMS 

@app.get('/teams/get_all_teams', tags=['TEAMS'])
def get_all_teams():
    db = Session()
    result = db.query(Team).all()
    if not result:
        return JSONResponse(status_code=404, content='Teams not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.post('/teams/create_team', tags=['TEAMS'])
def create_team(team: CreateTeam):
    db = Session()
    new_team = Team(**team.model_dump())
    db.add(new_team)
    db.commit()
    db.close()
    return JSONResponse(status_code=201, content='Team Created')

@app.put('/teams/update_team/{id}', tags=['TEAMS'])
def update_team(id:int, team: UpdateTeam):
    db = Session()
    result = db.query(Team).filter(Team.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content='Team not found')
    result.updated_at = datetime.now()
    result.name = team.name
    result.city = team.city
    result.league_id = team.league_id
    db.commit()
    db.close()
    return JSONResponse(content=f'Team: {result} updated successfully', status_code=202)
    
    
@app.delete('/teams/delete_team/{id}', tags=['TEAMS'])
def delete_team(id:int):
    db = Session()
    result = db.query(Team).filter(Team.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content='Team not found')
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(content='team deleted', status_code=202)

#TEAMS

#LEAGUES

@app.get('/leagues/get_all_leagues', tags=['LEAGUES'])
def get_all_leagues():
    db = Session()
    result = db.query(League).all()
    if not result:
        return JSONResponse(status_code=404, content='Leagues not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/leagues/create_leagues', tags=['LEAGUES'])
def create_leagues(league: CreateLeague):
    db = Session()
    new_league = League(**league.model_dump())
    db.add(new_league)
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content=f'league: {new_league}  created successfully')

@app.put('/leagues/update_leagues/{id}', tags=['LEAGUES'])
def update_leagues(id:int, league: UpdateLeague):
    db = Session()
    result = db.query(League).filter(League.id == id).first()
    result.name = league.name
    result.country = league.country
    result.updated_at = datetime.now()
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content=f'league: {result}  updated successfully')

@app.delete('/leagues/delete_leagues/{id}', tags=['LEAGUES'])
def delete_leagues(id:int):
    db = Session()
    result = db.query(League).filter(League.id == id).first()
    if not result:
       return JSONResponse(status_code=404, content='League not found')
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content='League Deleted')

#LEAGUES