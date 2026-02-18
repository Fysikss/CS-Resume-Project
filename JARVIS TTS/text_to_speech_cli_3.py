"""
    Name: text_to_speech_cli_3.py
    Author:
    Created:
    Purpose: Render text into speech
    This library has many modules with which you can try
    changing the voice, volume, and speed rate of the audio.
    https://pypi.org/project/pyttsx3/
    https://pyttsx3.readthedocs.io/en/latest/
"""
# pip install pyttsx3
import pyttsx3

class TextToSpeech():
    def __init__(self):
        # -------------- INITIALIZE TEXT TO SPEECH ENGINE ------------ #
        # init function creates an engine
        # instance/object for speech synthesis
        # initialize self.engine

        # Your code here
        self.engine = pyttsx3.init()

        # --------------- VOICE PROPERTIES CONSTANTS ----------------- #
        # The constants stay the same

        # Your code here
        RATE = 175
        VOLUME = .7
        VOICE = 0

        # ------------------ SET VOICE PROPERTIES -------------------- #
        # Set properties before you add items to say
        # Use self.engine to set voice properties

        # Your code here
        self.engine.setProperty("rate", RATE)
        self.engine.setProperty("volume", VOLUME)
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[VOICE].id)

    def speak(self, speak):
        # self.engine say

        # Your code here
        self.engine.say(speak)

        # Program will not continue execution until
        # all speech conversion has completed

        # Your code here
        self.engine.runAndWait()

def main():
    # Create text to speech object
    text_to_speech = TextToSpeech()

    while True:
        # Get input from user
        speak = input("What would you like me to say? ")

        # Queue up things to say
        text_to_speech.speak(speak)

# Run the main function unless this file is imported
if __name__ == "__main__":
    main()