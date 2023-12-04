
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from os import getenv

load_dotenv()
user = getenv('DB_User_Admin')
password = getenv('DB_User_Admin_Password')

#mysql_url = f'mariadb+mariadbconnector://{user}:{password}@localhost/mlb_db'
postgre_url = f'postgresql://{user}:{password}@postgresserver/db'
Base = declarative_base()
engine = create_engine(postgre_url,echo=True)
Session = sessionmaker(bind =engine)






