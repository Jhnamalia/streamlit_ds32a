import requests
import joblib
import os
import streamlit as st
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize

def prediksi():
    imdb_joblib = joblib.load ('imdb_joblib')
    data_actor = pd.read_csv('actor rank.csv', sep='\t')

    data_actor['actor'] = data_actor['actor'].str.lower()