import speech_recognition as sr
import pytts3
import pywhatkit 

listener = sr.recognizer()
engine = say()
voices = engine.getProperty("voice")
engine.setProperty('voice' , voice[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('litening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alixa'in command:
                commed = command.replace('alexa')
                print(command)
    except:
        pass 
        return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play' , '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    else:
        talk('plese say the command again')

    while True:
        run_alexa()