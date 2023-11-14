import pytest
from suny485.projects.homework15.api import app


@pytest.fixture
def client_get_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def client_post_endpoint():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiGetThroughCode:
    @pytest.mark.parametrize("good_password", [
        ('@@@@@@'),
    ])
    def test_get_strength_good_password(self, client_get_endpoint, good_password):
        response = client_get_endpoint.get(f'/get_strength?password={good_password}')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['password'] == good_password
        assert response_data['strength'] == 'good'

    @pytest.mark.parametrize("bad_password", [
        ('password'),
    ])
    def test_get_strength_bad_password(self, client_get_endpoint, bad_password):
        response = client_get_endpoint.get(f'/get_strength?password={bad_password}')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['password'] == bad_password
        assert response_data['strength'] == 'bad'


class TestApiPostThroughCode:
    @pytest.mark.parametrize("good_password", [
        ('@@@@@@'),
    ])
    def test_post_strength_good_password(self, client_post_endpoint, good_password):
        payload = {'password': good_password}
        response = client_post_endpoint.post('/get_strength', json=payload)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['password'] == good_password
        assert response_data['strength'] == 'good'

    @pytest.mark.parametrize("bad_password", [
        ('password'),
    ])
    def test_post_strength_bad_password(self, client_post_endpoint, bad_password):
        payload = {'password': bad_password}
        response = client_post_endpoint.post('/get_strength', json=payload)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['password'] == bad_password
        assert response_data['strength'] == 'bad'
