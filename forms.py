from flask_ckeditor import CKEditorField
from wtforms import SubmitField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    email = EmailField("Enter Your Email", validators=[DataRequired(), Email()])
    content = CKEditorField("Email Body")
    submit = SubmitField("Send", render_kw={'class': 'btn btn-indigo'})