import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")
if not token:
    raise ValueError("HF_TOKEN not found in .env")

client = InferenceClient(
    provider="hf-inference",
    api_key=token,
)

response = client.chat_completion(
    model="Qwen/Qwen2.5-7B-Instruct-1M",
    messages=[
        {"role": "user", "content": "Say hello in one cheerful sentence."}
    ],
    max_tokens=40,
)

print(response.choices[0].message.content)