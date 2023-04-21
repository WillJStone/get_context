"""
This Python module contains a single function count_tokens(text: str) -> int, which uses the tiktoken tokenizer to encode a given input text with the "gpt-4" model and return the number of resulting tokens.
"""
import tiktoken


def count_tokens(text: str) -> int:
    encoder = tiktoken.encoding_for_model("gpt-4")
    return len(encoder.encode(text))

