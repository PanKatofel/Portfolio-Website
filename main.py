from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

data = {
    'bs_portfolio': {
        "title": "Web Portfolio",
        "description": "A personal portfolio website built with Flask and Bootstrap, using Python.",
        "img_url_1": "assets/ptf_img/portfolio1.png",
        "img_url_2": "assets/ptf_img/portfolio2.png",
        "github_link": "https://github.com/PanKatofel/Portfolio-Website/tree/main"},

    'morse_code': {
        "title": "Morse Code Converter",
        "description": "A simple program for translating text to and from Morse code, showcasing a small portion of my Python abilities.",
        "img_url_1": "assets/ptf_img/morse1.png",
        "img_url_2": "assets/ptf_img/morse2.png",
        "github_link": "https://github.com/PanKatofel/Text-To-Morse-Code"},

    'fruit_ninja': {
        "title": "Unity - Fruit Ninja Lite",
        "description": "A copy of the game from my childhood, recreated using one of the best game engines in the world with C#",
        "img_url_1": "assets/ptf_img/fruit_ninja1.png",
        "img_url_2": "assets/ptf_img/fruit_ninja2.png",
        "github_link": "https://github.com/PanKatofel/Fruit-Ninja-Lite/tree/main"},
}


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/<string:project_name>")
def review(project_name):
    return render_template("review.html", data=data[project_name])

if __name__ == "__main__":
    app.run(debug=True)
