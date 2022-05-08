from flask import Flask, render_template,redirect,flash,url_for
from app import app,db,bcrypt
from app.models import User, Pitch
from .forms import *


@app.route('/')
@app.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.date, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created successfully. You can now login', 'success')
        return redirect(url_for('signin'))
    return render_template('signUp.html', form= form)

@app.route('/signIn', methods=['GET', 'POST'])

def signIn():
    form=LogInForm()
    return render_template('signin.html', form= form)

@app.route('/comment', methods=['GET', 'POST'])

def comment():
    form=CommentForm()
    return render_template('comment.html', form= form)

@app.route('/addapitch', methods=['GET', 'POST'])

def newpitch():
    form=NewPitchForm()
    return render_template('newpitch.html', form= form)