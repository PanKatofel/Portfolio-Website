from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from forms import ContactForm
from env import load_env
import smtplib
import os

load_env()
# -------------------------------------------------------------------
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["FLASK_KEY"]
app.config["CKEDITOR_CONFIG"] = {"versionCheck": False}
app.config["CKEDITOR_PKG_TYPE"] = 'standart'
app.config["CKEDITOR_SERVE_LOCAL"] = True

ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)

data = {
    'morse_code': {
        "title": "Morse Code Converter",
        "description": "A simple program for translating text to and from Morse code, showcasing a small portion of my Python abilities.",
        "img_url_1": "assets/ptf_img/morse1.png",
        "img_url_2": "assets/ptf_img/morse2.png",
        "github_link": "https://github.com/PanKatofel/Text-To-Morse-Code",
        "icon_img": "assets/img/morse.jpg",
        "album_desc": "A simple Python project that converts text to Morse code and vice versa."
    },

    'bs_portfolio': {
        "title": "Web Portfolio",
        "description": "A personal portfolio website built with Flask and Bootstrap, using Python.",
        "img_url_1": "assets/ptf_img/portfolio1.png",
        "img_url_2": "assets/ptf_img/portfolio2.png",
        "github_link": "https://github.com/PanKatofel/Portfolio-Website/tree/main",
        "icon_img": "assets/img/www.jpg",
        "album_desc": "A combination of Flask and Bootstrap used to create my web portfolio."
    },

    'fruit_ninja': {
        "title": "Fruit Ninja Lite",
        "description": "A copy of the game from my childhood, recreated using one of the best game engines in the world with C#",
        "img_url_1": "assets/ptf_img/fruit_ninja1.png",
        "img_url_2": "assets/ptf_img/fruit_ninja2.png",
        "github_link": "https://github.com/PanKatofel/Fruit-Ninja-Lite/tree/main",
        "icon_img": "assets/img/ninja.jpg",
        "album_desc": "Recreation of the mobile game Fruit Ninja, made in Unity."
        },

    'tic_tac_toe': {
        "title": "Tic Tac Toe",
        "description": "Game of TicTacToe made in python that allows two players to compete using simple command-line inputs.",
        "img_url_1": "assets/ptf_img/tictactoe1.png",
        "img_url_2": "assets/ptf_img/tictactoe2.png",
        "github_link": "https://github.com/PanKatofel/TicTacToe",
        "icon_img": "assets/img/tictactoe.jpg",
        "album_desc": "A classic Tic-Tac-Toe game for two players to play in the terminal."
    },

    'watermark': {
        "title": "Image Watermark",
        "description": "An application built in Python using the Tkinter library to add watermarks to photos and download the edited images.",
        "img_url_1": "assets/ptf_img/watermark1.png",
        "img_url_2": "assets/ptf_img/watermark2.png",
        "github_link": "https://github.com/PanKatofel/Watermark-Add",
        "icon_img": "assets/img/watermarked.jpg",
        "album_desc": "An application that allows you to add a watermark to a photo and download it."
    },

    'type_test': {
        "title": "Typing Speed Test",
        "description": "A Tkinter application built entirely with Python that lets you test your typing speed and then summarizes your results.",
        "img_url_1": "assets/ptf_img/type_test1.png",
        "img_url_2": "assets/ptf_img/type_test2.png",
        "github_link": "https://github.com/PanKatofel/Typing-Speed-Tester",
        "icon_img": "assets/img/keyboard.jpg",
        "album_desc": "Assess your typing speed by entering a series of randomly generated words."
    },
}

# --------------------------------------------------------------------


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", data=data)


@app.route("/portfolio/<string:project_name>")
def review(project_name):
    return render_template("review.html", data=data[project_name])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    message = request.args.get('message')

    if form.validate_on_submit():
        my_email = os.environ["EMAIL"]
        contact_email = form.email.data
        content = form.content.data

        soup = BeautifulSoup(content, "html.parser")
        content = soup.get_text()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=os.environ["PASSWORD"])
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                    msg=f"Subject:Portfolio Contact\n\n"
                                        f"Contact: {contact_email}\n{content}")

        return redirect(url_for('contact', message="The message was sent successfully."))

    return render_template("contact.html", form=form, message=message)


# --------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
