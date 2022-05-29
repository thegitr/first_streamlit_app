import streamlit

streamlit.title("My Parents' Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Idli")
streamlit.text("🥣 Dosa")
streamlit.text("🥣 Puri")

streamlit.header("🍒🍒🍒 Make your own fruit smoothie 🍒🍒🍒")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
