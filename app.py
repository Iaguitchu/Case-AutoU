from flask import Flask
from blueprints.page import page


app = Flask(__name__, static_url_path='', static_folder='static')


app.register_blueprint(page)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)