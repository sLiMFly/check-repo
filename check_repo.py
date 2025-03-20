import json
from urllib import request

def check_github_repos():
    username = "sLiMFly"
    key = "hero"
    api_url = f"https://api.github.com/users/{username}/repos"
    
    try:
        with request.urlopen(api_url) as response:
            if response.status == 200:
                repos = json.loads(response.read())
                heroes_repos = [repo['name'] for repo in repos if key in repo['name'].lower()]
                
                if heroes_repos:
                    print(f"Found repositories containing '{key}':")
                    for repo in heroes_repos:
                        print(f"- {repo}")
                else:
                    print(f"No repositories containing '{key}' were found.")
            else:
                print(f"Error accessing GitHub API: {response.status}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    check_github_repos()