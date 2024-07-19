import requests as rq

def test_read_item():
    response = rq.get("http://127.0.0.1:8000/api/")
    assert response.status_code == 200
    assert response.json() == {True: "API is working!"}
