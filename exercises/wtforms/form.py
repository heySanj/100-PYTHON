from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class MyForm(FlaskForm):
    # Have a look at the basic fields of WTForms: https://wtforms.readthedocs.io/en/2.3.x/fields/#basic-fields
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)]) # When validation is not met, a list of errors can be generated and passed into HTML
    submit = SubmitField(label='Sign me up!')