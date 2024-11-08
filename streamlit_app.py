# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the frits you want in your customer Smoothie!
    """
)
cnx = st.connection("snowflake")
session = cnx.session()
