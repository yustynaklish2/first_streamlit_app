import streamlit
import pandas
import requests


streamlit.title('My Mom\'s Healthy New Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

#make a pick list so users can see what they've selected
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


#display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#section header to display the repsonse
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())
