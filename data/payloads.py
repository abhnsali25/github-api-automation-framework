def create_repo_payload(repo_name):
    return {
        "name": repo_name,
        "description": "Repository created via API automation",
        "private": False
    }


def update_repo_payload():
    return {
        "description": "Updated description via API automation"
    }