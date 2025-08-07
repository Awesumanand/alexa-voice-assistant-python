import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
import pywhatkit
from youtubesearchpython import VideosSearch
from datetime import datetime
import webbrowser

# --------------------- Initialize Assistant ---------------------
listener = sr.Recognizer()
engine = pyttsx3.init()

def engine_speak(text):
    engine.say(text)
    engine.runAndWait()

# --------------------- GUI Setup ---------------------
root = tk.Tk()
root.title("Alexa Voice Assistant")
root.geometry("600x400")
root.configure(bg="#1e1e2f")

FONT_TITLE = ("Helvetica", 20, "bold")
FONT_BODY = ("Helvetica", 12)
COLOR_ACCENT = "#00FFFF"

status_var = tk.StringVar()
status_var.set("Status: Waiting for 'Alexa'...")

def update_status(text):
    status_var.set("Status: " + text)

def update_display(text):
    display_area.insert(tk.END, text + "\n")
    display_area.yview(tk.END)

title = tk.Label(root, text="🎤 Alexa Voice Assistant", font=FONT_TITLE, bg="#1e1e2f", fg=COLOR_ACCENT)
title.pack(pady=10)

status_label = tk.Label(root, textvariable=status_var, font=FONT_BODY, bg="#1e1e2f", fg="#FFFFFF")
status_label.pack(pady=5)

display_area = scrolledtext.ScrolledText(root, height=8, font=FONT_BODY, bg="#2d2d44", fg="#00ffcc")
display_area.pack(padx=20, pady=10, fill=tk.BOTH)

# --------------------- Functional Logic ---------------------
def play_song(song):
    update_status(f"Searching for '{song}'")
    try:
        videosSearch = VideosSearch(song, limit=1)
        results = videosSearch.result()
        if results["result"]:
            url = results["result"][0]["link"]
            webbrowser.open(url)
            update_status(f"Playing: {song}")
        else:
            engine_speak("Sorry, I couldn't find that song.")
            update_status("Video not found.")
    except Exception as e:
        engine_speak("Something went wrong while searching.")
        update_status(f"Error: {e}")

def process_command(command):
    update_display(f"You said: {command}")

    if 'play' in command:
        song = command.replace('play', '').strip()
        engine_speak(f"Playing {song}")
        play_song(song)

    elif 'joke' in command:
        joke = "Why don't scientists trust atoms? Because they make up everything!"
        engine_speak(joke)
        update_status("Told a joke.")

    elif 'time' in command:
        current_time = datetime.now().strftime("%H:%M")
        engine_speak(f"The current time is {current_time}")
        update_status("Told time.")

    elif 'date' in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        engine_speak(f"Today's date is {current_date}")
        update_status("Told date.")

    elif 'search' in command:
        query = command.replace('search', '').strip()
        engine_speak(f"Searching for {query}")
        pywhatkit.search(query)
        update_status(f"Searched: {query}")

    elif 'stop' in command or 'exit' in command:
        engine_speak("Goodbye!")
        root.quit()

    else:
        engine_speak("Sorry, I don't understand that.")
        update_status("Unknown command")

def run_assistant():
    update_status("Listening for next command...")
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source, timeout=5)
            command = listener.recognize_google(audio).lower()
            process_command(command)

    except sr.UnknownValueError:
        engine_speak("Sorry, I didn't catch that.")
        update_status("Could not understand audio.")
    except sr.WaitTimeoutError:
        update_status("No input detected.")
    except Exception as e:
        engine_speak("An error occurred.")
        update_status(f"Error: {e}")

def wake_word_listener():
    update_status("Listening for 'Alexa'...")
    while True:
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                audio = listener.listen(source, timeout=5)
                command = listener.recognize_google(audio).lower()
                print(f"Heard: {command}")

                if 'alexa' in command:
                    update_status("Wake word detected!")
                    engine_speak("Yes?")
                    run_assistant()
                else:
                    update_status("Listening for 'Alexa'...")

        except sr.WaitTimeoutError:
            update_status("No speech detected. Retrying...")
        except sr.UnknownValueError:
            continue
        except Exception as e:
            update_status(f"Error: {e}")

# --------------------- Start Button ---------------------
start_btn = tk.Button(
    root,
    text="🎙 Start Wake Word Listener",
    font=FONT_BODY,
    bg=COLOR_ACCENT,
    fg="black",
    command=lambda: threading.Thread(target=wake_word_listener, daemon=True).start()
)
start_btn.pack(pady=10)

# --------------------- Run GUI Loop ---------------------
root.mainloop()