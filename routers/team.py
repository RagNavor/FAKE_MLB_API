from datetime import datetime
from schemas.schemas_team import CreateTeam, UpdateTeam
from models.team import Team
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.player import PlayerService
from config.database import Session
from middlewares.permissions import VerifyPermissionCreateUpdate, OnlyAdmin


router = APIRouter()


@router.get('/teams', tags=['TEAMS'])
def get_all_teams():
    db = Session()
    result = db.query(Team).all()
    if not result:
        return JSONResponse(status_code=404, content='Teams not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get('/teams/{id}', tags=['TEAMS'])
def get_single_teams(id:int):
    db = Session()
    result = db.query(Team).filter(Team.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content='Teams not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post('/teams', tags=['TEAMS'],dependencies=[Depends(VerifyPermissionCreateUpdate())])
def create_team(team: CreateTeam):
    db = Session()
    new_team = Team(**team.model_dump())
    team_name = new_team.name
    db.add(new_team)
    db.commit()
    db.close()
    return JSONResponse(status_code=201, content=f'Team {team_name} Created')

@router.put('/teams/{id}', tags=['TEAMS'])
def update_team(id:int, team: UpdateTeam):
    db = Session()
    result = db.query(Team).filter(Team.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content='Team not found')
    result.updated_at = datetime.now()
    result.name = team.name
    result.city = team.city
    result.logo = team.logo
    team_name = result.name
    db.commit()
    db.close()
    return JSONResponse(content=f'Team: {team_name} updated successfully', status_code=202)
    
    
@router.delete('/teams/{id}', tags=['TEAMS'],dependencies=[Depends(OnlyAdmin())])
def delete_team(id:int):
    db = Session()
    result = db.query(Team).filter(Team.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content='Team not found')
    team_name = result.name
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(content=f'team {team_name} deleted', status_code=202)
