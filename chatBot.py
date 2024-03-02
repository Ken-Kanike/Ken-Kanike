import os
from groq import Groq

# Replace "YOUR_ACTUAL_API_KEY" with your Groq API key
api_key = "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"

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is php",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)