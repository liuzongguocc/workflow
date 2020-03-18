from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('user',validators=[DataRequired(message='input')])
    password = PasswordField('pwd',validators=[DataRequired(message='input')])
    remember_me = BooleanField('remember')
    submit = SubmitField('login')
