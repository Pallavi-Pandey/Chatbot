# AI Chat with Mistral Model

This is a simple web application built using [Streamlit](https://streamlit.io/) and the [MistralAI model](https://huggingface.co/mistralai), designed to allow users to chat with an AI assistant. The app keeps track of the conversation history and enables users to reset the chat when needed.

You can try the deployed app here: [AI Chat with Mistral Model](https://mistralai.streamlit.app/)

## Features

- **Real-time chat**: Interact with the Mistral model in real time.
- **Conversation history**: See the previous messages exchanged between the user and AI.
- **Reset chat**: Start a new conversation at any time by resetting the chat history.

## How to Run the App Locally

### Prerequisites

- Python 3.8 or higher
- [Streamlit](https://docs.streamlit.io/) for building the web app
- [LangChain](https://python.langchain.com/) for handling chat with the Mistral model
- A `.env` file containing your environment variables (for API keys and other secrets)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Pallavi-Pandey/Chatbot.git
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project and add the necessary environment variables.

### Running the App

To start the app, run:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can interact with the app through your browser.

# Project Structure
- app.py: The main Streamlit application.
- requirements.txt: Lists the dependencies required to run the app.
- .env: (Not included in the repository) Stores sensitive environment variables.
# Dependencies
- Streamlit for building the UI.
- LangChain for handling interaction with the Mistral model.
- dotenv for loading environment variables.
- MistralAI model via LangChain.
# Deployed Application
The application is deployed and can be accessed at the following link:

[AI Chat with Mistral Model](https://mistralai.streamlit.app/)

