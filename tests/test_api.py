import pytest


def test_get_all_post(client, post_keys):
    response = client.get('api/posts/')
    assert response.status_code == 200
    assert isinstance(response.json, list)

    for element in response.json:
        if set(element.keys()) != set(post_keys):
            assert False


def test_get_post(client, post_keys, first_post):
    response = client.get('/api/posts/1')
    assert response.status_code == 200

    if set(response.json.keys()) != set(post_keys):
        assert False

    assert response.json == first_post


def test_get_post_by_wrong_id(client):
    response = client.get('api/posts/11')
    assert response.status_code == 404
    assert response.json == {"error": "Пост не найден"}
