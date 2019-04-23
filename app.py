import os
from flask import Flask

UPLOAD_FOLDER = 'C:/Users/Visitor/uploads'
app = Flask(__name__)
app.secret_key = os.urandom(16)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024 * 1024
