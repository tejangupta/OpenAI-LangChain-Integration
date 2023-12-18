# OpenAI-LangChain Integration

## Overview

This project integrates OpenAI's powerful GPT models with the LangChain library to provide enhanced natural language processing capabilities. It is designed to enable easy querying of OpenAI's models and handle interactions with LangChain components.

## Features

- **OpenAI Connector**: Interface with OpenAI's GPT models.
- **Model Utilities**: Preprocess and postprocess text data for model interactions.
- **LangChain Helpers**: Facilitate interactions with LangChain's language models.
- **Custom Logger**: Comprehensive logging mechanism for debugging and monitoring.
- **Robust Error Handling**: Catch and log errors effectively.
- **Unit Testing**: Ensure code reliability and functionality.

## Installation

To set up this project:
1. Clone the repository: 
```bash
git clone https://github.com/tejangupta/OpenAI-LangChain-Integration.git 
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt 
```

## Prerequisites
1. **OpenAI API Key**: Ensure you have your OpenAI API key set as an environment variable. This is crucial for the OpenAI Connector to work.
```bash
export OPENAI_API_KEY='your-api-key'
```

## Running the Application
1. **Start a Python Shell**: Open a Python interactive shell in your project's root directory.
```bash
python 
```
2. **Import Classes**: In the Python shell, import the necessary classes from your project.
```bash
from src.openai_integration.openai_connector import OpenAIConnector
from src.langchain_util.langchain_helpers import LangChainHelpers 
```
3. **Initialize Connectors**: Create instances of `OpenAIConnector` and `LangChainHelpers`.
```bash
openai_connector = OpenAIConnector()
langchain_helpers = LangChainHelpers() 
```
4. **Query OpenAI Model**: Use the OpenAI connector to send a query to the OpenAI model.
```bash
response = openai_connector.query_model("Hello, how are you?")
print(response) 
```
5. **Interact with LangChain**: Similarly, you can use LangChainHelpers to interact with LangChain's features.
```bash
# Example: using LangChainHelpers (adjust according to your methods)
llm_response = langchain_helpers.query_llm("Some text")
chat_model_response = langchain_helpers.query_chat_model(["Message1", "Message2"])
print(llm_response, chat_model_response) 
```
## Running Tests
Run unit tests to verify functionality:
```bash
python -m unittest discover -s tests
```