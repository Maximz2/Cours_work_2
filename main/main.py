import logging
from flask import Blueprint, render_template, request
from main.utils import PostHandler

from exceptions import DataLayerError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    """Лента постов"""
    logging.info("Запрошена главная страница")
    posthandler =
    posts = posthandler.get_posts_all()
    count = len(posts)
    return render_template('index.html', posts=posts, count=count)
