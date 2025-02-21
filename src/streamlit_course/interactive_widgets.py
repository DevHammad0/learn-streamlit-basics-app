import streamlit as st


st.header("4. Interactive Widgets")

st.markdown("### Basic Input Widgets:")

# Text input
name = st.text_input("Enter your name")

# Slider
age = st.slider("Select your age", 0, 100, 25)

# Checkbox
happy = st.checkbox("Are you happy?")

# Display results
if name:
    st.write(f"Hello, {name}!")
st.write(f"Selected age: {age}")
if happy:
    st.write("😊 Glad you're happy!")