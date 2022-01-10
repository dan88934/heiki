from flask import Flask
# from .input_blueprint import input_blueprint
# from .file_processing_blueprint import file_processing_blueprint
# from .doc_create_blueprint import doc_create_blueprint
from process_file import process_file # removed . 
# import os
app = Flask(__name__)
app.config["SECRET_KEY"] = "iuhto743yto34iuho287gh78"
# app.testing = True
TEMPLATES_AUTO_RELOAD=True
UPLOAD_FOLDER = './uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #This is the folder in which images will be placed before they are processed
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #This limits the maximum size for an individual file to 16 megabytes

#This is the main file which calls the blueprints
# app.register_blueprint(input_blueprint)
# app.register_blueprint(file_processing_blueprint)
# app.register_blueprint(doc_create_blueprint)

app.register_blueprint(process_file)