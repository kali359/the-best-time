import speech_recognition as sr
from youtube_search import YoutubeSearch
import pyttsx3
import webbrowser


# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))
        return ""

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    print("Voice Assistant: Hello! How can I assist you?")
    while True:
        user_input = speech_to_text().lower()
        if user_input == "exit":
            speak("Goodbye!")
            break
        elif "open google" in user_input:
            webbrowser.open("https://www.google.com")
            speak("Google page opened.")
        elif "search video" in user_input:
            query = user_input.replace("search video", "").strip()
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(search_url)
            speak(f"Searching for {query} on YouTube.")
        elif "search on google" in user_input:
            query = user_input.replace("search on google", "").strip()
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            speak(f"Searching for {query} on Google.")
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
