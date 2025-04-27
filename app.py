from flask import Flask, request, redirect, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    search = None
    articles = []
    if request.method == "POST":
        search = request.form.get("query")
        api_key = "600d17c16d624dfaa0f20e86cd403976"
        url = f"https://newsapi.org/v2/everything?q={search}&apiKey={api_key}&language=en"
        respone = requests.get(url)

        if respone.status_code == 200:
            data = respone.json()
            articles = data["articles"]
        else:
            articles = []
    return render_template("index.html", search = search, articles=articles)

if __name__ == "__main__":
    app.run(debug=True)