import logging
import os
import sys

from flask import Flask, request, flash, redirect
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from werkzeug.utils import secure_filename
from program import Parser

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_PACK_EXTENSIONS = {'zip'}
ALLOWED_UNPACK_EXTENSIONS = {'bin'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

CORS(app)

def allowed_file(filename, extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions

@app.route('/')
def home():
    return 'Application works!'

@app.route('/unpackFile', methods=['POST'])
def unpackFile():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename, ALLOWED_UNPACK_EXTENSIONS):
        inputFileName = secure_filename(file.filename)
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exists." % (inputFileName,))
            flash("File or direcotry %s doesn't exists." % (inputFileName,))
            return redirect(request.url)
        if isDirectory:
            flash('Not supported yet')
            return redirect(request.url)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            Parser.unpackWatchFace(inputFileName)
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e,))
            import traceback
            traceback.print_stack()
            logging.exception(e)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
    return""

@app.route('/packFile', methods=['POST'])
def packFile():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename, ALLOWED_PACK_EXTENSIONS):
        inputFileName = secure_filename(file.filename)
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exists." % (inputFileName,))
            flash("File or direcotry %s doesn't exists." % (inputFileName,))
            return redirect(request.url)
        if isDirectory:
            flash('Not supported yet')
            return redirect(request.url)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            Parser.unpackWatchFace(inputFileName)
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e,))
            import traceback
            traceback.print_stack()
            logging.exception(e)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
    return""


if __name__ == '__main__':
    app.run()
