"""
codex_quickstart.py

This script provides a basic example of using OpenAI's Codex models via the OpenAI API.
Before running, install the OpenAI Python SDK:

    pip install openai

You also need an API key; set it in your environment as OPENAI_API_KEY.
"""

import openai
import os

def main():
    # Read API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable with your OpenAI API key.")
    openai.api_key = api_key

    # Example prompt for Codex: complete the function
    prompt = "def greet(name):\n    \"\"\"Return a personalized greeting.\"\"\"\n    "

    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=50,
        temperature=0,
        n=1,
        stop=None,
    )

    completion_text = response.choices[0].text.strip()
    print(prompt + completion_text)

if __name__ == "__main__":
    main()
