import datetime
import pyjokes
import requests
import pyautogui
import time
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Initialize speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Simulated DeepSeek NLP (replace with actual DeepSeek API if available)
class DeepSeek:
    def understand(self, command):
        command = command.lower()
        if "time" in command:
            return "get_time"
        elif "date" in command:
            return "get_date"
        elif "add task" in command:
            return "add_task"
        elif "show tasks" in command or "to-do list" in command:
            return "show_tasks"
        elif "joke" in command:
            return "tell_joke"
        elif "search" in command:
            return "search_web"
        elif "capture screen" in command or "screenshot" in command:
            return "capture_screen"
        else:
            return "unknown"

# Initialize DeepSeek (simulated)
ds = DeepSeek()

# To-Do List
todo_list = []

# Get Current Time
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

# Get Current Date
def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# Add Task to To-Do List
def add_task(task):
    todo_list.append(task)
    return f"Task '{task}' added."

# Show To-Do List
def show_tasks():
    if todo_list:
        return "\n".join([f"{i+1}. {task}" for i, task in enumerate(todo_list)])
    else:
        return "No tasks in the list."

# Tell a Joke
def tell_joke():
    return pyjokes.get_joke()

# Search the Web (using DuckDuckGo API)
def search_web(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    data = response.json()
    if "Abstract" in data and data["Abstract"]:
        return data["Abstract"]
    else:
        return "Sorry, I couldn't find any information on that."

# Capture Screen
def capture_screen():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(filename)
    return f"Screenshot saved as {filename}"

# Speak Function
def speak(text):
    print(f"Assistant: {text}")  # Print the response to the console
    engine.say(text)  # Convert text to speech
    engine.runAndWait()  # Wait for the speech to finish

# Listen for Wake Word
def listen_for_wake_word():
    with microphone as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen for audio input

    try:
        # Recognize speech using Google Web Speech API
        wake_word = recognizer.recognize_google(audio).lower()
        print(f"Heard: {wake_word}")
        if "hey assistant" in wake_word:
            return True
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
    return False

# Listen for User Commands
def listen_for_command():
    with microphone as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen for audio input

    try:
        # Recognize speech using Google Web Speech API
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
    return None

# Process User Commands
def process_command(command):
    intent = ds.understand(command)
    if intent == "get_time":
        return get_time()
    elif intent == "get_date":
        return get_date()
    elif intent == "add_task":
        task = command.split("add task")[1].strip()
        return add_task(task)
    elif intent == "show_tasks":
        return show_tasks()
    elif intent == "tell_joke":
        return tell_joke()
    elif intent == "search_web":
        query = command.split("search")[1].strip()
        return search_web(query)
    elif intent == "capture_screen":
        return capture_screen()
    else:
        return "Sorry, I didn't understand that."

# Main Loop
def main():
    speak("Hello! I'm your virtual assistant. Say 'Hey Assistant' to wake me up.")
    while True:
        if listen_for_wake_word():
            speak("How can I help you?")
            while True:
                command = listen_for_command()
                if command:
                    if command.lower() in ["exit", "quit", "bye"]:
                        speak("Goodbye!")
                        return
                    response = process_command(command)
                    speak(response)

# Run the Assistant
if __name__ == "__main__":
    main()
