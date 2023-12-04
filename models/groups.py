from config.database import Base
from sqlalchemy import Column, Integer,Boolean,VARCHAR, BIGINT, DateTime,ForeignKey, true
from sqlalchemy.orm import relationship
from datetime import datetime

class Group(Base):
    __tablename__="groups"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(30))
    group_user = relationship("User",back_populates="user_group")
    
    permissions_group = relationship("Permission",secondary="groups_permissions",back_populates="permission_group")
    
    