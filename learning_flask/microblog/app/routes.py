from flask import render_template, redirect, flash, url_for
from app import app 
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Goalra'}
    posts = [
        {
            'author': {'username': 'Golara'},
            'body': 'Beautiful day in Istanbul!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', posts=posts, user=user, title="home")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form, title="Sign In")