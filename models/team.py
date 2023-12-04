from config.database import Base
from sqlalchemy import Column, Integer,VARCHAR,DateTime,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .league import League

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key= True)
    name = Column(VARCHAR(45))
    logo = Column(VARCHAR(200))
    city = Column(VARCHAR(45))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default= datetime.now())
    updated_at = Column(DateTime, default= datetime.now())
    league_id = Column(Integer,ForeignKey("leagues.id"))
    teams_league = relationship("League", back_populates="league_teams")
    team_players = relationship("Player", back_populates="players_team")
    