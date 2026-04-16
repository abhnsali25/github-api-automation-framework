import pytest
import utils.logger
from api.github_api import GitHubAPI
from data.payloads import create_repo_payload  
import time  

@pytest.fixture(scope="module")
def api():
    return GitHubAPI()

@pytest.fixture(scope="module")
def repo_name():
    return f"test-repo-{int(time.time())}"

@pytest.fixture(scope="module")
def created_repo(api, repo_name):
    payload = create_repo_payload(repo_name)
    response = api.create_repo(payload)
    if response.status_code == 201:
        return repo_name
    elif response.status_code == 422:
    # Repo might already exist due to retry/timeout
        print("Repo already exists, continuing...")
        return repo_name
    else:
        assert False, f"Unexpected status code: {response.status_code}"