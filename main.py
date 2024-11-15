from langchain_openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

prompt = "Translate the following English text to French: 'Hello, how are you?'"
response = llm.invoke(prompt)
print(response)
