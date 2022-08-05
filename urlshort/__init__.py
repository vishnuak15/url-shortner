from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'djbadbbhh1b32h3b2bsndsjjdns32jn2bh3h2'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app 