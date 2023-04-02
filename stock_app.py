import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import requests
from bs4 import BeautifulSoup
from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
one_year_ago = today - relativedelta(years=1)
today_string = today.strftime('%Y-%m-%d')
one_year_ago_string = one_year_ago.strftime('%Y-%m-%d')



st.title("Welcome to the Stock Price App")
st.text("Analyze the performance of your favorite stock over the last year!")
ticker = st.text_input('Enter the ticker name of the stock','GOOGL')
st.markdown("Here are the ***Closing Price*** and ***Volume*** of "+ticker+":")
tickerdata = yf.Ticker(ticker)
tickerdf = tickerdata.history(period='1d',start=one_year_ago_string,end=today_string)

st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)


