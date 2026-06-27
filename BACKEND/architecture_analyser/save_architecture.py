import json
import os

def save_architecture(repo_id, architecture):
    os.makedirs("architectures", exist_ok=True)
    filename = repo_id.replace("/", "_") + ".json"
    with open(os.path.join("architectures", filename),"w",encoding="utf-8") as f:
        json.dump(architecture,f,indent=4)
