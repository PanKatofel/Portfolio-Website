from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


# -------------------------------------------------------------------
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["FLASK_KEY"]
app.config["CKEDITOR_CONFIG"] = {"versionCheck": False}
app.config["CKEDITOR_PKG_TYPE"] = 'standart'
app.config["CKEDITOR_SERVE_LOCAL"] = True

ckeditor = CKEditor(app)
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

# --------------------------------------------------------------------


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


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

        sg = SendGridAPIClient(os.environ["SENDGRID_KEY"])
        email = Mail(from_email=my_email, to_emails=my_email,
                     subject="Portfolio Contact",
                     plain_text_content=f"Contact {contact_email}\n\n{content}")
        sg.send(email)

        return redirect(url_for('contact', message="The message was sent successfully."))

    return render_template("contact.html", form=form, message=message)


# --------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
