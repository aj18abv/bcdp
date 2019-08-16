import base64
import json
import matplotlib.pyplot as plt

from flask import Flask, escape, request

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Welcome!'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route("/me")
def me_api():
    # user = get_current_user()

    import base64

    with open("C:\\ML\\a.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    # test_image = Image.open('"C:\\ML\\a.jpg"')
    # test_image.show()

    return {
        "information": "dummy"
        # "image": encoded_string

        # "username": user.username,
        # "theme": user.theme,
        # "image": url_for("user_image", filename=user.image),
    }



