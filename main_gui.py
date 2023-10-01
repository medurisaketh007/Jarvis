import tkinter as tk
from tkinter import font
import subprocess
from PIL import Image, ImageTk
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def recognize_speech_online(audio):
    recognizer = sr.Recognizer()
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""

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
        speak("Wikipedia Info", summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Wikipedia Info", "Please provide a more specific query.")
    except wikipedia.exceptions.PageError as e:
       speak("Wikipedia Info", "No information found for the given query.")
    except wikipedia.exceptions.WikipediaException as e:
        speak("Error", "An error occurred while fetching Wikipedia information.")


def run_air_canvas():
    subprocess.Popen(["python3", "Air-canvas.py"])

def run_chat_bot():
    subprocess.Popen(["python3", "chat_bot_gui.py"])

def start_voice_assistant():
    speak("Hi Saketh! Jarvis in your service!")
    recognizer = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognize_speech_online(audio)
        print("You said:", user_input)
        if "open air canvas" in user_input:
            run_air_canvas()
            speak("Yes Boss! Here is your Air Canvas")
        elif "open chatbot" in user_input:
            run_chat_bot()
            speak("Yes Boss! Here is your Chat Bot")
        elif "swiggy" in user_input:
            redirect_to_website("https://www.swiggy.com/")
            speak("Yes Boss!")
        elif "amazon" in user_input:
            redirect_to_website("https://www.amazon.com/")
            speak("Yes Boss!")
        elif "oyo" in user_input:
            redirect_to_website("https://www.oyorooms.com/")
            speak("Yes Boss!")
        elif "youtube" in user_input:
            redirect_to_website("https://www.youtube.com/")
            speak("Yes Boss!")
        elif "play" in user_input:
            song_name = user_input.replace("play", "").strip()
            play_song_on_youtube(song_name)
            speak("Yes Boss!")
        elif "wikipedia" in user_input:
            query = user_input.replace("wikipedia", "").strip()
            speak("Yes Boss!")
            get_wikipedia_info(query)
        elif "insta" in user_input:
            redirect_to_website("https://www.instagram.com/")
            speak("Yes Boss!")
        elif "fb" in user_input:
            redirect_to_website("https://www.facebook.com/")
            speak("Yes Boss!")
        elif "twitter" in user_input:
            redirect_to_website("https://twitter.com/")
            speak("Yes Boss!")
        elif "who created you" in user_input:
            speak("Saketh has created me! He is my boss! He is the creater and destroyer. I am under his control.")
        elif "allah" in user_input:
            speak("Islam is bullshit. Hinduism is supreme. Stay calm and say ,  Jai Shree Ram! ")
        elif "god" in user_input:
            speak("Hare Rama hare Rama rama rama hare hare , hare krishna hare krishna krishna krishna hare hare.")
        else:
            google_search(user_input)
            speak("Yes Boss!")

    except sr.RequestError as e:
        print("Error with the service; {0}".format(e))
        speak("Sorry Boss! , Error with the service")
    except Exception as ex:
        print("Error: {0}".format(ex))
        speak("Sorry Boss! Something went wrong.")

# Create the Tkinter root window
root = tk.Tk()
root.title("Main GUI")

# Set custom font and color for the title
title_font = font.Font(family="Helvetica", size=30, weight="bold")
title_label = tk.Label(root, text="JARVIS", font=title_font, fg="red")
title_label.pack(pady=20)

# Load the image using PIL
jarvis_image = Image.open("jarvis.png")
jarvis_image = ImageTk.PhotoImage(jarvis_image)

# Create a label to display the image
image_label = tk.Label(root, image=jarvis_image)
image_label.pack(pady=10)

button_canvas = tk.Button(root, text="Open Air Canvas", command=run_air_canvas, width=20, height=2)
button_canvas.pack(pady=10)

button_chat_bot = tk.Button(root, text="Open Chat Bot", command=run_chat_bot, width=20, height=2)
button_chat_bot.pack(pady=10)

# Add the voice assistant button
button_voice_assistant = tk.Button(root, text="Voice Assistant", command=start_voice_assistant, width=20, height=2)
button_voice_assistant.pack(pady=10)

# Increase the size of the main window
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Start the Tkinter main loop
root.mainloop()
