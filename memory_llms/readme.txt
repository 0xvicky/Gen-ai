memory in ai agents : Memory in AI agents refers to the ability of the system to store, recall, and utilize information from past interactions to inform future actions. It allows agents to maintain context over long conversations, learn from previous mistakes, and personalize responses based on user history. In frameworks like LangGraph, memory is often implemented through "checkpointers," which save the state of the graph at each step, enabling the agent to resume progress or "rewind" to previous states.

Types of memories:
1. Short-term memory: This type of memory holds information temporarily during an ongoing interaction. It allows the agent to maintain context and understand the flow of conversation.
2.  Long-term memory: This type of memory stores information over extended periods, allowing the agent to learn from past interactions and improve its performance over time.
Factual, episodic and semantic memory:
    - Factual Memory: Stores specific, verifiable pieces of information (e.g., a user's birthdate or a specific project deadline).
    - Episodic Memory: Relates to the sequence of events and experiences in past interactions, helping the agent remember the "story" of the conversation.
    - Semantic Memory: Involves the structured understanding of concepts, rules, and relationships learned over time.
    