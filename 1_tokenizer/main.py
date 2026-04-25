import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text= "Hey there"
tokens = enc.encode(text)
print(tokens)


decoded =  enc.decode(tokens)
print(decoded)

#vector embeddings : Vector embeddings are numerical representations of text that capture the semantic meaning of the text. They are used in various natural language processing tasks, such as text classification, sentiment analysis, and machine translation. Vector embeddings can be generated using various techniques, such as word2vec, GloVe, and BERT. These techniques use neural networks to learn the relationships between words and their contexts in a large corpus of text data. The resulting vector embeddings can then be used to perform various NLP tasks by comparing the similarity between different pieces of text based on their vector representations.

#position encoding : position encoding is a technique used in natural language processing to represent the position of words in a sentence. It is often used in transformer models, such as BERT and GPT, to help the model understand the order of words in a sentence. Position encoding typically involves adding a unique vector to each word in a sentence based on its position. This allows the model to capture the sequential nature of language and improve its ability to understand context and meaning.

#multihead attention: multihead attention is a mechanism used in transformer models to allow the model to focus on different parts of the input sequence when processing it. It consists of multiple attention heads that operate in parallel, each attending to different parts of the input. This allows the model to capture different aspects of the input and improve its ability to understand complex relationships between words and their contexts. Each attention head computes a weighted sum of the input tokens based on their relevance to the current token being processed, allowing the model to capture long-range dependencies and improve its performance on various NLP tasks.