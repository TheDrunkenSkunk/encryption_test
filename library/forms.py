import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms_alchemy import PhoneNumberField



class login(FlaskForm):
	username = StringField(label='Username:		', validators=[DataRequired(), Length(min=3, max=20)])
	password = PasswordField(label='Password:	', validators=[DataRequired(), Length(min=6, max=20)])
	login = SubmitField(label='Login')
	reset_password = SubmitField(label='Reset Password')

class register(FlaskForm):
	registration_number = StringField(label='Registration Number: ', validators=[DataRequired()])
	first_name = StringField(label='First name:	', validators=[DataRequired(), Length(min=1, max=35)])
	last_name = StringField(label='Last name: 	', validators=[DataRequired(), Length(min=1, max=35)])
	phone_number = PhoneNumberField(label='Phone number:	', validators=[DataRequired()])
	email = StringField(label='Email:	',validators=[DataRequired(), Email()])
	username = StringField(label='Username:	', validators=[DataRequired(), Length(min=3, max=20)])
	password = PasswordField(label='Password:	', validators=[DataRequired(), Length(min=6, max=20)])
	confirm_password = PasswordField(label='Confirm password:	', validators=[DataRequired(), Length(min=6, max=20), EqualTo('password')])
	submit = SubmitField(label='Register')
	reset_field = SubmitField(label='Reset field')

class add_turtle(FlaskForm):
	turtle_id = StringField(label='Animal ID: ', validators=[DataRequired(), Length(min=3, max=20)])
	common_name = StringField(label='Common name: ', validators=[DataRequired(), Length(max=100 )])
