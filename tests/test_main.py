from main import app

client = app.test_client()

# GET '/' 가 200 status 를 주는지에 대한 테스트
def test_index():
    response = client.get('/')

    assert response.status_code == 200

# GET '/' 가 200 status 를 주는지에 대한 테스트
def test_404():
    response = client.get('/cute')

    assert response.status_code == 404