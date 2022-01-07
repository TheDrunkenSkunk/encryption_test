import os
import MySQLdb
from datetime import date
from dotenv import load_dotenv

load_dotenv()

db = {'host': str(os.getenv('HOST')),
		'user': str(os.getenv('USER')),
		'password': str(os.getenv('PASS')),
		'db': 'dbmaster'}

def register_user(first_name, last_name, phone_number, email, username, password):
	conn = MySQLdb.connect(**db)
	cursor = conn.cursor()

	cursor.execute(""" INSERT INTO user_id (date_created, username, user_pass, first_name, last_name, email, phone_number) VALUES(%s, %s, %s, %s, %s, %s, %s) """, (date.today, username, password, first_name, last_name, email, phone_number))
	conn.commit()
	cursor.close()
	conn.close()

def validate_username(username_input):
	conn = MySQLdb.connect(**db)
	cursor = conn.cursor()

	validated_username = cursor.execute("SELECT * FROM user_id WHERE username = %s", {username_input})
	
	if int(validated_username) == 1:
		return True
	else:
		return False

	cursor.close()
	conn.close()

def pull_password(username_input):
	conn = MySQLdb.connect(**db)
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM user_id WHERE username = %s", {username_input})

	validated_password = cursor.fetchone()

	return validated_password[3]

	cursor.close()
	conn.close()