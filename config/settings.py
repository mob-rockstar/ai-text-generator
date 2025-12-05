

import os
from dotenv import load_dotenv
from openai import OpenAI


# Load .env variables
load_dotenv()


API_KEY = os.getenv("OPENAI_API_KEY")


if not API_KEY:
    raise Exception("OPENAI_API_KEY is missing in .env file")


client = OpenAI(api_key=API_KEY)