from openai import OpenAI
from config import OpenAI_Settings
client= OpenAI(
    api_key = OpenAI_Settings.openai_api_key
)

completion =  client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "compose a poem that explains the concept of a recursion in programming."}
    ]
)

print(completion.choices[0].message)