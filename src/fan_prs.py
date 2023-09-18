import logging

from github import Auth, Github

import constants
from demo_pr import DemoPr

logging.basicConfig(level="INFO")

auth = Auth.Token(constants.GH_ACCESS_TOKEN)

g = Github(auth=auth)

repo = g.get_repo(constants.REPO)

demo_pr = DemoPr(repo, ["1"])
demo_pr.create()
demo_pr.poll_until_targets_uploaded()
demo_pr.enqueue()

# clean_repo(repo)
