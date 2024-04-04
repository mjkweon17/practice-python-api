# practice-openai
Repository for practicing and testing OpenAI models

- 24년 3월 22일


### 토큰 개수 세는 법
- 전체적인 설명: https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken
- GitHub: https://github.com/openai/tiktoken/blob/main/README.md
- tiktoken
    - encodings: 텍스트가 어떻게 토큰으로 변환될지 적는 곳
        - cl100k_base: gpt나 embedding models 쓰면 이걸로
    - encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')를 써서 encoding을 구할 수도 있음


### Pinecone
- 참고: https://app.pinecone.io/organizations/-Nta4G_7CAhIPq4kU9hJ/projects/serverless:75dvkv3/indexes
- 참고: https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/pinecone/Semantic_Search.ipynb
- 참고: https://www.ncloud-forums.com/topic/124/?_fromLogin=1
- install
    ```bash
    pip install pinecone-client
    ```
- initialize
    ```python
    from pinecone import Pinecone, ServerlessSpec

    pc = Pinecone(api_key="feb8b2c8-b248-4d47-974b-8ef54c8af346")
    ```