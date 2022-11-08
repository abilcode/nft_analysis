import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Pages.user import user_analysis as pageUser
from Pages.word import word_analysis as pageWord
from Pages.sentiment import sentiment_analysis as pageSentiment
from Pages.general import general as pageGeneral
#from Pages.fun.loading import load as load

#-----START Load Data------
data = pd.read_csv('/Users/abilfad/Documents/NFT/tweet_analysis/tweet_scrap.csv')
data['date'] = pd.to_datetime(data['date'])
#-----END Load Data------

#st.set_page_config(page_title='My Dashboard',layout='wide')
st.title(f"NFT Tweet Analysis :{data['date'].dt.date.unique()} ")

#---START Sidebar----
st.sidebar.subheader("Menu")
genre = st.sidebar.radio(
     "Select desired menu below : ",
     ('General', 'User', 'Word','Sentiment'))
if genre =='User':
    #load(100)
    st.write(f'Ini Page: {genre}')
    
    pageUser()
elif genre == 'Word':
    #load(100)
    st.write(f'Ini Page: {genre}')
    pageWord()
elif genre =='Sentiment':
   #load(100)
    st.write(f'Ini Page: {genre}')
    pageSentiment()
else:
    #load(100)
    st.write(f'Ini Page: {genre}')
    pageGeneral()
#---END Sidebar----

