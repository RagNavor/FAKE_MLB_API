
from fastapi.responses import JSONResponse
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from os import getenv
from dotenv import load_dotenv


load_dotenv()
def expire_date(days:int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def create_token(data:dict):
    print()
    token = encode(payload={**data, "exp": expire_date(3)}, key=getenv('Key'), algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    try:
        data:dict= decode(token, key=getenv('Key'), algorithms=['HS256'])
        return data
    except exceptions.DecodeError:
        return JSONResponse(status_code=403, content={'message':'Invalid Token'})
    except exceptions.ExpiredSignatureError:
        return JSONResponse(status_code=403,content={'message':'Expired Token'})
    
