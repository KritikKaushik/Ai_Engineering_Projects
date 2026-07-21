# Import all the required libraries
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Groq API key from the environment variables
my_api_key = os.getenv("GROQ_API_KEY")

# Ensure that the API key exists before making API requests
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Create a Groq client using the API key
client = Groq(api_key=my_api_key)

# Select the model and define the role for the conversation
model = "llama-3.3-70b-versatile"
role = "user"

# Import BaseModel to define the expected structured output
from pydantic import BaseModel

# Define the schema for the structured JSON response
class CustomerTicket(BaseModel):
    name: str
    problem: str
    course_resolution: bool
    chat_support: bool
    phone_number: int

# Generate the JSON schema from the Pydantic model
schema = CustomerTicket.model_json_schema()

# Request the model to return its response as a JSON object
response_format = {
    "type": "json_object",
}

# System prompt instructing the model to follow the generated schema
prompt_system = f"""
Return the output as a valid JSON object matching the following schema:

{schema}
"""

# User input from which the required information will be extracted
text = (
    "Hello my name is kritik and i have problem in dsa "
    "i want course resolution along with chat support "
    "my number is 898989898989"
)

# Define the system message
messages_system = [
    {
        "role": "system",
        "content": prompt_system
    }
]

# Define the user message
messages = [
    {
        "role": role,
        "content": text
    }
]

# Send the request to the Groq API with structured JSON output enabled
response = client.chat.completions.create(
    model=model,
    messages=messages_system + messages,
    response_format=response_format,
    temperature=0
)

# Print a separator
print("############################################################")

# Print only the generated JSON response
print(response.choices[0].message.content)
