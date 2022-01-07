import os
import bcrypt
from dotenv import load_dotenv
from library import app
from flask import render_template, redirect, flash, url_for, request
from library.forms import register, login
from library.database import register_user, validate_username, pull_password


load_dotenv()

@app.route("/", methods=['POST', 'GET'])
@app.route("/home", methods=['POST', 'GET'])
def index():
	form = login()

	if form.validate_on_submit():
		validated_username = validate_username(form.username.data)

		stored_hash = pull_password(form.username.data)
		stored_hash = stored_hash.encode('utf-8')
		
		checkedHash = bcrypt.hashpw(form.password.data.encode('utf-8'), stored_hash)
		
		if checkedHash == stored_hash:
			validated_password = True
		else:
			validated_password = False

		if (validated_username == True) and (validated_password == True):
			flash(f'{form.username.data} welcome', category='success')
			return redirect(url_for('dashboard'))
		elif (validated_username == False):
			flash(f'{form.username.data} does not exist', category='danger')
			return redirect(url_for('index'))
		elif (validated_password == False):
			flash(f'Password entered is incorrect', category='danger')
			return redirect(url_for('index'))
		else:
			flash(f'Fatal Error', category='danger')
			return redirect(url_for('index'))

	return render_template('login.html', form=form)


@app.route("/signup", methods=['POST', 'GET'])
def signup():
	form = register()

	if form.validate_on_submit():
		if form.registration_number.data == os.getenv('REGISTRATION_NUMBER'):
			flash(f'Account successfully created for {form.username.data}', category='success')

			encrypted_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())

			register_user(form.first_name.data, form.last_name.data, form.phone_number.data, form.email.data, form.username.data, encrypted_password)

			return redirect(url_for('index'))
		else:
			flash(f'Registration number is invalid', category='danger')
			return redirect(url_for('signup'))

	return render_template('signup.html', form=form)
