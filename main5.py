import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct:cerebras",
    messages=[
        {"role": "user", "content": "Say hello in one cheerful sentence."}
    ],
    max_tokens=40,
)

print(completion.choices[0].message.content)