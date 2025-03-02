import os
from openai import OpenAI

client = OpenAI(
    api_key = "9cbfdace-a006-48bc-8846-*******",
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)

# Image input:
response = client.chat.completions.create(
    model="doubao-1-5-vision-pro-32k-250115",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
)

print(response.choices[0].message.content)