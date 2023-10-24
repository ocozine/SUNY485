'''
Planning out my testing

1. Testing evaluation of strength
   - Testing a "good" password
   - Testing a "bad" password

2. Testing Inputs
    - Empty password (This should raise a divsion by zero error)
'''

import json
import pytest
from suny485.projects.homework14.api import app  # this is the flask app


# this is a pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# this is a simplified happy path test
def test_expect_good(client):
    # call the API, get the server response
    response = client.get('/get_strength?password=%%%%%%%')
    assert response.status_code == 200

    # convert the json payload to a dict
    data = json.loads(response.data.decode())

    assert data.get('password') == '%%%%%%%'
    assert data.get('strength') == 'good'


# this is an example very negative test
def test_api_error(client):
    # disambiguate
    password = '#password'

    with pytest.raises(ZeroDivisionError):
        response = client.get(f"/get_strength?password={password}")


low_complexity_passwords = [
    ("thisIsaWeakpassword!", "bad"),
    ("12345", "bad"),
    ("abcd", "bad"),
]


# Parametrization testing of bad passwords
@pytest.mark.parametrize("password, expected_strength", low_complexity_passwords)
def test_low_complexity_password(client, password, expected_strength):
    response = client.get(f'/get_strength?password={password}')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == expected_strength


high_complexity_passwords = [
    ("=======", "good"),
    ("%%%%%%%%%%%%%%%%%%", "good"),
    ("-------", "good"),
]


# Parametrization testing of good passwords
@pytest.mark.parametrize("password, expected_strength", high_complexity_passwords)
def test_high_complexity_password(client, password, expected_strength):
    response = client.get(f'/get_strength?password={password}')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert data.get('password') == password
    assert data.get('strength') == expected_strength


# Testing a empty password
def test_empty_password(client):
    password = ''
    with pytest.raises(ZeroDivisionError):
        response = client.get(f"/get_strength?password={password}")
        assert response.status_code == 200
