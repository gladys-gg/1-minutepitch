from flask import Flask, render_template
from app import app
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