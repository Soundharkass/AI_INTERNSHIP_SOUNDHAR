import tkinter as tk#for creating frontend
from tkinter import scrolledtext# for scorlling our answer
from google import genai #building model

client = genai.Client(
    api_key="AQ.Ab8RN6JhE_B7731mKjNCw2QBV1oKVBY3bFmIvZhKR8dAQYgsgQ"
)#api key -paid version key from gemini api

MODEL_NAME = "gemini-3.1-flash-lite" # gemini's model and its vesrion 

def ask_ai():
    question = entry.get()# it stores user question

    if question.strip() == "":#if user didn't type any question
        return

    chat_box.insert(tk.END, "You : " + question + "\n\n")
# it helps for storing question inside the chatbox
    try:# if no problem in my code means it will  automatically execute
        response = client.models.generate_content(
            model=MODEL_NAME,#model name=gemini-3.1-flash-lite
            contents=question# userprompt - developer prompt
        )#building my model

        answer = response.text# it will store answers

    except Exception as e:#e - will be store which kind of error pgm gets
        # except will execute when chance for error in our pgm
        answer = f"Error:\n{e}"#answer variable stores error

    chat_box.insert(tk.END, "Gemini : " + answer + "\n")
    #chatbox will show error 
    chat_box.insert(tk.END, "-" * 60 + "\n\n")#for printing 60 ---

    entry.delete(0, tk.END)# for deleting question from entry box

root = tk.Tk()# for initializing tikinter module
root.title("Gemini AI Chatbot")# for setting title
root.geometry("1300x566")# frame high and width
root.configure(bg="white")#frame background =white

title = tk.Label(
    root,
    text="Gemini AI Chatbot",
    font=("Georgia", 18, "bold"),
    bg="gold",
    fg="black"
)# for heading Gemini AI Chabot
title.pack(pady=10)

entry = tk.Entry(
    root,
    font=("cursive", 14),
    width=75
)# we create entry box for question entry
entry.pack(pady=10)

ask_button = tk.Button(
    root,
    text="Ask",
    font=("sans-serif", 12, "bold"),
    bg="white",
    fg="purple",
    command=ask_ai
)
ask_button.pack(pady=10)# paddind is mainly focuse on placing component based on
#   x-axis and y-axis

chat_box = scrolledtext.ScrolledText(
    root,
    width=90,
    height=70,
    font=("cursive", 13)#for font size and font style
)#chabox is used for showing answers for user
chat_box.pack(pady=10)#answer getting box

root.mainloop()#showing frame