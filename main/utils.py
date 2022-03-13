import json
import re

from exceptions import DataLayerError


class PostHandler:

    def __init__(self, path_posts, path_comments):
        self.path_posts = path_posts
        self.path_comments = path_comments

    @staticmethod
    def loads_json_from_file(file_path):
        """Загружаем данные из файла"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                posts = json.load(file)
            return posts
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataLayerError("Что-то не так с файлом")

    def get_posts_all(self):
        """Возвращает посты"""
        posts = self.loads_json_from_file(self.path_posts)
        return posts

    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""
        posts = self.get_posts_all()
        posts_found = []
        for post in posts:
            if user_name.lower() in post['poster_name'].lower():
                posts_found.append(post)
        return posts_found

    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        comments = self.loads_json_from_file(self.path_comments)
        post_comments = []
        for comment in comments:
            if post_id == comment["post_id"]:
                post_comments.append(comment)
        return post_comments

    def search_for_posts(self, query):
        """Возвращает список словарей по вхождению query"""
        posts = self.get_posts_all()
        posts_found = []
        for post in posts:
            post_words = re.sub(r'[^\w\s]', '', post['content'].lower()).split(" ")
            if query.lower() in post_words:
                posts_found.append(post)
        return posts_found

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его идентификатору"""
        posts = self.get_posts_all()
        found_post = None
        for post in posts:
            if pk == post["pk"]:
                found_post = post
                break
        return found_post
