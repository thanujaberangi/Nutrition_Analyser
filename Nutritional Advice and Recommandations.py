import streamlit as st
import json

# Load the JSON file
with open('advice.json', 'r') as file:
    advice = json.load(file)

# Display the form
st.title('Nutritional Advice and Recommendations')
fitness_goals = st.selectbox('Fitness Goals:', sorted(set(item['fitness_goal'] for item in advice['recommendations'])))
body_composition = st.selectbox('Body Composition:', sorted(set(item['body_composition'] for item in advice['recommendations'])))
dietary_preferences = st.selectbox('Dietary Preferences:', sorted(set(item['dietary_preferences'] for item in advice['recommendations'])))

# Get recommendations and advice
recommendations = [item['advice'] for item in advice['recommendations'] if item['fitness_goal'] == fitness_goals and item['body_composition'] == body_composition and item['dietary_preferences'] == dietary_preferences]

# Display recommendations
if recommendations:
    st.header('Personalized Recommendations:')
    for recommendation in recommendations:
        st.write(recommendation)
else:
    st.write('No recommendations found for the selected criteria.')
