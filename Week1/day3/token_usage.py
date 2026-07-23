# Import all the required libraries
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


# Load environment variables from the .env file
load_dotenv()

# Retrieve the Groq API key from the environment variables
my_api_key = os.getenv("GROQ_API_KEY")

# Ensure that the API key is available before proceeding
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Create a Groq client using the API key
client = Groq(api_key=my_api_key)

# Select the model that will generate the responses
model = "llama-3.3-70b-versatile"

# Define the role of the sender in the conversation
role = "user"

# Sample prompts to test the model
prompt1 = "Hello"
prompt2 = "What is the time in new delhi?"
prompt3 = "what is the weather in new delhi write an essay of 1000 words on this topic."

# Define a system message to set the model's behavior
messages_system = [
    {
        "role": "system",
        "content": "You are an extreme climate enthusiast and a weather expert."
    }
]

# Iterate through each prompt and send it to the model
for prompt in [prompt1, prompt2, prompt3]:

    # Create the user message for the current prompt
    messages = [
        {
            "role": role,
            "content": prompt
        }
    ]

    # Generate a chat completion from the model
    response = client.chat.completions.create(
        model=model,
        messages=messages_system + messages,
        max_tokens=10000,
        temperature=1
    )

    # Extract the reason why the generation stopped
    finish_reason = response.choices[0].finish_reason

    # Retrieve token usage statistics
    usage = response.usage

    # Display token usage and completion details for the current prompt
    print(
        f"Prompt: {prompt} --> "
        f"Tokens used: {usage.total_tokens}, "
        f"Prompt tokens: {usage.prompt_tokens}, "
        f"Completion tokens: {usage.completion_tokens}, "
        f"Finish reason: {finish_reason}"
    )

# Print a separator
print("############################################################")

# Print the response generated for the last prompt
print(response.choices[0].message.content)
