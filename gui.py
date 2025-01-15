import tkinter as tk
from conversation import handle_conversation

def setup_gui(chain):
    root = tk.Tk()
    root.title("Yama Chat")
    root.geometry("1400x1240")  

    chat_frame = tk.Frame(root, bg="white")
    chat_frame.pack(padx=10, pady=10, fill="both", expand=True)


    scrollbar = tk.Scrollbar(chat_frame, orient="vertical")
    scrollbar.pack(side=tk.RIGHT, fill="y")
    

    chat_canvas = tk.Canvas(chat_frame, bg="white", yscrollcommand=scrollbar.set)
    chat_canvas.pack(side=tk.LEFT, fill="both", expand=True)

 
    scrollbar.config(command=chat_canvas.yview)

 
    message_frame = tk.Frame(chat_canvas, bg="white")
    chat_canvas.create_window((0, 0), window=message_frame, anchor="nw")

 
    def update_scroll_region(event=None):
        chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
        
    message_frame.bind("<Configure>", update_scroll_region)

    user_input = tk.StringVar()
    input_box = tk.Entry(root, textvariable=user_input, width=50)
    input_box.pack(padx=10, pady=5)

    send_button = tk.Button(root, text="Send", command=lambda: send_message())
    send_button.pack(pady=5)

    context_var = tk.StringVar(value="")


    def create_bubble(message, is_user):
        bubble_color = "lightblue" if is_user else "lightgray"
        text_color = "purple" if is_user else "black"
        anchor = "e" if is_user else "w"

        bubble_frame = tk.Frame(message_frame, bg="white")
        bubble_frame.pack(anchor="w" if not is_user else "e", pady=10, padx=20, fill="x")


        bubble = tk.Label(
            bubble_frame,
            text=message,
            bg=bubble_color,
            fg=text_color,
            wraplength=1360,  
            justify="left",
            padx=15,
            pady=10,
            relief="solid",
            bd=1,
        )


        bubble.pack(side="right" if is_user else "left", padx=10)

        
        chat_canvas.update_idletasks()
        chat_canvas.yview_moveto(1)

 
    def send_message(event=None):
        user_message = user_input.get().strip()
        if user_message:
            create_bubble(f"You: {user_message}", is_user=True)

            
            llm_response = handle_conversation(user_message, chat_canvas, context_var, chain)
            if llm_response:
                create_bubble(f"Yama: {llm_response}", is_user=False)

           
            if llm_response.lower() in ["exit", "quit", "goodbye", "bye", "stop", "end"]:
                root.destroy()

        user_input.set("")

    input_box.bind("<Return>", send_message)
    input_box.bind("<KP_Enter>", send_message)

    return root
