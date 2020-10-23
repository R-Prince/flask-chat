import os
from flask import Flask, redirect, render_template, request, session
from datetime import datetime

app = Flask(__name__)
messages = []
app.secret_key = os.getenv("SECRET", "randomstring123")


def add_message(username, message):
    # Add message to the messages list with time stamp
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)


@app.route("/", methods=["GET", "POST"])
def index():
    # Prompt user to supply username and then direct to personal homepage
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        redirect(session["username"])

    return render_template("index.html")


@app.route("/<username>", methods=["GET", "POST"])
def user(username):
    # Display and add chat messages

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(session["username"])

    return render_template(
        "chat.html", username=username, chat_messages=messages)


app.run(host=os.getenv(
    "IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=False)
