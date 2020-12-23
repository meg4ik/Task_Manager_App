from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, validators, ValidationError

class WritingForm(FlaskForm):
    content = StringField('content', validators = [validators.Length(min=4, max=200)])