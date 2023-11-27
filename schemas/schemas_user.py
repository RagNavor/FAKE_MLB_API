from pydantic import BaseModel

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password:str
    phone_number:int

class LoginUser(BaseModel):
    email: str 
    password: str
    
class UpdateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password:str
    phone_number:int
    
class UpdateFirstName(BaseModel):
    first_name: str
    
class UpdateLastName(BaseModel):
    last_name: str
    
class UpdateEmail(BaseModel):
    email: str
    
class UpdatePassword(BaseModel):
    password:str
    
class UpdatePhoneNumber(BaseModel):
    phone_number:int