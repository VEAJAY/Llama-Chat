from dotenv import load_dotenv
import openai
import time
import os

load_dotenv("./key.env")
openai.api_key = os.getenv("OPENAI_API_LLAMA_KEY")

def chat(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-16k",
            prompt=prompt,
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError: 
        print("Rate limit exceeded, now waiting...")
        time.sleep(2)  
        return chat(prompt)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "goodbye", "bye", "see ya"]:
            break
        response = chat(user_input)
        print(f"Llama: {response}")

