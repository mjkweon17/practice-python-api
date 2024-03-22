import tiktoken

# enc = tiktoken.encoding_for_model("gpt-4")    # To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.get_encoding("cl100k_base")

assert enc.decode(enc.encode("hello world")) == "hello world"


def count_token(text: str):
    result = enc.encode(text)
    return len(result)


def get_tokens(text: str):
    result = enc.encode(text)
    return result


def get_tokenized_text(text: str):
    result = enc.encode(text)
    return enc.decode(result)
