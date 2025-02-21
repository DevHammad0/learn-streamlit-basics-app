
import streamlit as st
import time

# st.header() creates a header text element in the Streamlit app
st.header("6. Simple Chatbot")

# st.session_state is Streamlit's way to persist data between reruns
# Here we initialize an empty list to store chat messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Iterate through existing messages in the session state to display chat history
for message in st.session_state.messages:
    # st.chat_message() creates a chat message container with the specified role (user/assistant)
    # Returns a container that can hold multiple elements
    chat_msg = st.chat_message(message["role"])
    # st.markdown() renders markdown text within the chat message container
    chat_msg.markdown(message["content"]) 


# st.chat_input() creates a chat input box at the bottom of the app
# The walrus operator := assigns the input value to 'prompt' and evaluates to True if there's input
if prompt := st.chat_input("What would you like to know about Streamlit?"):
    # Add new user message to the session state message history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Create and display the user's message in the chat interface
    user_message = st.chat_message("user")
    user_message.markdown(prompt)
    
    # Simple hardcoded response for demonstration
    response = "I'm a simple chatbot. I can help you learn about Streamlit! Try asking about basic commands or features."
    
    # Add bot's response to the session state message history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Create and display the assistant's response in the chat interface
    assistant_message = st.chat_message("assistant")
    assistant_message.markdown(response)