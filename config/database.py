from .credentials import user, password
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

Base = declarative_base()
mysql_url = f'mariadb+mariadbconnector://{user}:{password}@localhost/mlb_db'
engine = create_engine(mysql_url,echo=True)
Session = sessionmaker(bind =engine)






