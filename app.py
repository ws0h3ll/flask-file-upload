import os
from flask import Flask

UPLOAD_FOLDER = 'where to save to'
app = Flask(__name__)
app.secret_key = os.urandom(16) #encryption
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #upload folder
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024 * 1024 #maximum file size (i set mine to 200Gb)
