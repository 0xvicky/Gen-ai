from transformers import pipeline

pipe = pipeline("text-generation", model="google/gemma-3-4b-it")messages = [
    {"role": "user", "content": "Who are you?"},
]
output = pipe(messages, max_new_tokens=256)
print(output[0]["generated_text"][-1]["content"])
