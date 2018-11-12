import aiy.audio
import aiy.cloudspeech
import aiy.voice

def main():
    button = aiy.voicehat.get_button()
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.get_recorder().start()
    while True:
        print("Press the button")
        button.wait_for_press()
        print("Listening")
        text = recognizer.recognize()
        aiy.audio.say('You said ', text)

if __name__ == '__main__':
    main()
