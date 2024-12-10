import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()    
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Captures voice input from the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("Sorry, there's an issue with the service.")
    return ""

def perform_task(command):
    """Executes tasks based on voice commands."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "play music" in command:
        music_dir = "C:\\Users\\Hp\\Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music")
    elif "search" in command:
        search_query = command.split("search", 1)[-1].strip()  
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Searching for {search_query}")
        else:
            speak("Please provide something to search.")
    elif "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I can perform limited tasks for now. Try asking for the time, opening Google, or playing music.")

if __name__ == "__main__":
    speak("Hello Yousuf! I am your assistant. How can I help you?")
    while True:
        user_command = listen()
        if user_command:
            perform_task(user_command)
