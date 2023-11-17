from fastapi import FastAPI
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

