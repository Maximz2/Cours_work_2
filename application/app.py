from flask import Flask


def creat_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    from api.routes import api_bp
    from main.main import main_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
