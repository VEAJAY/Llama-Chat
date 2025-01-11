from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following question:

Here is the conversation history: {context}

Qurstion: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to Llama Chat!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print(f"Llama: {result}")
        context += f"\nUser: {user_input}\nLlama: {result}"
        
        
if __name__ == "__main__":
    handle_conversation()
        
