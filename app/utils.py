from dotenv import load_dotenv
import openai 
import os

load_dotenv()

#Set your OpenAI key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_description(input):
    messages = [
        {"role": "system",
         "content": """As a product Description Generator, generate multi paragraph rich text product description with emojis from the information provided to you' \n""",}
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply