import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN not found. Put it in a .env file.")

client = InferenceClient(token=token)

prompt = "Write a cheerful two-sentence welcome message for someone restarting coding."

response = client.text_generation(
    prompt,
    model="gpt2",
    max_new_tokens=60,
)

print("Model response:")
print(response)