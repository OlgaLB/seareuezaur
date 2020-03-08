#!/usr/bin/env python3

import pytest
import requests
import json

def test_search_iata_lower_case_full():
    response = requests.get('http://127.0.0.1:5000/api/IATA?iata=oca')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['iata'] == 'OCA'

def test_search_iata_upper_case_full():
    response = requests.get('http://127.0.0.1:5000/api/IATA?iata=OCA')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['iata'] == 'OCA'

def test_search_iata_non_existing():
    response = requests.get('http://127.0.0.1:5000/api/IATA?iata=ABCDEFG')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['iata'] != 'ABCDEFG'

def test_search_space_before():
    response = requests.get('http://127.0.0.1:5000/api/IATA?iata= oca')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['iata'] == 'OCA'

def test_search_iata_space_after():
    response = requests.get('http://127.0.0.1:5000/api/IATA?iata=oca ')
    assert response.status_code == 200
    data = json.loads(response.content)
    for record in data:
        assert record['iata'] == 'OCA'

def test_search_iata_wrong_parameter():
    response = requests.get('http://127.0.0.1:5000/api/IATA?ta=oca')
    assert response.status_code == 500

def test_search_iata_parameter_upper_case():
    response = requests.get('http://127.0.0.1:5000/api/IATA?IATA=oca ')
    assert response.status_code == 500

def test_search_iata_endpoint_lower_case():
    response = requests.get('http://127.0.0.1:5000/api/iata?iata=oca')
    assert response.status_code == 404

def test_search_iata_empty_parameter():
    response = requests.get('http://127.0.0.1:5000/api/IATA?iata')
    assert response.status_code == 500
