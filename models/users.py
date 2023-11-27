from config.database import Base
from sqlalchemy import BIGINT, Column, Integer,VARCHAR,DateTime,ForeignKey,Boolean,BINARY, LargeBinary
from datetime import datetime

class User(Base):
    __tablename__='users'
    id=Column(BIGINT, primary_key=True)
    first_name = Column(VARCHAR(45))
    last_name =Column(VARCHAR(45))
    full_name =Column(VARCHAR(90), default=f'{first_name} {last_name}')
    email =Column(VARCHAR(45))
    password =Column(LargeBinary())
    phone_number = Column(BIGINT)
    created_at =Column(DateTime, default=datetime.now())
    updated_at =Column(DateTime, default=datetime.now())