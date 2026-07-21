#importing all necessary files
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
#loading environment variables from .env file
load_dotenv()
#storing the API key from environment variable
my_api_key = os.getenv("GROQ_API_KEY")
#checking if the API key is set, if not raise an error
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")
#creating a Groq client instance with the API key
client = Groq(api_key=my_api_key)
#selecting the model, role, and prompt for the chat completion
model = "llama-3.3-70b-versatile"
role = "user"
prompt = "i love you"
#System message to set the context for the chat completion
messages_system=[
    {
        "role": "system",
        "content": "You are an extremely strict manager"
    }
]
#messages list containing the role and prompt for the chat completion
messages = [
    {
        "role": role,
        "content": prompt
    }
]

#temperature parameter to control the randomness of the output
response = client.chat.completions.create(
    model=model,
    messages=messages_system + messages,
    temperature=2
)

#print(response)

print("############################################################")
print(response.choices[0].message.content)
