import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Initialize the chat model
model = ChatMistralAI(model="mistral-large-latest")

# Set up session state for the chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful AI assistant.")]
if 'conversation' not in st.session_state:
    st.session_state.conversation = []  # Store conversation for display

# Streamlit app UI
st.title("AI Chat with Mistral Model")

# Display previous conversation
conversation_display = "\n".join(st.session_state.conversation)
st.text_area("Chat History", value=conversation_display, height=400, disabled=True)

# Use a form to handle user input submission
with st.form(key="user_input_form", clear_on_submit=True):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button("Send")

# Process user input and AI response when the user hits "Send"
if submit_button and user_input:
    # Add user's message to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.conversation.append(f"You: {user_input}")
    
    # Get AI response based on the current chat history
    result = model.invoke(st.session_state.chat_history)
    response = result.content
    
    # Add AI's message to chat history and update conversation display
    st.session_state.chat_history.append(AIMessage(content=response))
    st.session_state.conversation.append(f"AI: {response}")

# Button to reset the conversation
if st.button("Reset Chat"):
    st.session_state.chat_history = [SystemMessage(content="You are a helpful AI assistant.")]
    st.session_state.conversation = []
