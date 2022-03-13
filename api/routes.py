import logging
from flask import Blueprint, jsonify

from main.main import posthandler

api_bp = Blueprint('api', __name__)
logging.basicConfig(filename="basic.log", level=logging.INFO)


@api_bp.route('/posts/')
def get_list_posts_json():
    """Возвращает полный список постов в виде JSON-списка"""
    logging.info("Возвращаем все посты в виде JSON-списка")
    posts = posthandler.get_posts_all()
    return jsonify(posts)


@api_bp.route('/posts/<int:post_id>')
def get_post_json(post_id):
    """Возвращает один пост в виде JSON-словаря."""
    logging.info("Возвращаем пост в виде JSON-словаря")
    post = posthandler.get_post_by_pk(post_id)
    if post is None:
        return {"error": "Пост не найден"}, 404
    return jsonify(post)
