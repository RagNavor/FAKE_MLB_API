from typing import Any, Coroutine, Optional
from fastapi import Depends, FastAPI, HTTPException,Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.requests import Request
from config.database import Session, engine, Base
from models.player import Player
from models.team import  Team
from models.league import League
from models.groups import Group
from models.users import User
from models.permissions import Permission
from models.group_permissions import Group_Permission
from schemas.schemas_player import CreatePlayer, UpdatePlayer 
from schemas.schemas_league import CreateLeague, UpdateLeague 
from schemas.schemas_team import CreateTeam, UpdateTeam
from schemas.schemas_user import CreateUser, UpdateUser, LoginUser
from datetime import datetime
from middlewares.jwt_manager import create_token,validate_token
from fastapi.security import  HTTPBearer
from routers import user, player, team, league
from middlewares.permissions import VerifyPermissionCreateUpdate, OnlyAdmin
from middlewares.encrypt_password import verify_password


app = FastAPI()

app.title = "FAKE_MLB_API"

app.include_router(user.router)
app.include_router(player.router)
app.include_router(team.router)
app.include_router(league.router)

Base.metadata.create_all(bind=engine)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != '1@1':
            raise HTTPException(status_code=403, detail=' credencial invalida')
        

#USERS

@app.middleware
@app.post('/login', tags=['AUTH'])
def login(login_user:LoginUser):
    db = Session()
    result = db.query(User).filter(User.email == login_user.email).first()
    if result:
        auth = verify_password(login_user.password,result.password)
        print(result.password)
        print(login_user.password)
        print(auth)
        if auth:
            token:str =create_token(jsonable_encoder(result))
            return JSONResponse(status_code=200, content=token)
        return JSONResponse(status_code=403, content={'message': 'Invalid password'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})

#USERS


#PLAYERS

#PLAYERS

#TEAMS 
