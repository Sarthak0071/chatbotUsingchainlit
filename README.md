# LangChain Community Chat Bot

This repository contains code for a chat bot implemented using LangChain framework. The bot leverages Google's Generative AI capabilities to provide text generation functionality.
Overview

This chat bot application utilizes LangChain, ChainLit, and Google Generative AI to create a conversational interface. Below are the main functionalities implemented:

    Greeting with Gemma's Image: Upon initiation, the bot sends a greeting message along with an image of Gemma. This creates a welcoming atmosphere for users interacting with the bot.

    Text Generation: The bot is capable of generating text responses to user queries using Google's Generative AI. It utilizes LangChain's framework to manage the conversation flow and ChainLit library for message handling.

## Prerequisites

Before running the code, make sure you have the following installed:

    Python 3.x
    LangChain framework
    ChainLit library
    Google Generative AI API key (stored in GOOGLE_API_KEY environment variable)
    Gemma image (gemma.jpeg) in the project directory

### Installation



Install dependencies:

bash

pip install langchain chainlit google-generativeai

Usage

Run the chat bot script:

bash

python chat_bot.py

# Code Explanation:

The code provided in the chat_bot.py file is a Python script that implements the chat bot functionality using LangChain framework and Google's Generative AI capabilities.

    Importing Necessary Modules:

    The script begins by importing required modules from LangChain, ChainLit, and Google Generative AI. These include modules for prompts, schema, runnable configurations, and callback handlers.

    Configuring Google Generative AI:

    The script configures the Google Generative AI with the API key obtained from the environment variable GOOGLE_API_KEY.

    Defining Chat Start Function:

    The on_chat_start() function is a callback function that is executed when a chat session starts. It sends a greeting message along with Gemma's image using ChainLit's cl.Message() method. It also initializes the text generation model (GoogleGenerativeAI) and sets up a prompt template for the conversation.

    Handling Incoming Messages:

    The on_message() function is another callback function that is executed whenever a new message is received. Inside this function, the text generation model is invoked with the user's message as input. The generated text chunks are then streamed back to the user as responses.

## Key Components:

    LangChain Community (llms): This module provides access to LangChain's large language model services.
    ChatPromptTemplate: Represents a template for generating chat prompts.
    StrOutputParser: Parses the text output from the text generation model.
    Runnable: Represents a chain of processes that can be executed in LangChain.
    RunnableConfig: Configuration for executing a Runnable object.
    ChainLit (cl): Library for building conversational applications.
    GoogleGenerativeAI: Interface for accessing Google's Generative AI models.

## Main Flow:

    Initialization: The script initializes necessary modules and configurations.
    Chat Start: Upon initiation of a chat session, Gemma's image is sent along with a greeting message. The text generation model and prompt template are set up.
    Message Handling: When a new message is received, it is passed to the text generation model for processing. The generated text chunks are then streamed back to the user as responses.


## Video Demo
You can watch a demo of the chat bot in action [here](https://github.com/Sarthak0071/chatbotUsingchainlit/blob/main/Chatbot%20%E2%80%94%20Mozilla%20Firefox%202024-03-24%2023-24-02.mp4).

This code structure allows for easy extension and customization of the chat bot's functionalities within the LangChain framework.