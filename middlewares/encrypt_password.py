import bcrypt

def encrypt_password(password:str) -> bytes:
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password,salt=salt)
    return hashed
    
    
def verify_password(user_password:str, hash:bytes)->bool:
    user_password = user_password.encode('utf-8')
    if bcrypt.checkpw(user_password, hash):
        return True
    
    return False


crypt = encrypt_password('Navor123')
print(crypt)

print(verify_password('Navor123',crypt ))
    