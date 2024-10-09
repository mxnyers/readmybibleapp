import pyttsx3

def text_to_speech(text):
    """Converts text to speech and plays it."""

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)