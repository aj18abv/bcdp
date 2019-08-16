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
    return {
        "information": "dummy"
        # "image": encoded_string

        # "username": user.username,
        # "theme": user.theme,
        # "image": url_for("user_image", filename=user.image),
    }


if __name__ == "__main__":
    app.run()
