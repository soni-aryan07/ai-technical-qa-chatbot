import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

if openai_api_key:
    print(f"OpenAI API key found and begins with {openai_api_key[:5]}")
else:
    print('No OpenAI API key found!')

if anthropic_api_key:
    print(f"Anthropic API key found and begins with {anthropic_api_key[:5]}")
else:
    print('No Anthropic API key found!')

if google_api_key:
    print(f"Google API key found and begins with {google_api_key[:5]}")
else:
    print('No Google API key found!')

openai = OpenAI()

anthropic_url = "https://api.anthropic.com/v1"
google_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

anthropic = OpenAI(base_url=anthropic_url, api_key=anthropic_api_key)
google = OpenAI(base_url=google_url, api_key=google_api_key)
