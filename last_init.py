#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
#from database_setup import Base, Menu, Series, Movie, Item
from flask import session as login_session
import random
import string
import excel
# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import pandas as pd
from tablib import Dataset




UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['xls', 'xlsb', 'xlsm', 'xlsx', 'xlt', 'xltx', 'xlw'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
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
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
                                    #filename=filename))
            file_path = UPLOAD_FOLDER + "/" + filename
            df = pd.read_excel(file_path)
            ## .shape get the len of row first and second number column
            ## it our case not big deal cus our files will be all same number column and rows
            ##print(df.shape[0])
            
            print("")

                 
            print(df.iloc[0][0])
            print(df.iloc[0][1])
            print(df.iloc[1][0])
            print(df.iloc[1][1])

            #for n in df.iloc[0]:
                #print(n)
            #print(df.iloc[0][0])
            #print(df.iloc[0][1])
            #print(df.iloc[1][0])
            #print(df.iloc[1][1])
            #for x in df:
             #   print(x)
                
            #print(df["a"])
            #f = open(file_path, "r")
            #print(f.read())                        
            return ""

            
                                    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Uploadaaaa new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''











@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080, threaded=False)
