import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    # Main page instructions
    return "To send a message use /Username/Message "


@app.route("/<username>")
def user(username):
    return "Hi " + username.title()


@app.route("/<username>/<message>")
def send_message(username, message):
    return f"{username.title()}: {message}"


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
