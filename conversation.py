import tkinter as tk

def handle_conversation(user_input, chat_display, context_var, chain):
    context = context_var.get()
    
    if user_input.lower() == "exit":
        return "exit"

    result = chain.invoke({"context": context, "question": user_input})
    
    chat_display.config(state=tk.NORMAL)
    
    chat_display.insert(tk.END, f"Llama: {result}\n", "llm")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)
    
    context_var.set(f"{context}\nUser: {user_input}\nLlama: {result}")
