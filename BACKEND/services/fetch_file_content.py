import requests
def fetch_file_content(owner,repo,file_path):
    url = (f"https://raw.githubusercontent.com/"
           f"{owner}/{repo}/HEAD/{file_path}")
    try:
        response = requests.get(url)
        return response.text
    except:
        return None