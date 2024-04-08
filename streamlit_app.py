import streamlit as st
from snowflake.snowpark.functions import col
import requests
import pandas

st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """ Choose the fruits you want in your custom Smoothie!
    """)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
