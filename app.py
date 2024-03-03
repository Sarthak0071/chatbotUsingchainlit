from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl




import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@cl.on_chat_start
async def on_chat_start():
    
    # Sending an image with the local file path
    elements = [
    cl.Image(name="image1", display="inline", path="gemma.jpeg")
    ]
    await cl.Message(content="Hello Gemma Here. How can I help you ?", elements=elements).send()
    model = GoogleGenerativeAI(model="gemini-pro")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a text generation app so do everything as command.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()