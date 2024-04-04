from pinecone import Pinecone, ServerlessSpec

from config import PINECONE_Settings

api_key = PINECONE_Settings.pinecone_api_key
pc = Pinecone(api_key=api_key)

pc.create_index(
    name="quickstart",
    dimension=3072,
    metric=""
)