import streamlit as st
import json

# Load the JSON data
with open('dietdata.json', 'r') as file:
    food_data = json.load(file)

# Streamlit app
def main():
    st.title("Calories Calculator")

    # Display food items and allow selection
    selected_food_items = st.multiselect("Select Food Items:", [food_item["name"] for food_item in food_data["food_items"]])

    # Calculate total calories
    total_calories = sum([food_item["calories"] for food_item in food_data["food_items"] if food_item["name"] in selected_food_items])

    # Display total calories
    st.write(f"Total Calories: {total_calories} kcal")

if __name__ == '__main__':
    main()
