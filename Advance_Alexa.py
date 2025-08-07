import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
from youtubesearchpython import VideosSearch
import webbrowser
import random

# Alexa Voice Assistant - Corrected and Enhanced Version
print("🚀 Initializing Alexa Voice Assistant...")

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties for better experience
try:
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
except Exception as e:
    print(f"Voice setup warning: {e}")

# Command list for help function
command_list = [
    "Play [song name] - Play music from YouTube",
    "YouTube [search term] - Search YouTube videos", 
    "Open [website] - Open any website",
    "Weather in [location] - Get weather information",
    "News - Get latest news",
    "Calculate [expression] - Perform calculations",
    "Define [word] - Get word definitions",
    "Remind me [task] - Set reminders",
    "Set alarm [time] - Set alarms",
    "Translate [text] - Translate text",
    "Wikipedia [topic] - Search Wikipedia",
    "Tell me a joke - Get random jokes",
    "What time is it - Get current time",
    "What's the date - Get current date",
    "Search [query] - Search on Google",
    "Help - Show this command list",
    "Exit/Quit - Close the assistant",
    "Shutdown - Shutdown system"
]

def engine_speak(text):
    """Convert text to speech with error handling."""
    try:
        print(f"🤖 Alexa: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def user_command():
    """Listen and return user command if it contains 'alexa'."""
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening... (Say 'Alexa' followed by your command)")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=10, phrase_time_limit=10)
            command = listener.recognize_google(voice).lower()
            
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"✅ Command received: '{command}'")
                return command
            else:
                print("❌ Command must start with 'Alexa'")
                return ""
                
    except sr.WaitTimeoutError:
        print("⏱️ Listening timeout - no speech detected")
        return ""
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"❌ Speech recognition error: {e}")
        return ""
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return ""

def play_song(song):
    """Search YouTube and play the song."""
    try:
        print(f"🔍 Searching for: {song}")
        videosSearch = VideosSearch(song, limit=1)
        results = videosSearch.result()
        
        if results["result"]:
            url = results["result"][0]["link"]
            title = results["result"][0]["title"]
            print(f"🎵 Found: {title}")
            webbrowser.open(url)
            return f"Now playing {title}"
        else:
            return "Sorry, I couldn't find that song on YouTube."
    except Exception as e:
        print(f"Error playing song: {e}")
        return "Sorry, there was an error playing the song."

def safe_calculation(expression):
    """Safely evaluate mathematical expressions."""
    try:
        # Remove any potentially dangerous characters
        allowed_chars = "0123456789+-*/.() "
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return str(result)
        else:
            return "Invalid calculation expression"
    except Exception:
        return "Could not calculate that expression"

def run_alexa():
    """Main function to process voice commands."""
    command = user_command()

    if not command:
        return True  # Continue listening

    try:
        # Music commands
        if 'play' in command:
            song = command.replace('play', '').strip()
            if song:
                engine_speak(f"Playing {song}")
                response = play_song(song)
                if "error" in response.lower():
                    engine_speak(response)
            else:
                engine_speak("What would you like me to play?")

        # YouTube search
        elif 'youtube' in command:
            video_query = command.replace('youtube', '').strip()
            if video_query:
                engine_speak(f"Searching YouTube for {video_query}")
                response = play_song(video_query)
                if "error" in response.lower():
                    engine_speak(response)
            else:
                engine_speak("What would you like me to search on YouTube?")

        # Open website
        elif 'open' in command:
            website = command.replace('open', '').strip()
            if website:
                if not (website.startswith('http://') or website.startswith('https://')):
                    website = 'https://' + website
                engine_speak(f"Opening {website}")
                webbrowser.open(website)
            else:
                engine_speak("Which website would you like me to open?")

        # Weather information
        elif 'weather' in command:
            location = command.replace('weather', '').replace('in', '').strip()
            if location:
                engine_speak(f"Getting weather information for {location}")
                pywhatkit.search(f"weather in {location}")
            else:
                engine_speak("Which location's weather would you like to know?")

        # Latest news
        elif 'news' in command:
            engine_speak("Getting the latest news for you")
            pywhatkit.search("latest news today")

        # Calculator
        elif 'calculate' in command or 'math' in command:
            calculation = command.replace('calculate', '').replace('math', '').strip()
            if calculation:
                engine_speak(f"Calculating {calculation}")
                try:
                    result = safe_calculation(calculation)
                    engine_speak(f"The result is {result}")
                    print(f"🔢 {calculation} = {result}")
                except:
                    engine_speak("I couldn't perform that calculation. Let me search for it.")
                    pywhatkit.search(f"calculate {calculation}")
            else:
                engine_speak("What would you like me to calculate?")

        # Dictionary/Define
        elif 'define' in command or 'dictionary' in command or 'meaning' in command:
            word = command.replace('define', '').replace('dictionary', '').replace('meaning of', '').strip()
            if word:
                engine_speak(f"Looking up the definition of {word}")
                pywhatkit.search(f"define {word}")
            else:
                engine_speak("Which word would you like me to define?")

        # Reminders
        elif 'remind me' in command:
            reminder = command.replace('remind me', '').strip()
            if reminder:
                engine_speak(f"I'll remind you {reminder}")
                print(f"📝 Reminder set: {reminder}")
                # Note: This is a placeholder - you'd need to implement actual reminder functionality
            else:
                engine_speak("What would you like me to remind you about?")

        # Alarms
        elif 'set alarm' in command or 'alarm' in command:
            alarm_time = command.replace('set alarm', '').replace('alarm for', '').strip()
            if alarm_time:
                engine_speak(f"Setting an alarm for {alarm_time}")
                print(f"⏰ Alarm set for: {alarm_time}")
                # Note: This is a placeholder - you'd need to implement actual alarm functionality
            else:
                engine_speak("What time would you like me to set the alarm for?")

        # Translation
        elif 'translate' in command:
            translation_query = command.replace('translate', '').strip()
            if translation_query:
                engine_speak(f"Translating: {translation_query}")
                pywhatkit.search(f"translate {translation_query}")
            else:
                engine_speak("What would you like me to translate?")

        # Wikipedia search
        elif 'wikipedia' in command:
            search_query = command.replace('wikipedia', '').strip()
            if search_query:
                engine_speak(f"Searching Wikipedia for {search_query}")
                pywhatkit.search(f"{search_query} site:wikipedia.org")
            else:
                engine_speak("What would you like me to search on Wikipedia?")

        # Jokes
        elif 'joke' in command or 'funny' in command:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the math book look so sad? Because it had too many problems!",
                "What do you call a fake noodle? An impasta!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What do you call a bear with no teeth? A gummy bear!"
            ]
            joke = random.choice(jokes)
            engine_speak(joke)

        # Time
        elif 'time' in command:
            current_time = datetime.now().strftime("%I:%M %p")
            engine_speak(f"The current time is {current_time}")
            print(f"🕐 Current time: {current_time}")

        # Date
        elif 'date' in command:
            current_date = datetime.now().strftime("%B %d, %Y")
            engine_speak(f"Today's date is {current_date}")
            print(f"📅 Current date: {current_date}")

        # General search
        elif 'search' in command:
            search_query = command.replace('search', '').strip()
            if search_query:
                engine_speak(f"Searching for {search_query}")
                pywhatkit.search(search_query)
                print(f"🔍 Searched: {search_query}")
            else:
                engine_speak("What would you like me to search for?")

        # Help command
        elif 'help' in command:
            engine_speak("Here are the commands I can help you with:")
            print("\n📋 AVAILABLE COMMANDS:")
            print("=" * 50)
            for i, cmd in enumerate(command_list, 1):
                print(f"{i:2d}. {cmd}")
            print("=" * 50)
            engine_speak("I can help with music, web searches, calculations, weather, news, and much more!")

        # System shutdown
        elif 'shutdown' in command:
            engine_speak("I cannot shutdown the system, but I can exit the program.")
            print("⚠️ System shutdown not implemented for safety reasons")

        # Exit commands
        elif 'exit' in command or 'quit' in command or 'goodbye' in command:
            engine_speak("Goodbye! Thanks for using Alexa Assistant.")
            print("👋 Exiting Alexa Assistant...")
            return False

        # Unrecognized command
        else:
            engine_speak("I'm sorry, I didn't understand that command. Try saying 'Alexa help' to see available commands.")
            print(f"❓ Unrecognized command: '{command}'")

    except Exception as e:
        print(f"❌ Error processing command: {e}")
        engine_speak("Sorry, there was an error processing your command.")

    return True

def main():
    """Main program loop."""
    print("🎉 Alexa Voice Assistant is ready!")
    print("💡 Say 'Alexa' followed by your command")
    print("💡 Say 'Alexa help' to see all available commands")
    print("💡 Say 'Alexa exit' to quit the program")
    print("-" * 50)
    
    engine_speak("Hello! I'm your Alexa assistant. I'm ready to help you!")
    
    try:
        while True:
            if not run_alexa():
                break
            print("-" * 30)
    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user")
        engine_speak("Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        engine_speak("Sorry, an unexpected error occurred. Goodbye!")
    finally:    
        engine_speak("Thank you for using Alexa Assistant. Goodbye!")
        print("👋 Exiting Alexa Assistant...")
    print("🎉 Alexa Assistant has stopped.")
    return
3. Save and Run

Save the corrected Python code as Advance_Alexa.py
Run it with: python Advance_Alexa.py
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from datetime import datetime

class ModernVoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎤 Alexa Voice Assistant")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1e1e2e")
        self.root.minsize(1000, 700)

        self.start_time = datetime.now()

        self.setup_styles()
        self.build_ui()
        self.update_uptime()

    def setup_styles(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')

        style.configure('TFrame', background='#1e1e2e')
        style.configure('Title.TLabel', font=('Segoe UI', 24, 'bold'), foreground="#00d4ff", background="#1e1e2e")
        style.configure('Sub.TLabel', font=('Segoe UI', 11), foreground="#cdd6f4", background="#1e1e2e")
        style.configure('Log.TLabel', font=('Consolas', 10), foreground="#cdd6f4", background="#1e1e2e")
        style.configure('TButton', font=('Segoe UI', 10), padding=6)

    def build_ui(self):
        # Top Bar
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

        title = ttk.Label(top_frame, text="🎤 Alexa Voice Assistant", style='Title.TLabel')
        title.pack(side=tk.LEFT)

        self.uptime_label = ttk.Label(top_frame, text="Uptime: 00:00:00", style='Sub.TLabel')
        self.uptime_label.pack(side=tk.RIGHT)

        # Content Area
        content_frame = ttk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left: Controls
        control_frame = ttk.LabelFrame(content_frame, text="🎮 Controls", padding=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        mic_btn = tk.Button(control_frame, text="🎤 Start Listening", font=('Segoe UI', 14), bg="#00d4ff", fg="white", relief="flat")
        mic_btn.pack(pady=20, fill=tk.X)

        ttk.Button(control_frame, text="🎵 Play Music").pack(fill=tk.X, pady=5)
        ttk.Button(control_frame, text="🌤️ Weather").pack(fill=tk.X, pady=5)
        ttk.Button(control_frame, text="🕒 Time").pack(fill=tk.X, pady=5)
        ttk.Button(control_frame, text="📖 Help").pack(fill=tk.X, pady=5)

        # Right: Log Area
        right_frame = ttk.LabelFrame(content_frame, text="📋 Activity Log", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.log_box = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, font=('Consolas', 10),
                                                 bg="#1e1e2e", fg="#cdd6f4", insertbackground='white')
        self.log_box.pack(fill=tk.BOTH, expand=True)

        self.log("system", "🔧 GUI Initialized Successfully")

    def log(self, tag, message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.log_box.insert(tk.END, f"[{timestamp}] {tag.upper()}: {message}\n")
        self.log_box.see(tk.END)

    def update_uptime(self):
        now = datetime.now()
        uptime = now - self.start_time
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        self.uptime_label.config(text=f"Uptime: {hours:02}:{minutes:02}:{seconds:02}")
        self.root.after(1000, self.update_uptime)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernVoiceAssistantGUI(root)
    root.mainloop()


'''🎮 How to Use
Voice Commands Format:
Always start with "Alexa" followed by your command:
🎵 Entertainment:

"Alexa, play Shape of You"
"Alexa, youtube funny cats"
"Alexa, tell me a joke"

🌐 Web & Search:

"Alexa, open google.com"
"Alexa, search artificial intelligence"
"Alexa, wikipedia Albert Einstein"

🌤️ Information:

"Alexa, weather in New York"
"Alexa, news"
"Alexa, what time is it?"
"Alexa, what's the date?"

🔧 Utilities:

"Alexa, calculate 15 times 25"
"Alexa, define computer"
"Alexa, translate hello to Spanish"
"Alexa, remind me to call mom"
"Alexa, set alarm for 7 AM"

⚙️ System:

"Alexa, help" - Show all commands
"Alexa, exit" - Close the program'''