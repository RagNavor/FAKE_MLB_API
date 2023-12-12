from datetime import datetime
from schemas.schemas_league import CreateLeague, UpdateLeague
from models.league import League
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.player import PlayerService
from config.database import Session
from middlewares.permissions import VerifyPermissionCreateUpdate


router = APIRouter()

@router.get('/leagues', tags=['LEAGUES'])
def get_all_leagues():
    db = Session()
    result = db.query(League).all()
    if not result:
        return JSONResponse(status_code=404, content='Leagues not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get('/leagues/{id}', tags=['LEAGUES'])
def get_all_leagues(id:int):
    db = Session()
    result = db.query(League).filter(League.id == id).first
    if not result:
        return JSONResponse(status_code=404, content='Leagues not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.post('/leagues', tags=['LEAGUES'])
def create_leagues(league: CreateLeague):
    db = Session()
    new_league = League(**league.model_dump())
    db.add(new_league)
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content=f'league: {new_league}  created successfully')

@router.put('/leagues/{id}', tags=['LEAGUES'])
def update_leagues(id:int, league: UpdateLeague):
    db = Session()
    result = db.query(League).filter(League.id == id).first()
    result.name = league.name
    result.country = league.country
    result.updated_at = datetime.now()
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content=f'league: {result}  updated successfully')

@router.delete('/leagues/{id}', tags=['LEAGUES'])
def delete_leagues(id:int):
    db = Session()
    result = db.query(League).filter(League.id == id).first()
    if not result:
       return JSONResponse(status_code=404, content='League not found')
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content='League Deleted')