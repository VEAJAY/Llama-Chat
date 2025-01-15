import tkinter as tk

def handle_conversation(user_input, chat_canvas, context_var, chain):
    context = context_var.get()

    if user_input.lower() == "exit":
        return "exit"

    result = chain.invoke({"context": context, "question": user_input})

    context_var.set(f"{context}\nUser: {user_input}\nYama: {result}")
    
    return result
