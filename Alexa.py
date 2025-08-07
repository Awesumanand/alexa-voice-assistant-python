#Importing Libraries
#import speech_recognition as sr
import pyttsx3
#pyAudio
import pywhatkit
import datetime
#PyJokes
#Wikipedia
#openweatherApi
# Importing Required Libraries
import speech_recognition as sr


# Initialize speech recognition and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

def engine_speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def user_command():
    """Function to listen for user command."""
    try:
        with sr.Microphone() as source:
            print("Starting Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f"Command received: {command}")
                return command
            else:
                return None
    except Exception as e:
        print("Error occurred while listening.")
        return None

    except Exception as e:
        print("Sorry, I did not understand that.")
        pass  # or print("Error occurred")
def run_alexa():
    command = user_command()
    if 'play' in command:
        song = command.replace('play', '')
        engine_speak(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        engine_speak("Why don't scientists trust atoms? Because they make up everything!") 
    elif 'weather' in command:
        engine_speak("I can tell you the weather, but I need to be connected to the internet and have access to a weather API.")
    elif 'wikipedia' in command:

        engine_speak("I can search Wikipedia for you, but I need to be connected to the internet.") 
    elif 'time' in command:
        engine_speak("I can tell you the time, but I need to be connected to the internet.")    
    elif 'joke' in command:
        engine_speak("Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif 'search' in command:
        search_query = command.replace('search', '')
        engine_speak(f'Searching for {search_query} on Google.')
        pywhatkit.search(search_query)
    elif 'news' in command:
        engine_speak("I can tell you the news, but I need to be connected to the internet and have access to a news API.")
    elif 'play music' in command:
        song = command.replace('play music', '')
        engine_speak(f'Playing music: {song}')
        pywhatkit.playonyt(song)
    elif 'stop' in command:
        engine_speak("Stopping the music.")
        # Here you would add code to stop the music if applicable
    elif 'stop music' in command:
        engine_speak("Stopping the music.")
        # Here you would add code to stop the music if applicable
    elif 'stop playing' in command:
        engine_speak("Stopping the music.")
        # Here you would add code to stop the music if applicable
    elif 'pause' in command:

        engine_speak("Pausing the music.")
        # Here you would add code to pause the music if applicable
    elif 'pause music' in command:
        engine_speak("Pausing the music.")
        # Here you would add code to pause the music if applicable
    elif 'pause playing' in command:

        engine_speak("Pausing the music.")
        # Here you would add code to pause the music if applicable
    elif 'resume' in command:
        engine_speak("Resuming the music.")
        # Here you would add code to resume the music if applicable
    elif 'resume music' in command:
        engine_speak("Resuming the music.")
        # Here you would add code to resume the music if applicable
    elif 'resume playing' in command:
        engine_speak("Resuming the music.")
        # Here you would add code to resume the music if applicable
    elif 'stop all' in command:

        engine_speak("Stopping all music.")
        # Here you would add code to stop all music if applicable
    elif 'stop all music' in command:
        engine_speak("Stopping all music.")
        # Here you would add code to stop all music if applicable
    elif 'stop all playing' in command:
        engine_speak("Stopping all music.")
        # Here you would add code to stop all music if applicable
    elif 'volume up' in command:
        engine_speak("Turning the volume up.")
        # Here you would add code to turn up the volume if applicable
    elif 'volume down' in command:
        engine_speak("Turning the volume down.")
        # Here you would add code to turn down the volume if applicable
    elif 'mute' in command:

        engine_speak("Muting the music.")
        # Here you would add code to mute the music if applicable
    elif 'unmute' in command:
        engine_speak("Unmuting the music.")
        # Here you would add code to unmute the music if applicable
    elif 'skip' in command:
        engine_speak("Skipping to the next song.")
        # Here you would add code to skip to the next song if applicable
    elif 'previous' in command:

        engine_speak("Going back to the previous song.")
        # Here you would add code to go back to the previous song if applicable
    elif 'next' in command:
        engine_speak("Skipping to the next song.")
        # Here you would add code to skip to the next song if applicable
    elif 'previous song' in command:
        engine_speak("Going back to the previous song.")
        # Here you would add code to go back to the previous song if applicable
    elif 'next song' in command:
        engine_speak("Skipping to the next song.")
        # Here you would add code to skip to the next song if applicable
    elif 'shuffle' in command:
        engine_speak("Shuffling the playlist.")
        # Here you would add code to shuffle the playlist if applicable
    elif 'repeat' in command:
        engine_speak("Repeating the current song.")
        # Here you would add code to repeat the current song if applicable
    elif 'play next' in command:
        engine_speak("Playing the next song.")
        # Here you would add code to play the next song if applicable
    elif 'play previous' in command:
        engine_speak("Playing the previous song.")
        # Here you would add code to play the previous song if applicable       
    elif 'play song' in command:
        engine_speak("Playing the requested song.")
        # Here you would add code to play the song using a library like pywhatkit
    elif 'play song' in command:
        song = command.replace('play song', '')
        engine_speak(f'Playing the song: {song}')
        pywhatkit.playonyt(song)
    elif 'play music' in command:

        song = command.replace('play music', '')
        engine_speak(f'Playing music: {song}')
        pywhatkit.playonyt(song)
    elif 'play track' in command:
        song = command.replace('play track', '')
        engine_speak(f'Playing track: {song}')
        pywhatkit.playonyt(song)
    elif 'play audio' in command:
        song = command.replace('play audio', '')
        engine_speak(f'Playing audio: {song}')
        pywhatkit.playonyt(song)
    elif 'play playlist' in command:
        song = command.replace('play playlist', '')
        engine_speak(f'Playing playlist: {song}')
        pywhatkit.playonyt(song)
    elif 'time =' in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        engine_speak(f"The current time is {current_time}")
    elif 'date' in command:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        engine_speak(f"Today's date is {current_date}")
        
    elif 'stop music' in command:
        engine_speak("Stopping the music.")
        # Here you would add code to stop the music if applicable
    elif 'stop playing' in command:



    else:
        engine_speak("Sorry, I can only play music.")
run_alexa()
            # Here you would add code to play the song using a library like pywhatkit
