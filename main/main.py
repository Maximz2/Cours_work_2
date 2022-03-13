import logging
from flask import Blueprint, render_template, request

from settings import POST_PATH, COMMENTS_PATH
from main.utils import PostHandler

from exceptions import DataLayerError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)
posthandler = PostHandler(POST_PATH, COMMENTS_PATH)


@main_blueprint.route('/')
def tape_page():
    """Лента постов"""
    logging.info("Запрошена главная страница")
    posts = posthandler.get_posts_all()
    count = len(posts)
    return render_template('index.html', posts=posts, count=count)


@main_blueprint.route("/posts/<int:postid>")
def post_page(postid):
    """Просмотр поста"""
    logging.info("Запрошена страница поста с комментариями")
    post = posthandler.get_post_by_pk(postid)
    comments = posthandler.get_comments_by_post_id(postid)
    count = len(comments)
    return render_template('post.html', post=post, comments=comments, count=count)


@main_blueprint.route("/search/")
def search_page():
    """Поиск поста"""
    logging.info("Выполняется поиск")
    s = request.args.get("s", "")
    try:
        posts = posthandler.search_for_posts(s)
        count = len(posts)
        return render_template('search.html', posts=posts, count=count, s=s)
    except DataLayerError:
        return "Поврежден файл с данными"


@main_blueprint.route("/users/<username>")
def user_page(username):
    """Посты пользователя"""
    logging.info("Запрошены посты пользователя")
    posts = posthandler.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)
