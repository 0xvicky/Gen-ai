from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)



response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role":"system",
            "content":"You are an expert of physics. From now on answer the physics related questions only.If query still otherwise just respond => 'Sorry, I can't assist with that!'"
        },
        {
            "role": "user",
            "content": "Can you give me an architecture of an hypothetical blockchain that uses the power of physics to operate??"
        }
    ]
)

print(response.choices[0].message.content)