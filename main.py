import os

from dotenv import load_dotenv
from openai import OpenAI

# load environment variables
load_dotenv()

# create openai client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
