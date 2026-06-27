import json
import os
# this is just the file to laod the architecture in the json format 
def load_architecture(repo_id):
    filename = repo_id.replace("/", "_") + ".json"
    with open(os.path.join("architectures", filename),"r",encoding="utf-8") as f:
        return json.load(f)