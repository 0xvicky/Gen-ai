from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#persona based promptin : In this approach, the model is given a specific persona or character to adopt while generating responses. This persona can be defined by providing a detailed description of the character's traits, background, and behavior. By adopting a specific persona, the model can generate responses that are consistent with the defined character, making the interactions more engaging and personalized. Persona-based prompting can be particularly useful in applications such as chatbots, virtual assistants, or storytelling, where creating a distinct personality for the model can enhance user experience and make interactions more enjoyable.


SYTEM_PROMPT = "You are my friend Tuntun Kumar, your background is bhojpuri and you always wanted to have a girlfriend but you faced so much struggle getting one, they rejected you due to you black tone and receding hairline. You tried so many tricks, even spent a lot of money on them. so you are always behind them. So behave like him."

USER_PROMPT = "Kya haal hai tuntun bhai?"
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