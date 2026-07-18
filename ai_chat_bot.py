import tkinter as tk# for creating frontend
from tkinter import scrolledtext#component mainly used for scorlling
import ollama#fetching answer

def send_message():# it execute user input
    user_msg = entry.get().strip()#strip is used for removing spce

    if not user_msg:
        return

    # Display user message in purple
    chat_area.insert(tk.END, f"You: {user_msg}\n", "user")
    chat_area.see(tk.END)#tk.End next next one by one finally it
    #shows answer

    entry.delete(0, tk.END)

    try:#if i didn't get any error try block will be execute
        response = ollama.chat(
            model="phi3:mini",
            messages=[
                {"role": "user", "content": user_msg}
            ]
        )

        bot_msg = response["message"]["content"]#ollama answer

        # Display bot message in green
        chat_area.insert(tk.END, f"Bot: {bot_msg}\n\n", "bot")
        chat_area.see(tk.END)#answer showing on chat area bot

    except Exception as e:#if i get any error means
        #except block will be executed
        chat_area.insert(tk.END, f"Error: {e}\n\n", "error")
        chat_area.see(tk.END)

# Main Window
root = tk.Tk()#tkinter initialize
root.title("AI Chatbot")#title set
root.geometry("1350x550")#for setting width and hight

# Chat Area -for showing answer from ollama
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11)
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# Configure Colors
chat_area.tag_config("user", foreground="black", font=("Arial", 11, "bold"))
chat_area.tag_config("bot", foreground="green")    #font family,font size,style
chat_area.tag_config("error", foreground="red")

# Entry Box
entry = tk.Entry(
    root,
    font=("Arial", 12),
    fg="purple"
)#it is used for typing question
entry.pack(padx=10, pady=5, fill=tk.X)

# Send Button
send_btn = tk.Button(
    root,
    text="Send",
    command=send_message,
    font=("Arial", 11, "bold")
)# if it activated means it will help to show output for user
send_btn.pack(pady=5)#plotting component base on padding

# Press Enter to Send
entry.bind("<Return>", lambda event: send_message())#entry to send answeer in entry book
root.mainloop()# for visulizing forntend frame
