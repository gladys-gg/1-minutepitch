from flask import Flask, render_template,redirect,flash,url_for
from app import app,db,bcrypt
from app.models import User, Pitch
from .forms import *
from flask_login import login_user, current_user,logout_user,login_required


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
        user = User(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created successfully. You can now login', 'success')
        return redirect(url_for('signIn'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creatting the user:(err_msg)')
    return render_template('signUp.html', form= form)

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. PLease check email and password', 'danger')
    return render_template('signin.html', title = 'Login', form= form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    form=CommentForm()
    return render_template('comment.html', form= form)

@app.route('/addapitch', methods=['GET', 'POST'])
def newpitch():
    form=NewPitchForm()
    return render_template('newpitch.html', form= form)