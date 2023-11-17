from config.database import Base
from sqlalchemy import Column, Integer,VARCHAR, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class League(Base):
    __tablename__ = "leagues"
    id = Column(Integer, primary_key= True)
    name = Column(VARCHAR(45))
    country = Column(VARCHAR(45))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime,default=datetime.now())
    updated_at = Column(DateTime,default=datetime.now())
    league_teams = relationship("Team", back_populates="teams_league")