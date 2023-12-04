
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from os import getenv

load_dotenv()
user = getenv('DB_User_Admin')
password = getenv('DB_User_Admin_Password')
Base = declarative_base()
mysql_url = f'mariadb+mariadbconnector://{user}:{password}@localhost/mlb_db'
engine = create_engine(mysql_url,echo=True)
Session = sessionmaker(bind =engine)






