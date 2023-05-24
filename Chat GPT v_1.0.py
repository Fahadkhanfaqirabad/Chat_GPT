import tkinter as tk
from tkinter.constants import *
import mixerpack as m
import openai
api_key = m.openai_API_Key
openai.api_key = api_key
problem = "There is a problem Comming. Please check your internet or Troubleshoot"
# Function to send a message to the OpenAI chatbot model and return its response
def send_message(message_log):
#this is git status checking
    # Use OpenAI's ChatCompletion API to get the chatbot's response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
            messages=message_log,   # The conversation history up to this point, as a list of dictionaries
            max_tokens=3800,        # The maximum number of tokens (words or subwords) in the generated response
            stop=None,              # The stopping sequence for the generated response, if any (not used here)
            temperature=0.7,        # The "creativity" of the generated response (higher temperature = more creative)
        )
    except Exception as e:
         Text1.insert(tk.END, problem + "\n\n\n")
    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response['choices']:
        if 'message' in choice and 'content' in choice['message']:
            return choice['message']['content']
    # If no response with text is found, return an empty string
    return ""
# Function to handle sending user input and displaying responses
def send_user_input(event=None):
    user_input = Entry1.get()
    if "you" in user_input:
            Text1.insert(tk.END, "You: " + user_input + "\n")
            Text1.insert(tk.END, "AI assistant: " + "Sorry sir i cannot understande" + "\n\n\n")
    message_log.append({"role": "user", "content": user_input})
    response = send_message(message_log)
    message_log.append({"role": "assistant", "content": response})
    Text1.config(state=tk.NORMAL)
    Text1.insert(tk.END, "You: " + user_input + "\n")
    Text1.insert(tk.END, "AI assistant: " + response + "\n")
    Text1.config(state=tk.DISABLED)
    Entry1.delete(0, tk.END)
# Initialize the conversation history with a message from the chatbot
message_log = [
     {"role": "system", "content": "You are a helpful assistant."}
     ]
root = tk.Tk()
root.geometry("841x569+219+96")
root.minsize(120, 1)
root.maxsize(1284, 781)
root.title("Chat GPT3")
root.configure(background="#2c2c2c")
root.configure(cursor="icon")
root.configure(highlightbackground="#2d2b2b")
root.configure(highlightcolor="#32252b")
menubar = tk.Menu(root,font="TkMenuFont",bg='#2b2b2b',fg='#4d0b0d')
root.configure(menu = menubar)
Entry1 = tk.Entry(root)
Entry1.place(relx=0.119, rely=0.879, height=40, relwidth=0.766)
Entry1.bind("<Return>", send_user_input)
Entry1.configure(background="#000000")
Entry1.configure(borderwidth="5")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="TkFixedFont")
Entry1.configure(foreground="#ffffff")
Entry1.configure(insertbackground="black")
Text1 = tk.Text(root)
Text1.place(relx=0.036, rely=0.07, relheight=0.78, relwidth=0.932)
Text1.configure(background="#141414")
Text1.configure(font="TkTextFont")
Text1.configure(foreground="#ffffff")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(wrap="word")
Label1 = tk.Label(root)
Label1.place(relx=0.036, rely=0.018, height=21, width=174)
Label1.configure(anchor='w')
Label1.configure(background="#060606")
Label1.configure(compound='left')
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#ffffff")
Label1.configure(highlightbackground="#ffffff")
Label1.configure(text='''CHAT GPT 3''')
root.mainloop()