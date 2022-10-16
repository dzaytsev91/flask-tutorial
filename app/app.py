# app.py
from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def hello():  # call method hello
    return "Hello World!"  # which returns "hello world"


@app.route("/<name>")  # at the end point /
def hello_test(name):  # call method hello
    return "Hello {}!".format(name)  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
