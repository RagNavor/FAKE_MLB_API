from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from .jwt_manager import validate_token

class VerifyPermissionCreateUpdate(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        print(request.base_url)
        print(auth.credentials)
        data = validate_token(auth.credentials)
        print(data)
        if data['group_id'] > 5:
            raise HTTPException(status_code=403,detail='User cannot permission')
        
        
class OnlyAdmin(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        print(type(request.url))
        print(auth.credentials)
        data = validate_token(auth.credentials)
        print(data)
        if data['group_id'] > 4:
            raise HTTPException(status_code=403,detail='User cannot permission')