def generate_recommendations(criteria):
    recommendations = []
    if "vegan" in criteria:
        recommendations.append("Incorporate more plant-based protein sources like lentils, beans, and tofu.")
    if "low-carb" in criteria:
        recommendations.append("Focus on high-fiber vegetables and lean protein sources.")
    if "high-protein" in criteria:
        recommendations.append("Include a variety of lean meats, eggs, and plant-based protein sources.")
    if "gluten-free" in criteria:
        recommendations.append("Choose gluten-free grains like quinoa, brown rice, and oats.")
    if "dairy-free" in criteria:
        recommendations.append("Use plant-based milk alternatives like almond or oat milk.")
    if "nut-free" in criteria:
        recommendations.append("Avoid all nuts and nut products, and use seed butters instead.")
    if "soy-free" in criteria:
        recommendations.append("Replace soy-based products with other plant-based protein sources.")
    if "muscle-building" in criteria:
        recommendations.append("Incorporate strength training exercises and increase protein intake.")
    if "weight-loss" in criteria:
        recommendations.append("Focus on portion control and include more vegetables in your meals.")
    if "endurance" in criteria:
        recommendations.append("Include complex carbohydrates and focus on cardiovascular exercises.")
    if "strength-training" in criteria:
        recommendations.append("Incorporate resistance training exercises and increase protein intake.")
    if "flexibility" in criteria:
        recommendations.append("Include stretching and mobility exercises in your routine.")
    if "cardiovascular-health" in criteria:
        recommendations.append("Engage in regular aerobic activities and focus on heart-healthy foods.")
    return recommendations

import streamlit as st
import json

# Load the JSON file
with open('meal.json', 'r') as f:
    data = json.load(f)

# Sample meal plans
meal_plans = {
    ("vegetarian", "muscle-building"): [
        "Breakfast: Tofu scramble with spinach, avocado, and whole-grain toast",
        "Lunch: Lentil and quinoa salad with roasted vegetables",
        "Dinner: Vegetarian chili with brown rice and a side salad",
        "Snack: Greek yogurt with mixed berries and almonds"
    ],
    ("vegan", "endurance"): [
        "Breakfast: Overnight oats with chia seeds, almond milk, and mixed berries",
        "Lunch: Chickpea and lentil curry with brown rice",
        "Dinner: Baked sweet potato with sautéed kale and tempeh",
        "Snack: Banana with almond butter"
    ],
    ("low-carb", "weight-loss"): [
        "Breakfast: Veggie omelet with avocado and a side of mixed nuts",
        "Lunch: Grilled salmon with roasted asparagus and a side salad",
        "Dinner: Zucchini noodles with pesto and grilled chicken",
        "Snack: Cucumber slices with hummus"
    ],
    ("high-protein", "strength-training"): [
        "Breakfast: Egg white and turkey bacon omelette with whole-grain toast",
        "Lunch: Grilled chicken breast with quinoa and roasted Brussels sprouts",
        "Dinner: Lean steak with roasted sweet potatoes and steamed broccoli",
        "Snack: Greek yogurt with mixed nuts and berries"
    ],
    ("gluten-free", "flexibility"): [
        "Breakfast: Gluten-free oatmeal with almond butter, banana, and cinnamon",
        "Lunch: Grilled salmon with quinoa and a mixed green salad",
        "Dinner: Stir-fried tofu and vegetables with brown rice",
        "Snack: Apple slices with almond butter"
    ],
    ("dairy-free", "cardiovascular-health"): [
        "Breakfast: Smoothie bowl with almond milk, spinach, and mixed berries",
        "Lunch: Grilled chicken salad with mixed greens and balsamic vinaigrette",
        "Dinner: Lentil and vegetable soup with gluten-free bread",
        "Snack: Carrot and hummus"
    ]
}

# Streamlit app
st.title("Meal Planning and Optimization")

# Dietary Requirements
st.sidebar.subheader("Dietary Requirements")
dietary_reqs = st.sidebar.multiselect("Select your dietary requirements", data["dietaryRequirements"])

# Fitness Goals
st.sidebar.subheader("Fitness Goals")
fitness_goals = st.sidebar.multiselect("Select your fitness goals", data["fitnessGoals"])

# Generate Meal Plan
if st.sidebar.button("Generate Meal Plan"):
    # Implement your meal plan generation logic here
    if dietary_reqs and fitness_goals:
        meal_plan_key = tuple(set(dietary_reqs) & set(data["dietaryRequirements"])) + tuple(set(fitness_goals) & set(data["fitnessGoals"]))
        if meal_plan_key in meal_plans:
            meal_plan = meal_plans[meal_plan_key]
            st.subheader("Your Personalized Meal Plan")
            for item in meal_plan:
                st.write(item)
        else:
            st.warning("No meal plan available for the selected requirements and goals.")
    else:
        st.warning("Please select at least one dietary requirement and one fitness goal.")

# Recommendations
st.sidebar.subheader("Recommendations")
if dietary_reqs:
    st.sidebar.write("Based on your dietary requirements, we recommend:")
    recommendations = generate_recommendations(dietary_reqs)
    for recommendation in recommendations:
        st.sidebar.write(f"- {recommendation}")

if fitness_goals:
    st.sidebar.write("Based on your fitness goals, we recommend:")
    recommendations = generate_recommendations(fitness_goals)
    for recommendation in recommendations:
        st.sidebar.write(f"- {recommendation}")

