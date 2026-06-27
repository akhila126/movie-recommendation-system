from flask import Flask, render_template, request
from model import recommend

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommendation():
    movie_name = request.form["movie"]

    recommendations = recommend(movie_name)

    return render_template(
        "result.html",
        movie_name=movie_name,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)