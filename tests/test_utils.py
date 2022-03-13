import pytest

from main.utils import PostHandler
from settings import POST_PATH, COMMENTS_PATH


class TestPosthandler:

    def test_loads_json_from_file(self):
        posthandler = PostHandler(POST_PATH, COMMENTS_PATH)
        assert isinstance(posthandler.loads_json_from_file(POST_PATH), list)
        assert isinstance(posthandler.loads_json_from_file(COMMENTS_PATH), list)

    def test_get_posts_all(self):
        posthandler = PostHandler(POST_PATH, COMMENTS_PATH)
        assert isinstance(posthandler.get_posts_all(), list)

    def test_get_posts_by_user(self):
        posthandler = PostHandler(POST_PATH, COMMENTS_PATH)
        name = "leo"
        posts = posthandler.get_posts_by_user(name)
        for post in posts:
            assert post.get("poster_name") == name

    def test_get_comments_by_post_id(self):
        posthandler = PostHandler(POST_PATH, COMMENTS_PATH)
        post_id = 1
        comments = posthandler.get_comments_by_post_id(post_id)
        for comment in comments:
            assert comment.get("post_id") == post_id

    def test_search_for_posts(self):
        posthandler = PostHandler(POST_PATH, COMMENTS_PATH)
        query = "еда"
        posts = posthandler.search_for_posts(query)
        for post in posts:
            assert query in post.get("content")

    def test_get_post_by_pk(self):
        posthandler = PostHandler(POST_PATH, COMMENTS_PATH)
        pk = 1
        post = posthandler.get_post_by_pk(pk)
        assert post.get("pk") == pk
