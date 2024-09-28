import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("HUGGINGFACE_API_KEY")

# API endpoint
api_url = "https://api-inference.huggingface.co/models/gpt2"

# Headers
headers = {"Authorization": f"Bearer {api_key}"}

# Test input
payload = {
    "inputs": "Hello, how are you?",
    "parameters": {"max_length": 50}
}

# Make the request
response = requests.post(api_url, headers=headers, json=payload)

# Check the response
if response.status_code == 200:
    print("API is working!")
    print("Response:", response.json())
else:
    print("API request failed.")
    print("Status code:", response.status_code)
    print("Error message:", response.text)