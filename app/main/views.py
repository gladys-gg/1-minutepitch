from flask import Flask, render_template
from . import main
from .forms import *

@main.route('/')
@main.route('/index')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    return render_template('signUp.html', form= form)

@main.route('/signIn', methods=['GET', 'POST'])
def signIn():
    form=LogInForm()
    return render_template('signin.html', form= form)
@main.route('/comment', methods=['GET', 'POST'])

def comment():
    form=CommentForm()
    return render_template('comment.html', form= form)
@main.route('/newpitch', methods=['GET', 'POST'])

def newpitch():
    form=NewPitchForm()
    return render_template('newpitch.html', form= form)