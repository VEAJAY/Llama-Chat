import tkinter as tk
from conversation import handle_conversation

def setup_gui(chain):
    root = tk.Tk()
    root.title("Llama Chat")

    chat_display = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD, bg="white", fg="black", height=20, width=50)
    chat_display.pack(padx=10, pady=10)

    user_input = tk.StringVar()
    input_box = tk.Entry(root, textvariable=user_input, width=50)
    input_box.pack(padx=10, pady=5)

    context_var = tk.StringVar(value="")

    def send_message():
        user_message = user_input.get().strip()
        if user_message: 
            if handle_conversation(user_message, chat_display, context_var, chain) == "exit":
                root.destroy()
        user_input.set("") 

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(pady=5)

    return root
