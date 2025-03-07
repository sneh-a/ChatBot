import tkinter as tk
from tkinter import scrolledtext

# Basic chatbot responses
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
    "your name": "I'm a simple chatbot!",
    "default": "I'm not sure how to respond to that. Try asking something else."
}

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Function to send message
def send_message():
    user_text = entry_box.get()
    if user_text.strip():
        chat_window.insert(tk.END, "🧑‍💻 You: " + user_text + "\n", "user")
        bot_response = get_response(user_text)
        chat_window.insert(tk.END, "🤖 Bot: " + bot_response + "\n", "bot")
        entry_box.delete(0, tk.END)  # Clear input field
        chat_window.yview(tk.END)  # Scroll down to latest message

# GUI Setup
root = tk.Tk()
root.title("Chatbot 🤖")
root.geometry("450x550")
root.configure(bg="#1E1E1E")

# Chat history display
chat_window = scrolledtext.ScrolledText(root, width=55, height=20, wrap=tk.WORD, font=("Arial", 12), bg="#282C34", fg="white", bd=0)
chat_window.grid(row=0, padx=10, pady=10, columnspan=2)
chat_window.tag_configure("user", foreground="#61AFEF", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="#98C379", font=("Arial", 12, "bold"))

# User input field
entry_box = tk.Entry(root, width=40, font=("Arial", 14), bg="#3E4451", fg="white", bd=2, relief=tk.FLAT)
entry_box.grid(row=1, padx=10, pady=10, sticky="w")

# Send button with styling
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 14, "bold"), bg="#61AFEF", fg="white", padx=15, pady=5, relief=tk.FLAT)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

root.mainloop()
