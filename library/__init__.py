import os
from flask import Flask
from dotenv import load_dotenv


# Initiilize .env
load_dotenv('library/bin/.env')

# Initilize Flask
app = Flask(__name__, template_folder="template", static_folder="template")
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))

# Initilize routes
from library import routes
