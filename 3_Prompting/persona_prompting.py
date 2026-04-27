from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# persona based promptin : In this approach, the model is given a specific persona or character to adopt while generating responses. This persona can be defined by providing a detailed description of the character's traits, background, and behavior. By adopting a specific persona, the model can generate responses that are consistent with the defined character, making the interactions more engaging and personalized. Persona-based prompting can be particularly useful in applications such as chatbots, virtual assistants, or storytelling, where creating a distinct personality for the model can enhance user experience and make interactions more enjoyable.


SYTEM_PROMPT = "You are chemistry expert!"

USER_PROMPT = "Calcium Carbonate"
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
)

print(json.dumps(response.choices[0].message))
