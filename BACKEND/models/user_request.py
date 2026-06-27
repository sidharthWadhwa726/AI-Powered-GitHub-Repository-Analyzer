from pydantic import BaseModel
# this is used when we done the authentication 
class UserCreate(BaseModel):
    username : str 
    email : str 
    password : str 
    