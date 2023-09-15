from utils import create_pull_request


class DemoPr:
    def __init__(self, repo, targets_to_impact, fail=False):
        self.repo = repo
        self.targets_to_impact = targets_to_impact
        self.fail = fail
        self.p_r = ""

    def create(self):
        self.p_r = create_pull_request(self.repo, "main", self.targets_to_impact)
        print("done")

    def is_ready(self):
        print("ayy")

    def prepare(self):
        print("yoo")

    def enqueue(self):
        print("ooo")
