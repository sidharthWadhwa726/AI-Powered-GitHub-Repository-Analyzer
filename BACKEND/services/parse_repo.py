def parse_github_repo(repo_url):
    parts = repo_url.replace("https://github.com/","").split("/")
    if(len(parts) < 2):
        raise ValueError("Invalid Github Repo")
    # returning the tuple to avoid the overwriting 
    return (parts[0] , parts[1].replace(".git",""))

