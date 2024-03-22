from openai import OpenAI
from config import OpenAI_Settings

client = OpenAI(
    api_key=OpenAI_Settings.openai_api_key
)


def get_embedding(text: str):
    result = client.embeddings.create(
        model="text-embedding-3-large",
        # 토큰의 최대 개수인 8192 토큰을 넘으면 안됨. empyty string도 안됨. 배열은 2048차원이거나 적어야 함.
        input=text,
        encoding_format="float"  # float 또는 base64
    )
    return result

# 코드 참고: https://platform.openai.com/docs/api-reference/embeddings
