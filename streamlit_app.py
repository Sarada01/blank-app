# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    """Choose the frits you want in your customer Smoothie!
    """
)

name_on_order = st.text_input("Name on the Smoothie:")
st.write(name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options") \
    .select(col("FRUIT_NAME"))

ingradient_list = st.multiselect("Choose upto 5 Ingredients:"
    , my_dataframe
    , max_selections = 5
    )
