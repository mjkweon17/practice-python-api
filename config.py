from dotenv import load_dotenv
import os

dotenv_path = ".env"
load_dotenv(dotenv_path)

class OpenAI_Settings():
    openai_api_key = os.getenv("OPENAI_API_KEY")

class PINECONE_Settings():
    pinecone_api_key = os.getenv("PINECONE_API_KEY")