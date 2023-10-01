import tkinter as tk
from tkinter import messagebox
import webbrowser
import wikipedia

def redirect_to_website(url):
    webbrowser.open(url)

def play_song_on_youtube(song_name):
    base_url = "https://www.youtube.com/results?search_query="
    query = song_name.replace(" ", "+")
    url = base_url + query
    redirect_to_website(url)

def google_search(query):
    base_url = "https://www.google.com/search?q="
    query = query.replace(" ", "+")
    url = base_url + query
    redirect_to_website(url)

def get_wikipedia_info(query):
    try:
        summary = wikipedia.summary(query)
        messagebox.showinfo("Wikipedia Info", summary)
    except wikipedia.exceptions.DisambiguationError as e:
        messagebox.showwarning("Wikipedia Info", "Please provide a more specific query.")
    except wikipedia.exceptions.PageError as e:
        messagebox.showwarning("Wikipedia Info", "No information found for the given query.")
    except wikipedia.exceptions.WikipediaException as e:
        messagebox.showerror("Error", "An error occurred while fetching Wikipedia information.")

def process_user_input():
    user_input = entry.get().lower()
    
    if "swiggy" in user_input:
        redirect_to_website("https://www.swiggy.com/")
    elif "amazon" in user_input:
        redirect_to_website("https://www.amazon.com/")
    elif "oyo" in user_input:
        redirect_to_website("https://www.oyorooms.com/")
    elif "youtube" in user_input:
        redirect_to_website("https://www.youtube.com/")
    elif "play song" in user_input:
        song_name = user_input.replace("play song", "").strip()
        play_song_on_youtube(song_name)
    elif "wikipedia" in user_input:
        query = user_input.replace("wikipedia", "").strip()
        get_wikipedia_info(query)
    elif "insta" in user_input:
        redirect_to_website("https://www.instagram.com/")
    elif "fb" in user_input:
        redirect_to_website("https://www.facebook.com/")
    elif "x" in user_input:
        redirect_to_website("https://twitter.com/")
    else:
        google_search(user_input)

    entry.delete(0, tk.END)

app = tk.Tk()
app.title("Chat Bot")

label = tk.Label(app, text="Ask me anything:")
label.pack()

entry = tk.Entry(app, width=50)
entry.pack()

button = tk.Button(app, text="Submit", command=process_user_input)
button.pack()

app.mainloop()
