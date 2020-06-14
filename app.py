# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger
#use api + /apidocs

app=Flask(__name__)#Start app, which point you start the app
Swagger(app)

pickle_in=open("..\DockerPrac\classifier.pkl",'rb')
classifier=pickle.load(pickle_in)

@app.route('/')#root path
def welcome():
    return "Hey Everyone"

@app.route('/predict')#by default both above one and this one is a get method
def predict_note_authenticate():

    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    


    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "predicted value is " + str(prediction)


@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    #Send the API call using POSTman
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    
    test_df=pd.read_csv(request.files.get("file"))#"..\DockerPrac\testPrac.csv"
    
    prediction=classifier.predict(test_df)
    
    return "predicted value is " + str(list(prediction))

if __name__=='__main__':
    app.run()

