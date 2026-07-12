from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_data = None

    if request.method == "POST":
        username = request.form["username"]

        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()

    return render_template("index.html", user=user_data)

if __name__ == "__main__":
    app.run(debug=True)