from datetime import datetime
from schemas.schemas_player import CreatePlayer, UpdatePlayer
from models.player import Player
from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.player import PlayerService
from config.database import Session
from middlewares.permissions import VerifyPermissionCreateUpdate


router = APIRouter()

@router.get('/players', tags=['CRUD_PLAYERS'],dependencies=[Depends(VerifyPermissionCreateUpdate())])
def get_all_players():
    db = Session()
    result = db.query(Player).all()
    if not result:
        return JSONResponse(status_code=404, content='Players not found')
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get('/players/get_players_by_team/{id}', tags=['PLAYER_GET_OPTIONS'])
def get_players_by_team(id):
    db = Session()
    result = PlayerService(db).get_players_by_team(id)
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_starting_pitchers/',tags=['PLAYER_GET_OPTIONS'])
def get_players_starting_pitchers():
    db = Session
    result = PlayerService(db).get_players_starting_pitchers()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_relief_pitchers/',tags=['PLAYER_GET_OPTIONS'])
def get_players_relief_pitchers():
    db = Session
    result = PlayerService(db).get_players_relief_pitchers()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_catchers/', tags=['PLAYER_GET_OPTIONS'])
def get_players_catchers():
    db = Session
    result = PlayerService(db).get_players_catchers()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_shortstops/', tags=['PLAYER_GET_OPTIONS'])
def get_players_shortstops():
    db = Session
    result = PlayerService(db).get_players_shortstops()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_first_base/', tags=['PLAYER_GET_OPTIONS'])
def get_players_first_basemen():
    db = Session
    result = PlayerService(db).get_players_first_base()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_second_base/', tags=['PLAYER_GET_OPTIONS'])
def get_players_second_basemen():
    db = Session
    result = PlayerService(db).get_players_second_base()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_third_base/', tags=['PLAYER_GET_OPTIONS'])
def get_players_third_basemen():
    db = Session
    result = PlayerService(db).get_players_third_base()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_left_fielders/', tags=['PLAYER_GET_OPTIONS'])
def get_players_left_fielders():
    db = Session
    result = PlayerService(db).get_players_left_fielders()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_right_fielders/', tags=['PLAYER_GET_OPTIONS'])
def get_players_right_fielders():
    db = Session
    result = PlayerService(db).get_players_right_fielders()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_center_fielders/', tags=['PLAYER_GET_OPTIONS'])
def get_players_center_fielders():
    db = Session
    result = PlayerService(db).get_players_center_fielders()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_designated_hitter/', tags=['PLAYER_GET_OPTIONS'])
def get_players_designated_hitter():
    db = Session
    result = PlayerService(db).get_players_designated_hitter()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_bat_right/', tags=['PLAYER_GET_OPTIONS'])
def get_players_bat_right():
    db = Session
    result = PlayerService(db).get_players_bat_right()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})

@router.get('/players/get_players_bat_left/', tags=['PLAYER_GET_OPTIONS'])
def get_players_bat_left():
    db = Session
    result = PlayerService(db).get_players_bat_left()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})


@router.get('/players/get_players_throw_right/', tags=['PLAYER_GET_OPTIONS'])
def get_players_throw_right():
    db = Session
    result = PlayerService(db).get_players_throw_right()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})
    


@router.get('/players/get_players_throw_left/', tags=['PLAYER_GET_OPTIONS'])
def get_players_throw_left():
    db = Session
    result = PlayerService(db).get_players_throw_left()
    if result:
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    return JSONResponse(status_code=404, content={'message':'Payers not found'})
    

@router.post('/players/create_player', tags=['CRUD_PLAYERS'])
def create_player(player: CreatePlayer):
    db = Session()
    new_player = Player(**player.model_dump())
    db.add(new_player)
    db.commit()
    db.close()
    return JSONResponse(status_code=201, content='Player Created')
    
@router.put('/players/update_player/{id}',tags=['CRUD_PLAYERS'])
def update_player(id:int, player:UpdatePlayer):
    db = Session()
    result= db.query(Player).filter(Player.id ==id).first()
    if not result:
        return JSONResponse(status_code=404, content='Player not found')
    result = player
    result.updated_at = datetime.now()
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content=f'Player {result} has ben updeted')
    
@router.delete('/players/delete_player/{id}',tags=['CRUD_PLAYERS'])
def delete_player(id:int):
    db = Session()
    result = db.query(Player).filter(Player.id == id).first()
    if not result:
       return JSONResponse(status_code=404, content='Player not found')
    db.delete(result)
    db.commit()
    db.close()
    return JSONResponse(status_code=202, content='Player Deleted')
