import pytest
from data.payloads import update_repo_payload

USERNAME = "abhnsali25" 

@pytest.mark.smoke
def test_get_repo(api,created_repo):
    response = api.get_repo(USERNAME,created_repo)
    print("\n\nFETCHING:", created_repo)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == created_repo

@pytest.mark.smoke
@pytest.mark.parametrize("username", ["abhnsali25","octocat"])
def test_get_user(api, username):
    response = api.get_user(username)
    data = response.json()
    assert response.status_code == 200
    assert data["login"] == username
    assert "public_repos" in data

@pytest.mark.regression
def test_update_repo(api,created_repo):
    payload = update_repo_payload()
    response = api.update_repo(USERNAME, created_repo, payload)
    assert response.status_code == 200
    data = response.json()
    assert "Updated description" in data["description"]

@pytest.mark.regression
def test_delete_repo(api, created_repo):
    response = api.delete_repo(USERNAME, created_repo)
    assert response.status_code == 204
    response2 = api.delete_repo(USERNAME, created_repo)
    assert response2.status_code == 404

@pytest.mark.regression
def test_get_user_invalid(api):
    invalid_username = "thisuserdoesnotexist123456"
    response = api.get_user(invalid_username)
    assert response.status_code == 404
    data = response.json()
    assert "Not Found" in data["message"]

@pytest.mark.regression
def test_get_repo_invalid(api):
    invalid_repo = "fake-repo-12345"
    response = api.get_repo(USERNAME, invalid_repo)
    assert response.status_code == 404
    data = response.json()
    assert "Not Found" in data["message"]
