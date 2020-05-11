#!/usr/bin/env python3

import pytest
import requests
import json


def test_search_name_lower_case_partial():
    response = requests.get('http://127.0.0.1:5000/api/name?name=tegel')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] == 'Berlin-Tegel Airport'

def test_search_name_upper_case_partial():
    response = requests.get('http://127.0.0.1:5000/api/name?name=TEGEL')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] == 'Berlin-Tegel Airport'

def test_search_name_lower_case_full():
    response = requests.get('http://127.0.0.1:5000/api/name?name=berlin-tegel airport')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] == 'Berlin-Tegel Airport'

def test_search_name_upper_case_full():
    response = requests.get('http://127.0.0.1:5000/api/name?name=BERLIN-TEGEL AIRPORT')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] == 'Berlin-Tegel Airport'

def test_search_name_non_existing():
    response = requests.get('http://127.0.0.1:5000/api/name?name=ABCDEFG')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] != 'ABCDEFG'

def test_search_space_before():
    response = requests.get('http://127.0.0.1:5000/api/name?name= tegel')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] == 'Berlin-Tegel Airport'

def test_search_name_space_after():
    response = requests.get('http://127.0.0.1:5000/api/name?name=tegel ')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['name'] == 'Berlin-Tegel Airport'

def test_search_name_list_of_airports():
    response = requests.get('http://127.0.0.1:5000/api/name?name=teg')
    assert response.status_code == 200
    data = json.loads(response.content)
    assert len(data) == 5

def test_search_name_endpoint_upper_case():
    response = requests.get('http://127.0.0.1:5000/api/NAME?name=tegel')
    assert response.status_code == 404

def test_search_name_parameter_upper_case():
    response = requests.get('http://127.0.0.1:5000/api/name?NAME=tegel')
    assert response.status_code == 500

def test_search_name_wrong_parameter():
    response = requests.get('http://127.0.0.1:5000/api/name?nme=teg')
    assert response.status_code == 500

def test_search_name_empty_parameter():
    response = requests.get('http://127.0.0.1:5000/api/name?name')
    assert response.status_code == 500
