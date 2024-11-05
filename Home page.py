import streamlit as st

def main():
    st.title('Welcome to Your Streamlit Home Page')
    
    st.write('This is a simple example of a home page for a Streamlit web application.')
    
    st.image('https://your-image-url.com/your-image.png', caption='Your Image Caption', use_column_width=True)

if __name__ == '__main__':
    main()
