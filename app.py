from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# os.urandom(24)
app.secret_key = '\xa8\xe5\xff{\x04\xed@\xf8^&\xee\xdf\xf7N,[\xc3^\xec^\xd6(7\x87'

import os

app.config.from_object(os.environ['APP_SETTINGS'])

# UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# create the salalchemy object
db = SQLAlchemy(app)

from models import *

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    posts = []
    try:
        posts = db.session.query(BlogPost).all()
    except:
        flash("You have no database!")

    return render_template('index.html', posts = posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out.')
    return redirect(url_for('welcome'))



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')