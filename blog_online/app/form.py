from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField

from wtforms.validators import DataRequired


class loginform(FlaskForm):
    username = StringField('user', validators=[DataRequired(message='Please input')])
    password = PasswordField('pwd', validators=[DataRequired(message='please input ')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Login')
