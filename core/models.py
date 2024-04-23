from openai import OpenAI
import os

class GPT():

    def __init__(self, version='gpt-3.5-turbo'):
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))