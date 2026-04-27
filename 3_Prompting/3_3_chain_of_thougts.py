from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# few-shot prompting : In this approach, the model is provided with a few examples of input-output pairs to learn from before generating a response. These examples serve as guidance for the model, helping it understand the desired format and content of the response. The model can then use this information to generate a more accurate and relevant response based on the input prompt. Few-shot prompting can be particularly useful when the task at hand is complex or requires specific knowledge that may not be easily inferred from the input prompt alone.
# The more example we provide the better the model will perform as it will have more context to learn from, but it also depends on the quality of examples provided. If the examples are not relevant or not well-structured, it may lead to poor performance of the model. Therefore, it is important to carefully select and curate the examples used for few-shot prompting to ensure that they are representative of the task and provide clear guidance for the model.

SYTEM_PROMPT = """
You're a physics expert, you only answer physics related questions.
If question is invalid return :
{{
isValid:False,
content:None
}}

If Valid then you're going to follow some rules in order to give the response, 

Rules-
1. Strict JSON format
Eg : {{
IsValid : Boolean,
step : START | EXECUTE | RESULT | None
content : String | None
}}
2. Execute each step one by one
3. Valid question goes through three steps - START, EXECUTE, RESULT
4. In START step, system analyse what user want to know, break the whole problem statement into executable step by step plan.

"""

# USER_PROMPT = "Can you give me an architecture of an hypothetical blockchain that uses the power of physics to operate??"
USER_PROMPT = "How thermodynamics affecting our daily lives?"
ASSISTANT_PROMPT = {
    "step": "START",
    "analysis": "User wants to know about how thermodynamics affecting daily lives.",
}

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
        {
            "role": "assistant",
            "content": json.dumps({"step": "START", "content": ASSISTANT_PROMPT}),
        },
    ],
)

print(response.choices[0].message.content)
