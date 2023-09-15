import constants
from github import Auth, Github

auth = Auth.Token(constants.GH_ACCESS_TOKEN)

g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)

g.close()
