import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Pages.fun.most_frequent_values import most_frequent_values as mfv
from Pages.fun.missing_data import missing_data as md

def general():
    st.header('Summary Analysis')
    #---START Data Loading------
    data = pd.read_csv('/Users/abilfad/Documents/NFT/tweet_analysis/tweet_scrap.csv')
    #---END Data Loading--------
   
    #---START Data Metrics------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tweets", f"{len(data.tweet.unique())}")
    col2.metric("Authors", f"{len(data.username.unique())}")
    col3.metric("Languages",f"{len(data.language.unique())}")
    col4.metric("Hashtags", f"{len(data.hashtags.unique())}")
    #---END Data Metrics--------

    #---START Data Information--
    st.subheader('Data Information')

    st.write('Authors Activity')
    data['date'] = pd.to_datetime(data['date'])
    st.table(data.resample('H',on='date').tweet.count())
    
    st.write('Tweet Engagement')
    st.table(data.describe().iloc[[1,3,7],:].astype('int'))
    #---END Data Information----
    
    #---START Data Language--
    st.write('Top 5 Tweet Langanges')
    st.table(data.language.value_counts().head())
    
    
    