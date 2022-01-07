import os
from flask import Flask
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt


# Initiilize .env
load_dotenv('library/bin/.env')

# Initilize Flask
app = Flask(__name__, template_folder="template", static_folder="template")
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))

# Initilize the bcrypt
bcrypt = Bcrypt(app)

# Initilize routes
from library import routes
