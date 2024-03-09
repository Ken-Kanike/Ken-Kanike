import os
from groq import Groq

user_input = input("Enter your question : ")
if( user_input == ""):
    user_input = "hii"


# Replace "YOUR_ACTUAL_API_KEY" with your Groq API key
api_key = "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"  #harsh key
api_key2 = "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"  #mye key


client = Groq(
    api_key=api_key2,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":user_input,
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)