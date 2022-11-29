#! /usr/bin/env python
from dotenv import load_dotenv
import os

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(WORKING_DIR, '.env'))

# Put your name here
NAME = ""
DESC = "This is a simple web app. It showcases some functions with Python Flask. It is built with Flask and " \
       "Bootstrap CSS"
SECRET_KEY = os.getenv('SECRET_KEY')
DB_FILE_NAME = 'data.json'
DB_FILE_FULL_PATH = os.path.join(WORKING_DIR, DB_FILE_NAME)
