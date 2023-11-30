from typing import Any, Coroutine, Optional
from fastapi import Depends, FastAPI, HTTPException,Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.requests import Request
from config.database import Session, engine, Base
from models.player import Player
from models.team import  Team
from models.league import League
from schemas.schemas_player import CreatePlayer, UpdatePlayer 
from schemas.schemas_league import CreateLeague, UpdateLeague 
from schemas.schemas_team import CreateTeam, UpdateTeam
from schemas.schemas_user import CreateUser, UpdateUser, LoginUser
from datetime import datetime
from middlewares.jwt_manager import create_token,validate_token
from fastapi.security import  HTTPBearer
from routers import user, player



app = FastAPI()

app.title = "FAKE_MLB_API"

app.include_router(user.router)
app.include_router(player.router)
Base.metadata.create_all(bind=engine)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != '1@1':
            raise HTTPException(status_code=403, detail=' credencial invalida')
        

#USERS


@app.post('/login', tags=['AUTH'])
def login(user: LoginUser):
    if user.email == '1@1' and user.password =='123':
        token:str =create_token(user.model_dump())
    return JSONResponse(status_code=200, content=token)

#USERS


#PLAYERS

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