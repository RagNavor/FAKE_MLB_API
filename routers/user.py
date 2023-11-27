from fastapi import APIRouter
from services.user import User_Service
from schemas.schemas_user import CreateUser, UpdateUser, UpdateFirstName, UpdateLastName,UpdateEmail,UpdatePassword,UpdatePhoneNumber
from config.database import Session, Base, engine
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()

@router.get( path="/get_all_users", tags=['USER'])
def get_all_user():
    db = Session()
    result = User_Service(db).get_all_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@router.get( path="/get_user", tags=['USER_GET_OPTIONS'])

@router.post( path='/create_user', tags=['USER'])
def create_user(user:CreateUser):
    db = Session()
    new_user=User_Service(db).create_user(user)
    return JSONResponse(status_code=200, content={'message': f'User created successfuly. New user: {new_user}' })


@router.put( path='/update_user/{id}', tags=['USER'])
def update_user(id,user: UpdateUser):
    db = Session()
    user_updated = User_Service(db).update_user(user,id)
    if user_updated:
        return JSONResponse(status_code=201, content={'message': 'User updated successfuly'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})

@router.put( path='/update_firts_name_user/{id}', tags=['USER_UPDATE_OPTIONS'])
def update_firts_name_user(id:int, user: UpdateFirstName):
    db = Session()
    user_updated = User_Service(db).update_first_name_user(user,id)
    if user_updated:
        return JSONResponse(status_code=201, content={'message': 'User updated successfuly'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})
    


@router.put( path='/update_last_name_user/{id}/', tags=['USER_UPDATE_OPTIONS'])
def update_last_name_user(id:int, user:UpdateLastName):
    db = Session()
    user_updated = User_Service(db).update_first_name_user(user,id)
    if user_updated:
        return JSONResponse(status_code=201, content={'message': 'User updated successfuly'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})


@router.put( path='/update_email_user/{id}/', tags=['USER_UPDATE_OPTIONS'])
def update_email_user(id:int, user:UpdateEmail):
    db = Session()
    user_updated = User_Service(db).update_email_user(user,id)
    if user_updated:
        return JSONResponse(status_code=201, content={'message': 'User updated successfuly'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})



@router.put( path='/update_password_user/{id}/', tags=['USER_UPDATE_OPTIONS'])
def update_password_user(id:int, user:UpdatePassword):
    db = Session()
    user_updated = User_Service(db).update_password_user(user,id)
    if user_updated:
        return JSONResponse(status_code=201, content={'message': 'User updated successfuly'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})

@router.put( path='/update_phone_number_user/{id}/', tags=['USER_UPDATE_OPTIONS'])
def update_phone_number_user(id:int, user:UpdatePhoneNumber):
    db = Session()
    user_updated = User_Service(db).update_phone_number_user(user,id)
    if user_updated:
        return JSONResponse(status_code=201, content={'message': 'User updated successfuly'})
    return JSONResponse(status_code=404, content={'message': 'user not found'})



@router.delete( path='/delete_user/{id}', tags=['USER'])
def delete_user(id:int):
    pass