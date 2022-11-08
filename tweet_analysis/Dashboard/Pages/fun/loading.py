import time
import streamlit as st
my_bar = st.progress(0)
def load(n):
    for percent_complete in range(n):
         time.sleep(0.1)
         my_bar.progress(percent_complete + 10)