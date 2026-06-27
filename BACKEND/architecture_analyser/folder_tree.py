# this is the main loop for the folder tree 
def build_folder_tree(repo_files):
    tree = {}
    for file in repo_files:
        path = file['path']
        path_list = path.split('/')

        curr = tree
        for part in path_list:
            if part not in curr : 
                curr[part]  = {}
            curr = curr[part]
            # initialise empty then push into it 
    return tree 