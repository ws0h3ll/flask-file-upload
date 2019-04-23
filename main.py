import os
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']) #file extensions that are allowed

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS #check if the file extensions is in the allowed files array

@app.route('/') #index
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST']) # post to the form
def upload_file():
	if request.method == 'POST': #if it is a post req
		if 'file' not in request.files: #if cant get file type
			flash('part of file missin')
			return redirect(request.url) #redirect home
		file = request.files['file']
		if file.filename == '': #if there is no file selected to upload
			flash('select file to upload')
			return redirect(request.url) # return home
		if file and allowed_file(file.filename): #if it is a valid file
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #save it to the server
			flash('File(s) successfully uploaded') #tell user it was a success
			return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,port=80) # run it
