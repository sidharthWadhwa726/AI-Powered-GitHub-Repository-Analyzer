from pydantic import BaseModel
# checking the repo request 
class RepoRequest(BaseModel):
    repo_url : str 
