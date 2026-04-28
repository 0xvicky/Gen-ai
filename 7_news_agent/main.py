# pip install -qU langchain "langchain[google-genai]"
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain.tools import tool
from pydantic import SecretStr
from langchain_groq import ChatGroq
import requests
from langchain_core.messages import SystemMessage


load_dotenv()


@tool
def get_weather(city: str):
    """Get weather information for a given city."""
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"


llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)

agent = create_agent(
    llm,
    [get_weather],
    system_prompt=SystemMessage(
        content="Be concise. Use tools only when necessary. Avoid unnecessary explanations."
    ),
)

# while True:

#     USER_QUERY = input("> ")
#     result = agent.invoke({"messages": [{"role": "user", "content": USER_QUERY}]})
#     print(result["messages"][-1].content_blocks[0])
while True:

    USER_QUERY = input("> ")
    if USER_QUERY.lower() in ["exit", "quit"]:
        break
    for step in agent.stream(
        {"messages": [{"role": "user", "content": USER_QUERY}]},
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()
