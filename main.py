from chat_chain import create_chain
from gui import setup_gui

if __name__ == "__main__":
    chain = create_chain()

    root = setup_gui(chain)

    root.mainloop()
