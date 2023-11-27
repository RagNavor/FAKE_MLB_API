from schemas.schemas_user import CreateUser,UpdateUser,UpdateFirstName,UpdateLastName,UpdateEmail,UpdatePassword,UpdatePhoneNumber
from models.users import User
from datetime import datetime
from middlewares.encrypt_password import encrypt_password


class User_Service():
    def __init__(self, db):
        self.db = db
        
    
    def get_all_users(self):
        result = self.db.query(User).all()
        return result
    
    def get_user(self, id):
        pass
    
    def create_user(self, user:CreateUser):
        new_user = User(**user.model_dump())
        new_user.full_name = f'{user.first_name} {user.last_name}'
        new_user.password = encrypt_password(new_user.password)
        self.db.add(new_user)
        self.db.commit()
        self.db.close()
        return new_user
    
    def update_user(self,user:UpdateUser,id) -> User:
        user_to_update = self.db.query(User).get(id)
        if user_to_update == None:
            return False
        user_to_update.first_name = user.first_name
        user_to_update.last_name = user.last_name
        user_to_update.full_name = f'{user.first_name} {user.last_name}'
        user_to_update.email = user.email
        user_to_update.password = encrypt_password(user.password)
        user_to_update.phone_number = user.phone_number
        user_to_update.updated_at = datetime.now()
        self.db.commit()
        self.db.close()
        return user_to_update
    
    def update_first_name_user(self,user:UpdateFirstName,id):
        user_to_update = self.db.query(User).get(id)
        
        if user_to_update == None:
            return False
        user_to_update.first_name = user.first_name
        user_to_update.full_name = f'{user.first_name} {user_to_update.last_name}'
        user_to_update.updated_at = datetime.now()
        self.db.commit()
        self.db.close()
        return user_to_update
    
    
    def update_last_name_user(self,user:UpdateLastName,id):
        user_to_update = self.db.query(User).get(id) 
        if user_to_update == None:
            return False
        user_to_update.last_name = user.last_name
        user_to_update.full_name = f'{user_to_update.first_name} {user.last_name}'
        user_to_update.updated_at = datetime.now()
        self.db.commit()
        self.db.close()
        return user_to_update
        
    
    
    def update_email_user(self,user:UpdateEmail,id):
        user_to_update = self.db.query(User).get(id) 
        if user_to_update == None:
            return False
        user_to_update.email = user.email
        user_to_update.updated_at = datetime.now()
        self.db.commit()
        self.db.close()
        return user_to_update
    
    
    def update_password_user(self,user:UpdatePassword,id):
        user_to_update = self.db.query(User).get(id) 
        if user_to_update == None:
            return False
        user_to_update.password = encrypt_password(user.password)
        user_to_update.updated_at = datetime.now()
        self.db.commit()
        self.db.close()
        return user_to_update
    
    def update_phone_number_user(self,user:UpdatePhoneNumber,id):
        user_to_update = self.db.query(User).get(id) 
        if user_to_update == None:
            return False
        user_to_update.phone_number = user.phone_number
        user_to_update.updated_at = datetime.now()
        self.db.commit()
        self.db.close()
        return user_to_update
    def delete_user(self,id):
        pass
        
        
        
        
        
        
    
    