import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Define class labels
class_labels = {0: 'APPLES', 1: 'BANANA', 2: 'ORANGE', 3: 'PINEAPPLE', 4: 'WATERMELON'}

# Nutritional data for fruits
fruit_nutritional_data = {
    'APPLES': {"calories": 95, "protein": 0.5, "carbs": 25, "fats": 0.3},
    'BANANA': {"calories": 105, "protein": 1.3, "carbs": 27, "fats": 0.4},
    'ORANGE': {"calories": 62, "protein": 1.2, "carbs": 15, "fats": 0.2},
    'PINEAPPLE': {"calories": 50, "protein": 0.5, "carbs": 13, "fats": 0.1},
    'WATERMELON': {"calories": 46, "protein": 0.9, "carbs": 11, "fats": 0.2}
}

# Function to preprocess the image
def preprocess_image(image):
    # Resize the image to the required input shape of the model
    image = image.resize((32, 32))
    # Convert the image to a numpy array
    img_array = np.array(image)
    # Normalize the pixel values
    img_array = img_array / 255.0
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Streamlit app
def main():
    st.title("Nutrion Analyser")
    st.text("Upload an image of a fruit to classify it.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True, width=200)  # Adjust width as needed

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Perform prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction)

        # Display the prediction result
        predicted_fruit = class_labels[predicted_class]
        st.write(f"Prediction: {predicted_fruit}")

        # Display the nutritional data for the predicted fruit
        st.subheader("Nutritional Data:")
        st.write(f"Calories: {fruit_nutritional_data[predicted_fruit]['calories']} kcal")
        st.write(f"Protein: {fruit_nutritional_data[predicted_fruit]['protein']} g")
        st.write(f"Carbohydrates: {fruit_nutritional_data[predicted_fruit]['carbs']} g")
        st.write(f"Fats: {fruit_nutritional_data[predicted_fruit]['fats']} g")

if __name__ == '__main__':
    main()
