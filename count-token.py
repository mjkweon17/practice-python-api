import tiktoken
# enc = tiktoken.encoding_for_model("gpt-4")    # To get the tokeniser corresponding to a specific model in the OpenAI API:
enc = tiktoken.get_encoding("cl100k_base")
assert enc.decode(enc.encode("hello world")) == "hello world"

text = "Hello, world!"

result = enc.encode(text)
print(result)   # 이렇게 하면 코튼 번호로 결과가 출력됨
print(len(result)) # 이렇게 하면 토큰의 개수가 출력됨

decoded_text = enc.decode(result)
print(decoded_text)