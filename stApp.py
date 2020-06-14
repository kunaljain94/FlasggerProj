"""
Created on Mon Jun 15 00:43:54 2020

@author: kunal.jain
"""


### With Streamlit, integrates HTML code inside only

import pandas as pd
import numpy as np
import pickle
import streamlit as st

#https://docs.streamlit.io/en/latest/


pickle_in=open("..\DockerPrac\classifier.pkl",'rb')
classifier=pickle.load(pickle_in)


def welcome():
    return "Hey Everyone"


def predict_note_authentication(variance,skewness,curtosis,entropy):

    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "predicted value is " + str(prediction)


'''To run the app
conda create --name myenv
conda activate myenv
pip install streamlit

===>streamlit run app.py

 streamlit files to be added 
Copy streamlit files in C Users\AppData\Roaming\Python\Python36\Scripts and paste them into
your Anaconda Scripts

'''

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
        
if __name__=='__main__':
    main()#instead of app.run

