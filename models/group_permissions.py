from config.database import Base
from sqlalchemy import Column, Integer,Boolean,VARCHAR, BIGINT, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Group_Permission(Base):
    __tablename__ = "groups_permissions"
    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey("groups.id"),primary_key=True)
    permission_id = Column(ForeignKey("permissions.id"),primary_key=True)
