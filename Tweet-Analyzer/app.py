
import streamlit as st
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns



apiKey = "X9H28AREvH3BoJojxrffOnY6l"
apiSecret = "h8AZAWLDLJDDp1gV4TmVcvGwBPGvR70JLJHeX0Stdpbqz4793g"
accessToken = "1251571335769108480-6XV5VbQtt2WqpUVGf1zvRSIe5B8Thj"
accessTokenSecret = "XFBfu2OevVXluKukHy2ySRKdNkp75H8RZuUKyVJXq7Rjo"


#Create the authentication object
authenticate = tweepy.OAuthHandler(apiKey, apiSecret) 
    
# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret) 
    
# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit = True)





def app():


	st.title("Sentwent Anayl 🤓")


	activities=["Sentwent System","Call Data Under Use"]

	choice = st.sidebar.selectbox("Features",activities)

	

	if choice=="Sentwent Anayl 🤓":

		st.subheader("Analyze the tweets of anyone on Twitter:")

		st.subheader("Model Features :")

        st.write("1. Generates a Word Cloud")
        st.write("2. Performs Sentiment Analysis a displays it in form of a Bar Graph")
		
        raw_text = st.text_area("Twitter username (NO LINK)")
		
		st.markdown("xxxxxxxxxx------MORE FEATURE AT SIDEBAR (on upleft corner)------xxxxxxxxxxx")

		Analyzer_choice = st.selectbox("Select Tasks 🏭",  ["Visualize the Sentiment Analysis","Generate WordCloud" ])


		if st.button("Work ⚙"):

			
			if Analyzer_choice=="Generate WordCloud":

				st.success("Getting Your Request🎇")

				def gen_wordcloud():

					posts = api.user_timeline(screen_name=raw_text, count = 100, lang ="en", tweet_mode="extended")


					# Create a dataframe with a column called Tweets
					df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
					# word cloud visualization
					allWords = ' '.join([twts for twts in df['Tweets']])
					wordCloud = WordCloud(width=500, height=300, random_state=21, max_font_size=110).generate(allWords)
					plt.imshow(wordCloud, interpolation="bilinear")
					plt.axis('off')
					plt.savefig('wordcloud.jpg')
					img= Image.open("wordcloud.jpg") 
					return img

				img=gen_wordcloud()

				st.image(img)



			else:



				
				def Plot_Analysis():

					st.success("Getting Your Request 🎨")
		

					posts = api.user_timeline(screen_name=raw_text, count = 100, lang ="en", tweet_mode="extended")

					df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])


					
					# Create a function to clean the tweets
					def cleanTxt(text):
					 text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
					 text = re.sub('#', '', text) # Removing '#' hash tag
					 text = re.sub('RT[\s]+', '', text) # Removing RT
					 text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
					 
					 return text


					# Clean the tweets
					df['Tweets'] = df['Tweets'].apply(cleanTxt)


					def getSubjectivity(text):
					   return TextBlob(text).sentiment.subjectivity

					# Create a function to get the polarity
					def getPolarity(text):
					   return  TextBlob(text).sentiment.polarity


					# Create two new columns 'Subjectivity' & 'Polarity'
					df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
					df['Polarity'] = df['Tweets'].apply(getPolarity)


					def getAnalysis(score):
					  if score < 0:
					    return 'Negative'
					  elif score == 0:
					    return 'Neutral'
					  else:
					    return 'Positive'
					    
					df['RESULT'] = df['Polarity'].apply(getAnalysis)


					return df



				df= Plot_Analysis()



				st.write(sns.countplot(x=df["RESULT"],data=df))


				st.pyplot(use_container_width=True)

	
	
	else:
        
		
		st.subheader("This features fetches the last 100 tweets from the twitter handel & Performs the Sentiment Analysisea")

		# st.write("1. Converts it into a DataFrame")
		# st.write("2. Cleans the text")
		# st.write("3. Analyzes Subjectivity of tweets and adds an additional column for it")
		# st.write("4. Analyzes Polarity of tweets and adds an additional column for it")
		# st.write("5. Analyzes Sentiments of tweets and adds an additional column for it")






		user_name = st.text_area("*Enter the exact twitter handle of the Personality (without @)*")

		st.markdown("xxxxxxxxxx------MORE FEATURE AT SIDEBAR (on upleft corner)------xxxxxxxxxxx")

		def get_data(user_name):

			posts = api.user_timeline(screen_name=user_name, count = 100, lang ="en", tweet_mode="extended")

			df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])

			def cleanTxt(text):
				text = re.sub('@[A-Za-z0–9]+', '', text) #Removing @mentions
				text = re.sub('#', '', text) # Removing '#' hash tag
				text = re.sub('RT[\s]+', '', text) # Removing RT
				text = re.sub('https?:\/\/\S+', '', text) # Removing hyperlink
				return text

			# Clean the tweets
			df['Tweets'] = df['Tweets'].apply(cleanTxt)


			def getSubjectivity(text):
				return TextBlob(text).sentiment.subjectivity

						# Create a function to get the polarity
			def getPolarity(text):
				return  TextBlob(text).sentiment.polarity


						# Create two new columns 'Subjectivity' & 'Polarity'
			df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
			df['Polarity'] = df['Tweets'].apply(getPolarity)

			def getAnalysis(score):
				if score < 0:
					return 'Negative'

				elif score == 0:
					return 'Neutral'


				else:
					return 'Positive'

		
						    
			df['Analysis'] = df['Polarity'].apply(getAnalysis)
			return df

		if st.button("Show Data"):

			st.success("Fetching Last 100 Tweets")

			df=get_data(user_name)

			st.write(df)






st.subheader(' ------------------------Created By :  Ayush Bhardwaj ---------------------- :rocket:')


			

				


























if __name__ == "__main__":
	app()