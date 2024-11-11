import logging
import pyttsx3

class TextToSpeech:
        
    def text_to_speech(text):
        """Converts text to speech and plays it."""
        logging.getLogger("comtypes").setLevel(logging.WARNING)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
