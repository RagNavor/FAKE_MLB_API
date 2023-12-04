from config.database import Base
from sqlalchemy import Column, Integer,Boolean,VARCHAR, BIGINT, DateTime,ForeignKey, true
from sqlalchemy.orm import relationship
from datetime import datetime


class Permission(Base):
    __tablename__= "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(30))
    permission_group = relationship("Group",secondary="groups_permissions",back_populates="permissions_group")