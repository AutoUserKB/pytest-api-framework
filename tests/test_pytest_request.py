import requests
import pytest



def test_get_user(base_url):
    response = requests.get(url=f"{base_url}/users/1", timeout = 5)
    assert response.status_code == 200, f"Expected 200 , got {response.status_code}"
    response_data = response.json()
    assert response_data["name"] == "Leanne Graham"
    assert response_data["id"] == 1    

    #assert response.json["name"] == "Leanne Graham" ---> Incorrect

@pytest.mark.learn_parameter
@pytest.mark.parametrize("id, expected_status_code",[(1,200),(2,200),(3,200),(9999,404)])
def test_check_status_code(base_url,id,expected_status_code):
    response = requests.get(f"{base_url}/users/{id}", timeout=5)
    assert response.status_code  == expected_status_code


def test_post(base_url):
    payload = {"title": "test", "body": "hello", "userId": 1}
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    }
    response = requests.post(url=f"{base_url}/posts", json = payload, headers = headers, timeout = 5)
    assert response.status_code == 201,f"Expected 201 got {response.status_code}"
    response_body = response.json()
    assert response_body["title"] == payload["title"]









