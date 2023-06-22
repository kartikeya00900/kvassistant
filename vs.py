import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser as wb

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Sorry, I'm unable to access the Google Speech Recognition service.")
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'where is' in command:
        location = command.replace('where is', '')
        speak('Here is what I found for ' + location)
        map_url = "https://www.google.com/maps"
        place = ("/place/" + location)
        wb.open(map_url + place)

    elif 'play' in command:
        song = command.replace('play', '')
        speak('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak("Here's what I found about " + person + ": " + info)

    elif 'what is' in command:
        topic = command.replace('what is', '')
        speak("Searching for information about " + topic)
        wb.open_new_tab('https://www.google.com/search?q=' + topic)

    else:
        speak('I did not understand the command. Please try again.')


text = "Good Morning Inspection Team. Welcome to our Computer Lab. Press the 'Space Bar' to ask your question."
print(text)
speak(text)

while True:
    key = input("Press Enter to ask a question or 'q' to quit: ")
    if key == 'q':
        break
    elif key == '':
        run_alexa()
