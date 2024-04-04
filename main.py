from count_token import count_token
from get_vector import get_embedding

text = ""

if count_token(text) > 8192:
    raise ValueError("The number of tokens in the text is greater than 8192. The maximum number of tokens is 8192.")

text_vector = get_embedding(text)