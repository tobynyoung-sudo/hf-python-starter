import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")
print("Token loaded:", bool(token))

client = InferenceClient(
    provider="hf-inference",
    api_key=token,
)

response = client.chat_completion(
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ],
    max_tokens=30,
)

print(response.choices[0].message.content)