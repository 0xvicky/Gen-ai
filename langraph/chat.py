from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

llm = init_chat_model(model="qwen/qwen3-32b", model_provider="groq")


def chatbot(state: State):
    # llm = ChatGroq(
    #     model="qwen/qwen3-32b",
    #     temperature=0,
    #     max_tokens=None,
    #     reasoning_format="parsed",
    #     timeout=None,
    #     max_retries=2,
    #     # other params...
    # )

    res = llm.invoke(state.get("messages"))
    return {"messages": [res]}


def sampleNode(state: State):
    return {"messages": ["this is message from sampleNode"]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sampleNode", sampleNode)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sampleNode")
graph_builder.add_edge("sampleNode", END)

graph = graph_builder.compile()


updated_state = graph.invoke(State({"messages": [""""""]}))
print(updated_state)
