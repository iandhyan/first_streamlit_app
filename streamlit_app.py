import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('π₯£ Omega 3 & Blueberry Oatmeal')
streamlit.text('π₯Kale, Spinach & Rocket Smoothie')
streamlit.text('π Hard-Boiled Free-Range Egg')
streamlit.text('π₯π Avocado Toast')
streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')




import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Fruit Picker
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the table on page                      
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# Creates table of API data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
