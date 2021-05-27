# SentWent Main

Sentwent Main is an powerful analyzing web application powered by Machine Learning Algorithms. 

1.Analyze the tweets of anyone.

This tool performs the following tasks :

1. Generates a Word Cloud
2. Performs Sentiment Analysis a displays it in form of a Bar Graph

2.This tool fetches the last 100 tweets from the twitter handel & Performs the following tasks
Converts it into a DataFrame

### Cleans the text
1. Analyzes Subjectivity of tweets and adds an additional column for it
2. Analyzes Polarity of tweets and adds an additional column for it
3. Analyzes Sentiments of tweets and adds an additional column for it


This respository contains all the files for end to end model building and deployment of tweet analyzer web app

Procfile : To generate command to run the app

Sentiment_Analysis_.ipynb : Model building File


Requirements.txt: Requirement file

setup.sh : predefined file for streamlite on heroku


## NOTE
Anyone running the mainapp.py should have Access Tokens,Key Secrets,API key and authentication.(Twitter Developer Authentication).



This app is created on a tool called Streamlit which saves you from the headache of front-end devlopment ,you can install it by:
Streamlit documentation: https://docs.streamlit.io/en/latest/

pip install streamlit

& to run it on local host : streamlit run mainapp.py
