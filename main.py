import pyttsx3

def list_voices(engine):
    voices = engine.getProperty('voices')
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name}")
    return voices

def text_to_speech():
    engine = pyttsx3.init()

    # List available voices
    voices = list_voices(engine)
    choice = input("Choose a voice index (e.g., 0 or 1): ")

    # Set selected voice
    try:
        engine.setProperty('voice', voices[int(choice)].id)
    except (IndexError, ValueError):
        print("Invalid choice. Using default voice.")

    # Set optional properties
    engine.setProperty('rate', 150)    # Speed
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Get text from user
    text = input("\nEnter text to convert to speech:\n")

    if text.strip():
        print("Speaking...")
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text entered.")

if __name__ == "__main__":
    text_to_speech()
