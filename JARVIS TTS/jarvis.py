"""
    Name: jarvis.py
    Author: Noel Onate
    Created: 2/13/26
    Purpose: Voice recognition from Google Speech API OOP
    You can use the Google Speech API for free 50 times a day
"""
# We have to install pyaudio, we do not have to import it
# SpeechRecognition uses pyaudio directly
# pip install pyaudio
# pip install setuptools
# pip install SpeechRecognition
import speech_recognition as sr
from time import sleep
from sys import exit
from text_to_speech_cli_3 import TextToSpeech
import wikipedia_oop

"""Sleep commands are added throughout the program to ensure the mic
    disconnects/reconnects properly and fixing code overlapping with
    the TTS module
"""

class Jarvis:
    def __init__(self) -> None:
        # Create SpeechRecognition recognizer object
        self.r = sr.Recognizer()

        # Create text to speech object
        self.text_to_speech = TextToSpeech()

        # Create Wikipedia object
        self.wikipedia_app = wikipedia_oop.WikipediaApp()

        # Default username for user
        self.username = "Tony"

        # Greet the user
        self.greet_user()

# ----------- GREET USER ------------------------------------------ #
    def greet_user(self):
        print(f"Hello {self.username}!")
        self.text_to_speech.speak(f"Hello {self.username}!")
        sleep(1)

    
# ------------------ USER INPUT ----------------------------------- #
    def user_input(self):
        """Recognizes user voice input using
            Speech recognition module, converts it to text
        """
        # Your local microphone as the source
        sleep(0.5)
        with sr.Microphone() as source:
            print('Listening . . .')

            # Start listening for speech
            audio = self.r.listen(source)

            try:
                print('Recognizing . . .')
                # Capture the recognized word in a string variable
                recognized_words = self.r.recognize_google(
                    audio,
                    language='en-US',
                    show_all=True
                )

                # Google Speech Recognition returns a list of dictionaries
                # Pull only the transcript with the highest confidence
                self.query = recognized_words['alternative'][0]['transcript']

                # If you say quit, the program will exit

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

                # Empty query
                self.query = ""

            except sr.RequestError as e:
                # If there was an error communicating with Google Speech
                print(f"Google Speech did not respond: {e}")

                # Empty query
                self.query = ""

# ------------------ VOICE COMMANDS ------------------------------------------- #
    def voice_commands(self):
        print(self.query)

        # Make jarvis say the words recognized
        self.text_to_speech.speak(self.query)
        sleep(1)

        if "quit" in self.query:
            print(f"Goodbye {self.username}!")
            self.text_to_speech.speak(f"Goodbye {self.username}!")
            sleep(1)
            exit()

        elif "username" in self.query:
            # If user says username, ask them to input a new name
            print("Please enter a new username.")

            # Get new name
            self.username = input(">> ")

            # Repeat new name to user
            self.greet_user()

        elif "Wikipedia" in self.query:
            # Display menu option
            print("+--------------------+")
            print("|  Search Wikipedia  |")
            print("+--------------------+")

            # Ask user what they would like to search for
            print("What would you like to search for on Wikipedia?")
            self.text_to_speech.speak("What would you like to search for on Wikipedia?")

            # Get user input through speech
            self.user_input()

            # Use Wikipedia OOP program to get search results and display them
            self.summary = self.wikipedia_app.get_wikipedia(self.query)
            print(self.summary)

# Create a jarvis program object
jarvis = Jarvis()
while True:
    # Display title and available commands
    print("+--------------------+")
    print("|  JARVIS Main Menu  |")
    print("+--------------------+")
    print("Commands: username, Wikipedia, quit")

    jarvis.user_input()
    jarvis.voice_commands()