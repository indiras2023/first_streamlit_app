import streamlit
streamlit.title('My Moms New Healthy Dinner')
   
streamlit.header('Breakfast favorites')
streamlit.text('🥣Oatmeal & Milk')
streamlit.text('🥗Bluberry & Brocoli')
streamlit.text('🐔 Hard-Boiled Egg & Waffels')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
