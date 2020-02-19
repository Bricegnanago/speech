# import pyaudio
import speech_recognition as sr
import webbrowser
import time
import random
import playsound
import os
from gtts import gTTS
cvt = 0
r = sr.Recognizer()


def brice_speak(audio_string):
    tts = gTTS(text=audio_string, lang='fr')
    r = random.randint(1, 1000000)
    audio_file = "audio-" + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            brice_speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio, language="fr-FR")
            # print(voice_data)
        except sr.UnknownValueError:
            voice_data = 'Rien entendu veuillez repéter s\'il vous plait'
        except sr.RequestError:
            voice_data = 'Notre application est Hors Service'
        return voice_data


def respond(voice):
    global cvt
    if "nom" in voice:
        brice_speak("Je me nomme Brice Gnanago")
    if "date" in voice:
        brice_speak(time.ctime())
    if "recherche" in voice:
        search = record_audio("Que voulez-vous que je cherche pour vous ?")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        brice_speak('Veuillez consulter votre navigateur par defaut !')

    if 'emplacement' in voice:
        brice_speak("Quel emplacement s'il vous plait ")
        location = record_audio(voice)
        url = 'https://www.google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        brice_speak("Voila l'emplacement que vous cherchez !")

    if "comment allez-vous" in voice:
        if cvt == 0:
            brice_speak("Je vais très bien Merci !")
            cvt += 1
            print("svt : " + str(cvt))
        elif cvt > 0:
            brice_speak(
                "Demandez-moi quelque chose d'autre. Savez-vous que je peux faire des recherche en un temps record pour vous ?")
    if 'quitter' in voice:
        brice_speak("Ce service je vous l'aie rendu avec plaisir ! A Bientôt")
        exit()


time.sleep(1)
brice_speak('Bonjour ! Comment pourrais-je vous aider ?')
while 1:
    voice_data = record_audio()  # Ecouter
    respond(voice_data)  # Repondre
