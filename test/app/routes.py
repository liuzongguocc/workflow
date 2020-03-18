from flask import render_template
from app import app
from app.form import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'duck'}
    return render_template('index.html',title='my',user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='login',form=form)
