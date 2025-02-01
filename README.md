# DeepSeek_AI Voice Assistant 

Overview (Work in Progess)

This is a simple voice assistant script that can perform various tasks such as:

Checking the time and date

Managing a to-do list

Telling jokes

Searching the web

Taking screenshots

The assistant listens for the wake word "Hey Assistant" and processes voice commands accordingly.

Features

Speech Recognition: Uses speech_recognition to recognize user commands.

Text-to-Speech: Uses pyttsx3 to respond with voice output.

Task Management: Allows adding and viewing tasks in a simple to-do list.

Web Search: Fetches search results using the DuckDuckGo API.

Joke Telling: Fetches jokes using the pyjokes library.

Screenshot Capture: Takes a screenshot and saves it with a timestamp.

Installation

To run this assistant, ensure you have Python installed and install the required dependencies:

pip install pyttsx3 speechrecognition pyjokes requests pyautogui

Usage

Run the script:

python assistant.py

Say "Hey Assistant" to activate it, then give it a command.

Example Commands:

"What time is it?"

"What is today's date?"

"Add task Buy groceries"

"Show tasks"

"Tell me a joke"

"Search Python programming"

"Capture screen"

Notes

The web search feature uses the DuckDuckGo API for retrieving results.

Speech recognition is based on Google Web Speech API and requires an internet connection.

License

This project is open-source and free to use under the MIT License.

