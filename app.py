from flask import Flask, escape, request

from bcdp_test import predict_cancer

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome"


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/client')
def client():
    return app.send_static_file('Client.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/me', methods=['POST'])
def me_api():

    f = request.files['data']
    f.save('test_images/uploaded_file.jpg')

    result = predict_cancer('uploaded_file.jpg')
    return result

    # return {
    # "information": "dummy",
    # "image": "saved"
    # }


if __name__ == "__main__":
    app.run()
