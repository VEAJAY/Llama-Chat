import tkinter as tk
from conversation import handle_conversation

def setup_gui(chain):
    root = tk.Tk()
    root.title("Llama Chat")
    root.geometry("1400x1240")

    chat_display = tk.Text(
        root, state=tk.DISABLED, wrap=tk.WORD, bg="white", fg="black", height=70, width=200
    )
    chat_display.pack(padx=10, pady=10)

    chat_display.tag_configure("user", justify="right", foreground="purple")
    chat_display.tag_configure("llm", justify="left", foreground="black")

    user_input = tk.StringVar()
    input_box = tk.Entry(root, textvariable=user_input, width=50)
    input_box.pack(padx=10, pady=5)

    context_var = tk.StringVar(value="")

    def display_message(message, tag):
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, message + "\n", tag)
        chat_display.config(state=tk.DISABLED)
        chat_display.see(tk.END) 

    def send_message(event=None):
        user_message = user_input.get().strip()
        if user_message:
            display_message(f"You: {user_message}", "user")
            
            llm_response = handle_conversation(user_message, chat_display, context_var, chain)
            
            if llm_response:
                display_message(f"Llama: {llm_response}", "llm")
            
            if llm_response in ["exit", "quit", "goodbye", "bye", "stop", "end"]:
                root.destroy()

        user_input.set("")

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(pady=5)

    input_box.bind("<Return>", send_message)
    input_box.bind("<KP_Enter>", send_message)

    return root
