from pydantic import BaseModel
# to check whether this user belongs to this repo or not 
class UserLogin(BaseModel):
    email : str 
    password : str 

