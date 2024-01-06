from openai import OpenAI
from dotenv import load_dotenv
import os

# Loading API Key from .env file (require python-dotenv pip package)
load_dotenv()
mykey = os.getenv("OPENAI_API_KEY")

# Use API Key to construct OpenAI client instance
client = OpenAI(api_key=mykey)

completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)