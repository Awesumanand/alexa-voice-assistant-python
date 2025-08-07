import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
from youtubesearchpython import VideosSearch
import webbrowser
import webbrowser
# Alexav1.py - A simple voice assistant that responds to commands prefixed with "Alexa"
# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def engine_speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def user_command():
    """Listen and return user command if it contains 'alexa'."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Command received: {command}")
                return command
    except Exception as e:
        print("Error:", e)
    return ""

def play_song(song):
    """Search YouTube and play the song."""
    videosSearch = VideosSearch(song, limit=1)
    results = videosSearch.result()
    if results["result"]:
        url = results["result"][0]["link"]
        webbrowser.open(url)
    else:
        engine_speak("Sorry, I couldn't find a suitable video on YouTube.")

def run_alexa():
    command = user_command()

    if not command:
        engine_speak("Sorry, I didn't catch that.")
        return

    # Music
    if 'play' in command:
        song = command.replace('play', '').strip()
        engine_speak(f"Playing {song}")
        play_song(song)
    # YouTube
    elif 'youtube' in command:
        video_query = command.replace('youtube', '').strip()
        engine_speak(f"Searching YouTube for {video_query}")
        play_song(video_query)
    # Open website
    elif 'open' in command:
        website = command.replace('open', '').strip()
        if 'http://' not in website and 'https://' not in website:
            website = 'http://' + website
        engine_speak(f"Opening {website}")
        webbrowser.open(website)
    # Weather
    elif 'weather' in command:
        location = command.replace('weather', '').strip()
        engine_speak(f"Fetching weather information for {location}.")
        pywhatkit.search(f"weather in {location}")
    # News
    elif 'news' in command:
        engine_speak("Fetching the latest news.")
        pywhatkit.search("latest news")
    # Calculator
    elif 'calculate' in command:
        calculation = command.replace('calculate', '').strip()
        engine_speak(f"Calculating {calculation}.")
        try:
            result = eval(calculation)
            engine_speak(f"The result is {result}.")
        except Exception as e:
            engine_speak("Sorry, I couldn't perform the calculation.")
        print("Error in calculation:", e)
        pywhatkit.search(f"calculate {calculation}")
# Dictionary
    elif 'define' in command or 'dictionary' in command:
        word = command.replace('define', '').replace('dictionary', '').strip()
        engine_speak(f"Looking up the definition of {word}.")
        pywhatkit.search(f"define {word}")
    # Reminders
    elif 'remind me' in command:
        reminder = command.replace('remind me', '').strip()
        engine_speak(f"Setting a reminder for {reminder}.")
        # Here you could implement a reminder system, e.g., using a database or file
        print(f"Reminder set for: {reminder}")
    # Alarm
    elif 'set alarm' in command:
        alarm_time = command.replace('set alarm', '').strip()
        engine_speak(f"Setting an alarm for {alarm_time}.")
        # Here you could implement an alarm system, e.g., using a scheduling library
        print(f"Alarm set for: {alarm_time}")
    # Translation
    elif 'translate' in command:
        translation_query = command.replace('translate', '').strip()
        engine_speak(f"Translating {translation_query}.")
        pywhatkit.search(f"translate {translation_query}")
    # Wikipedia
    elif 'wikipedia' in command:
        search_query = command.replace('wikipedia', '').strip()
        engine_speak(f"Searching Wikipedia for {search_query}.")
        pywhatkit.search(f"{search_query} site:wikipedia.org")
    # Jokes
    elif 'joke' in command:
        engine_speak("Why don't scientists trust atoms? Because they make up everything!")

    # Time
    elif 'time' in command:
        current_time = datetime.now().strftime("%H:%M")
        engine_speak(f"The current time is {current_time}")

    # Date
    elif 'date' in command:
        current_date = datetime.now().strftime("%Y-%m-%d")
        engine_speak(f"Today's date is {current_date}")

    # Search
    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        engine_speak(f"Searching for {search_query} on Google.")
        pywhatkit.search(search_query)
        print(f"Search query sent: {search_query}")
    # Shutdown
    elif 'shutdown' in command:
        engine_speak("Shutting down the system.")
        # Here you could implement a system shutdown command
        print("System shutdown initiated.")
    # Exit
    elif 'exit' in command or 'quit' in command:
        engine_speak("Exiting the program.")
        print("Program exited.")
        return
    # Default response
    elif 'help' in command:
        engine_speak("Here are some things I can help you with:")
        print("Available commands:")
        for cmd in command_list:
            print(f" - {cmd}")
        engine_speak("You can ask me to do things like:")
        print(" - Play a song")
        print(" - Search YouTube")
        print(" - Open a website")
        print(" - Get the weather")
        print(" - Get the latest news")
        print(" - Perform calculations")
        print(" - Look up definitions")
        print(" - Set reminders")

    elif 'help' not in command:
        engine_speak("Sorry, I didn't understand that command. Please try again.")
        print("Unrecognized command:", command) 
    # Unrecognized command

    else:
        engine_speak("Sorry, I don't understand that command.")

# Start the assistant
run_alexa() 
# This function will keep the assistant running
while True:
    run_alexa()
    print("Listening for the next command...")
# This loop allows the assistant to continuously listen for commands
# You can stop the assistant by using a keyboard interrupt (Ctrl+C) in the terminal
# or by implementing a specific exit command in the run_alexa function.
# This function will keep the assistant running
while True:
    run_alexa()
    print("Listening for the next command...")
# This loop allows the assistant to continuously listen for commands
# You can stop the assistant by using a keyboard interrupt (Ctrl+C) in the terminal
# or by implementing a specific exit command in the run_alexa function.
# This function will keep the assistant running

