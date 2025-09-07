import requests
import pytest


def test_get_booking():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.status_code == 200


def test_invalid_endpoint():
    response = requests.get("https://restful-booker.herokuapp.com/invalid")
    assert response.status_code == 404


# def test_create_booking():
#    payload = {"firstname": "John", "lastname": "Doe"}
#    response = requests.post(
#        "https://restful-booker.herokuapp.com/booking", json=payload)
#    assert response.status_code == 400  # Expecting bad request for missing fields
