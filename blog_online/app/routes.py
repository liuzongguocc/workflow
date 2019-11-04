from app import app
from flask import render_template,flash,redirect,url_for
from app.form import loginform
@app.route('/login',methods=["GET","POST"])
def login():
    form = loginform()
    if form.validate_on_submit():
        flash("user name:{},if rememberme:{}".format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='login',form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username':"zliuzon"}
    posts = [
        {
            'author': {'username': 'liu'},
            'body': '1111111111111111'

        },
        {
            'author': {'username': 'qiang'},
            'body': '22222222222222'
        }
    ]

    return render_template("index.html", title='zliuzon', user=user ,posts=posts)