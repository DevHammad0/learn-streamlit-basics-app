import streamlit as st
import pandas as pd #type: ignore
import numpy as np
from datetime import date

# Author and Date
st.markdown(
    f"<div style='text-align: right; font-size: 12px; color: gray;'>"
    f"Author: Muhammad Hammad | {date.today().strftime('%B %d, %Y')}"
    f"</div>", unsafe_allow_html=True
)



def main():
    st.title("🎈 Learning Streamlit - A Beginner's Guide")
    st.write("---")
    
    # Navigation
    section = st.sidebar.selectbox(
        "Choose a section",
        ["1. Introduction to Streamlit",
         "2. Basic Elements",
         "3. Data Display",
         "4. Interactive Widgets",
         "5. Layouts",
         "6. Simple Chatbot"]
    )
    
    if "1. Introduction to Streamlit" in section:
        introduction()
    elif "2. Basic Elements" in section:
        basic_elements()
    elif "3. Data Display" in section:
        data_display()
    elif "4. Interactive Widgets" in section:
        interactive_widgets()
    elif "5. Layouts" in section:
        layouts()
    elif "6. Simple Chatbot" in section:
        simple_chatbot()

def introduction():
    st.header("1. Introduction to Streamlit")
    
    st.markdown("""
    ### What is Streamlit?
    Streamlit is a Python library that makes it easy to create web apps for data science and machine learning.
    
    ### Key Features:
    - 🚀 Quick to build
    - 📊 Great for data applications
    - 🔄 Auto-rerun on save
    - 🎨 Beautiful default styling
    
    ### Basic Syntax:
    ```python
    import streamlit as st
    
    st.title("My First App")
    st.write("Hello, World!")
    ```
    """)
    
    # Live example
    st.subheader("Live Example:")
    st.write("This is a live example of Streamlit in action!")
    if st.button("Click me!"):
        st.balloons()

def basic_elements():
    st.header("2. Basic Elements")
    
    st.markdown("""
    ### Text Elements:
    Streamlit provides various ways to display text:
    """)
    
    # Examples of text elements
    st.title("This is a title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.text("This is plain text")
    st.markdown("**This is bold markdown text**")
    
    st.write("---")
    st.subheader("Code Example:")
    # Code example
    st.code('''
    st.title("Title")
    st.header("Header")
    st.subheader("Subheader")
    st.text("Text")
    st.markdown("**Markdown**")
    ''')

def data_display():
    st.header("3. Data Display")
    
    # Create sample data
    df = pd.DataFrame({
        'Name': ['John', 'Anna', 'Peter'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']
    })
    
    st.markdown("### Displaying Data:")
    
    # Display dataframe
    st.subheader("DataFrame Display")
    st.dataframe(df)
    
    st.write("---")
    # Show code example for DataFrame
    st.code('''
    # Create and display a DataFrame
    df = pd.DataFrame({
        'Name': ['John', 'Anna', 'Peter'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'London']
    })
    st.dataframe(df)
    ''')
    
    # Display chart
    st.subheader("Chart Example")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Line 1', 'Line 2', 'Line 3']
    )
    st.line_chart(chart_data)
    
    # Show code example for Chart
    st.write("---")
    st.code('''
    # Create and display a line chart
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Line 1', 'Line 2', 'Line 3']
    )
    st.line_chart(chart_data)
    ''')

def interactive_widgets():
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

    st.write("---")
    # Show code example
    st.subheader("Code Example:")
    st.code('''
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
    ''')

def layouts():
    st.header("5. Layouts")
    
    st.markdown("### Using Columns:")
    
    # Create three columns
    col1, col2, col3 = st.columns(3)
    
    col1.header("Column 1")
    col1.write("This is column 1")

    # Column 2
    col2.header("Column 2")
    col2.write("This is column 2")

    # Column 3
    col3.header("Column 3")
    col3.write("This is column 3")
    
    
    st.write("---")
    # Example with expander
    st.markdown("### Using Expander:")
    exp = st.expander("Click to expand")
    exp.write("This content is hidden by default!")
        
    st.write("---")
    st.subheader("Code Example:")
    st.code('''
    # Create three columns
    col1, col2, col3 = st.columns(3)
    
    col1.header("Column 1")
    col1.write("This is column 1")

    # Column 2
    col2.header("Column 2")
    col2.write("This is column 2")

    # Column 3
    col3.header("Column 3")
    col3.write("This is column 3")
    
    # Example with expander
    exp = st.expander("Click to expand")
    exp.write("This content is hidden by default!")
    ''')

def simple_chatbot():
    st.header("6. Simple Chatbot")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        chat_mes =st.chat_message(message["role"])
        chat_mes.markdown(message["content"])
    
    
    # Chat input
    if prompt := st.chat_input("What would you like to know about Streamlit?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        user = st.chat_message("user")
        user.markdown(prompt)
        
        # Simple response logic
        response = "I'm a simple chatbot. I can help you learn about Streamlit! Try asking about basic commands or features."
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        assistant = st.chat_message("assistant")
        assistant.markdown(response)
            
            
    st.write("---")
    st.subheader("Code Example:")
    st.code('''
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        chat_mes = st.chat_message(message["role"]):
        chat_mes.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know about Streamlit?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        user = st.chat_message("user")
        user.markdown(prompt)
        
        # Simple response logic
        response = "I'm a simple chatbot. I can help you learn about Streamlit!"
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        assistant = st.chat_message("assistant")
        assistant.markdown(response)
    ''')
    
    

if __name__ == "__main__":
    main()

