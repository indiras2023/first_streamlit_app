import streamlit
streamlit.title('My Moms New Healthy Dinner')
   
streamlit.header('Breakfast favorites')
streamlit.text('🥣Oatmeal & Milk')
streamlit.text('🥗Bluberry & Brocoli')
streamlit.text('🐔egg Hard-Boiled Egg & Waffels')
streamlit.text('🥑🍞 and Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
   streamlit.error("Please select a fruit to get information.")
else:
back_from_function=get_fruityvice_data(fruit_choice)
streamlit.dataframe(back_from_function)

except URLError as e:
streamlit.error()



