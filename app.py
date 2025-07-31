# pip install streamlit 
# python -m streamlit run app.py

import yfinance as yf
import streamlit as st

data = yf.download('aapl', start='2020-01-01',end='2024-01-01')
# Add  a title
st.title('اولين تجربه من از فارسي نويسي در استريم‌ليت')
# Add some text 
st.text('Streamlit is great')
st.button('Click')
st.slider('اسلايدر من',0,63,(25,45))
st.write('---')
st.write('##')
st.date_input('تاريخ امروز')
st.line_chart(data)

