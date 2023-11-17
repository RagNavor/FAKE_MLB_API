from config.database import Base
from sqlalchemy import Column, Integer,Boolean,VARCHAR, BIGINT, DateTime,ForeignKey, true
from sqlalchemy.orm import relationship
from datetime import datetime


class Player(Base):
    __tablename__ = "players"
    id = Column(BIGINT, primary_key = True)
    name= Column(VARCHAR(60))
    pos = Column(VARCHAR(10))
    bat = Column(VARCHAR(2))
    thw = Column(VARCHAR(2))
    age = Column(Integer())
    ht = Column(VARCHAR(7))
    wt = Column(Integer)
    birth_place = Column(VARCHAR(45))
    status = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now())
    team_id = Column(Integer,ForeignKey("teams.id"))
    players_team = relationship("Teams",back_populates="team_players")