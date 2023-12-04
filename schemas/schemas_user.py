from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    first_name: str = Field(max_length=45)
    last_name: str = Field(max_length=45)
    email: str = Field(max_length=45)
    password:str = Field(min_length=8)
    phone_number:int = Field(ge=1,le=20)
    group_id:int = Field(ge=1,le=4)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "first_name": "Peter",
                "last_name": "Gregory",
                "email": "PeterGregory@gmail.com",
                "password": "SecurityPassword Ex4mpl3 !",
                "phone_number": 5555551234,
                "group_id":2,
                }
            ]
            
        }
    }

class LoginUser(BaseModel):
    email: str  = Field(max_length=45)
    password: str = Field(min_length=8)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "email": "PeterGregory@gmail.com",
                "password": "SecurityPassword Ex4mpl3 !",
                }
            ]
            
        }
    }
    
class UpdateUser(BaseModel):
    first_name: str = Field(max_length=45)
    last_name: str = Field(max_length=45)
    email: str = Field(max_length=45)
    password:str = Field(min_length=8)
    phone_number:int = Field(ge=1,le=20)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "first_name": "Peter",
                "last_name": "Gregory",
                "email": "PeterGregory@gmail.com",
                "password": "SecurityPassword Ex4mpl3 !",
                "phone_number": 5555551234,
                }
            ]
            
        }
    }
    
class UpdateFirstName(BaseModel):
    first_name: str = Field(max_length=45)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "first_name": "Peter",
                }
            ]
            
        }
    }
    
class UpdateLastName(BaseModel):
    last_name: str = Field(max_length=45)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "last_name": "Gregory",
                }
            ]
            
        }
    }
    
class UpdateEmail(BaseModel):
    email: str = Field(max_length=45)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "email": "PeterGregory@gmail.com",
                }
            ]
            
        }
    }
    
class UpdatePassword(BaseModel):
    password:str = Field(min_length=8)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "password": "SecurityPassword Ex4mpl3 !",
                }
            ]
            
        }
    }
    
    
class UpdatePhoneNumber(BaseModel):
    phone_number:int = Field(ge=1,le=20)
    model_config = {
        
        "json_schema_extra":{
            "examples":[
                {
                "phone_number": 5555551234,
                }
            ]
            
        }
    }