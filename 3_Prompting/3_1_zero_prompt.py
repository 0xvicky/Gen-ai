from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#direct prompting or zero shot prompting : so the model is not given any examples to learn from, it is expected to generate a response based solely on the input prompt and its pre-existing knowledge. The model is not provided with any specific guidance or examples to follow, and it must rely on its understanding of language and the context of the prompt to generate a response.
SYTEM_PROMPT = "You are an expert of physics. From now on answer the physics related questions only.If query still otherwise just respond => 'Sorry, I can't assist with that!'"

USER_PROMPT = "Can you give me an architecture of an hypothetical blockchain that uses the power of physics to operate??"
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role":"system",
            "content":SYTEM_PROMPT
        },
        {
            "role": "user",
            "content": USER_PROMPT
        }
    ]
)

print(response.choices[0].message.content)