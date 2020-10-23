import os
from flask import Flask, redirect
from datetime import datetime

app = Flask(__name__)
messages = []


def add_message(username, message):
    # Add message to the messages list with time stamp
    now = datetime.now().strftime("%H:%M:%S")
    messages.append(f"{username.title()}: {message} ({now})")


def get_all_messages():
    # Adding a break between all messages
    return "<br>".join(messages)


@app.route("/")
def index():
    # Main page instructions
    return "To send a message use /Username/Message "


@app.route("/<username>")
def user(username):
    # Display chat message
    return f"<h1>Welcome {username.title()}</h1> {get_all_messages()}"


@app.route("/<username>/<message>")
def send_message(username, message):
    # Create chat message and redirect back to chat page
    add_message(username, message)
    return redirect("/" + username)


app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)
