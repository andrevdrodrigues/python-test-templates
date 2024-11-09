import requests
import json
import pytest

def test_simple_get_component_test_equals_200():
    # Arrange
    # As example, add some headers for the request
    headers = {
        'Accept': '*/*',
        'User-Agent': 'request'
    }

    # Act
    # Make a request passing the correct url, endpoint and headers
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1", headers=headers)
    json_object = json.loads(response.text)

    # Assert
    # Check the status code and returned fields
    assert response.status_code == 200
    assert json_object["userId"] == 1
    assert json_object["id"] == 1
    assert json_object["title"] == "delectus aut autem"
    assert json_object["completed"] == False

