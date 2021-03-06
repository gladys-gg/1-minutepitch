from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. PLease choose a different one.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. PLease choose a different one.')
    
class LogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. PLease choose a different one.')
    
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. PLease choose a different one.')
    
    
class CommentForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
    
    
class NewPitchForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    title = StringField('Title', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    newPitch =StringField('New Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit Pitch')