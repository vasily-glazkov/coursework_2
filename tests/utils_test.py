import utils
import pytest
from app import app
POSTS_DATA = "data/data.json"

allowed_keys = sorted(["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"])


def test_posts_api():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    assert type(response.json) == list
    for post in response.json:
        post_keys = sorted(list(post.keys()))
        assert post_keys == allowed_keys

    

def test_load_data():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert type(response.json) == dict
    post_keys = sorted(list(response.json.keys()))
    assert post_keys == allowed_keys


