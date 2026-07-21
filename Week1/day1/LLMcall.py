# Import the required libraries
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Groq API key from the environment variables
my_api_key = os.getenv("GROQ_API_KEY")

# Raise an error if the API key is not found
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Create a Groq client using the API key
client = Groq(api_key=my_api_key)

# Specify the model to use for generating the response
model = "llama-3.3-70b-versatile"

# Define the role of the message sender
role = "user"

# User's prompt that will be sent to the model
prompt = "What should I say to my mother to make her feel appreciated?"

# Create the conversation as a list of messages
messages = [
    {
        "role": role,
        "content": prompt
    }
]

# Send the request to the Groq API and generate a chat completion
response = client.chat.completions.create(
    model=model,
    messages=messages
)

# Print the complete response object (includes metadata like usage, model, etc.)
print(response)

print("############################################################")

# Print only the generated text from the model's response
print(response.choices[0].message.content)
