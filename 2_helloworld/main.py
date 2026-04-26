from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
print("KEY:", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "What's the day today ?"

response = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages=[
        {"role":"user", "content":prompt}
    ]
)

print(response.choices[0].message.content)





