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

# 코드 참고: https://pkgpl.org/2023/09/14/openai-tiktoken%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%86%A0%ED%81%B0-%EC%88%98-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0/


##### 예제 #####
text = "Hello, world!"

if count_token(text) > 8192:
    raise ValueError(
        "The number of tokens in the text is greater than 8192. The maximum number of tokens is 8192.")
