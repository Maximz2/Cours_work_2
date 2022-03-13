from flask import Flask, render_template, request, jsonify

from utils import PostHandler

POST_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"

app = Flask(__name__)

app.register_blueprint(main_blueprint)

posthandler = PostHandler(POST_PATH, COMMENTS_PATH)


@app.route("/")
def tape_page():
    """Лента постов"""
    posts = posthandler.get_posts_all()
    count = len(posts)
    return render_template('index.html', posts=posts, count=count)


@app.route("/posts/<int:postid>")
def post_page(postid):
    """Просмотр поста"""
    post = posthandler.get_post_by_pk(postid)
    comments = posthandler.get_comments_by_post_id(postid)
    count = len(comments)
    return render_template('post.html', post=post, comments=comments, count=count)


@app.route("/search/")
def search_page():
    """Поиск поста"""
    s = request.args.get("s", "")
    posts = posthandler.search_for_posts(s)
    count = len(posts)
    return render_template('search.html', posts=posts, count=count, s=s)


@app.route("/users/<username>")
def user_page(username):
    """Посты пользователя"""
    posts = posthandler.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)


@app.route("/api/posts/")
def get_list_posts_json():
    """Возвращает полный список постов в виде JSON-списка"""
    posts = posthandler.get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def get_post_json(post_id):
    """Возвращает один пост в виде JSON-словаря."""
    post = posthandler.get_post_by_pk(post_id)
    if post is None:
        return {"error": ""}
    return jsonify(post)


# if __name__ == '__main__':
#     app.config['JSON_AS_ASCII'] = False
app.run()
