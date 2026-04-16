from api.base_api import BaseAPI
from utils.config import BASE_URL
import logging

logger = logging.getLogger(__name__)

class GitHubAPI(BaseAPI):

    def get_user(self, username):
        url = f"{BASE_URL}/users/{username}"
        return self.send_request("GET", url)

    def get_repo(self, username, repo_name):
        url = f"{BASE_URL}/repos/{username}/{repo_name}"
        return self.send_request("GET", url)

    def list_repos(self, username):
        url = f"{BASE_URL}/users/{username}/repos"
        return self.send_request("GET",url)

    def create_repo(self, payload):
        url = f"{BASE_URL}/user/repos"
        return self.send_request("POST",url, data=payload)

    def update_repo(self, owner, repo_name, payload):
        url = f"{BASE_URL}/repos/{owner}/{repo_name}"
        return self.send_request("PATCH",url, data=payload)

    def delete_repo(self, owner, repo_name):
        url = f"{BASE_URL}/repos/{owner}/{repo_name}"
        return self.send_request("DELETE",url)