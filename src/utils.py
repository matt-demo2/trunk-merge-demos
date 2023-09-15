import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    # trunk-ignore(bandit/B311)
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def create_pull_request(repo, source_branch, targets_to_impact):
    s_b = repo.get_branch(source_branch)
    t_b = f"branch_for_demo_{get_random_string(10)}"
    repo.create_git_ref(ref="refs/heads/" + t_b, sha=s_b.commit.sha)

    for target in targets_to_impact:
        repo.create_file(
            path=f"demo_workspace/target_{target}/files/{t_b}.txt",
            message="Create diff",
            content=get_random_string(100),
            branch=t_b,
        )

    pr_body = """
        THIS PR IS MANAGED BY THE TRUNK MERGE DEMO SCRIPT.

        It was openend for the purpose of demonstrating the merge graph, and either will be merged or eventually closed.
        """

    p_r = repo.create_pull(
        title=f"PR impacting targets {', '.join(targets_to_impact)}",
        body=pr_body,
        head=t_b,
        base="main",
    )
    print(p_r)
    return p_r
