import pytest
import requests

@pytest.mark.live_api
class TestApiLive:
    live_api_url = "http://127.0.0.1:5000"

    @pytest.mark.parametrize("password, expected_strength", [
        ("%%%%%", "good"),
        ("@@@@@", "good"),
    ])
    def test_get_password_strength_good(self, password, expected_strength):
        response = requests.get(f'{self.live_api_url}/get_strength?password={password}')
        assert response.status_code == 200
        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == expected_strength

    @pytest.mark.parametrize("password", [
        ("abcdef"),
        ("password"),
    ])
    def test_get_password_strength_bad(self, password):
        response = requests.get(f'{self.live_api_url}/get_strength?password={password}')
        assert response.status_code == 200
        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == 'bad'

    def test_get_password_strength_empty(self):
        response = requests.get(f'{self.live_api_url}/get_strength?password=')
        assert response.status_code == 500

    @pytest.mark.parametrize("password, expected_strength", [
        ("%%%%%", "good"),
        ("@@@@", "good"),
    ])
    def test_post_password_strength_good(self, password, expected_strength):
        response = requests.post(f'{self.live_api_url}/get_strength', json={'password': password})
        assert response.status_code == 200
        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == expected_strength

    @pytest.mark.parametrize("password", [
        ("abcdef"),
        ("password"),
    ])
    def test_post_password_strength_bad(self, password):
        response = requests.post(f'{self.live_api_url}/get_strength', json={'password': password})
        assert response.status_code == 200
        data = response.json()
        assert data.get('password') == password
        assert data.get('strength') == 'bad'

    def test_post_password_strength_empty(self):
        response = requests.post(f'{self.live_api_url}/get_strength', json={'password': ''})
        assert response.status_code == 500
