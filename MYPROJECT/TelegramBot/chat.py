import os
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext, ttk
from dotenv import load_dotenv

os.system("cls")
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
)


history = []


def start_chat():
    global chat_session
    chat_session = model.start_chat(history=history)


def send_message():
    user_input = user_input_field.get()
    if user_input.strip() == "":
        return  

    
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_input}\n")
    chat_area.config(state=tk.DISABLED)

    
    response = chat_session.send_message(user_input)
    model_response = response.text

    
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"Bot: {model_response}\n\n")
    chat_area.config(state=tk.DISABLED)

    
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

    
    user_input_field.delete(0, tk.END)


root = tk.Tk()
root.title("Chat with AI Bot")
root.geometry("500x700")
root.configure(bg="#f0f0f0")


frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


chat_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", fg="#333333", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


user_input_field = ttk.Entry(root, width=80, font=("Arial", 12))
user_input_field.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)


send_button = ttk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)


start_chat()

root.mainloop()