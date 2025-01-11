from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def create_chain():
    template = """
    Answer the following question:

    Here is the conversation history: {context}

    Question: {question}

    Answer:
    """
    model = OllamaLLM(model="llama3")
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model
