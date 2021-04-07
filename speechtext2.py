from pydub import AudioSegment
import speech_recognition as sr
def audio_processor():
#Code to transcript the audio
    recogniser = sr.Recognizer()
    #the above line starts the recongniser, it can be thought of as a function the recognises the audio

    #convert mp3 to wav

    sound = AudioSegment.from_ogg('voice.ogg')
    sound.export('voice.wav', format='wav')
    transcription_file = 'voice.wav'
    with sr.AudioFile(transcription_file) as source:
        audio =  recogniser.record(source)
        #the above line recorded the audio file in wav format into the recogniser
        text = recogniser.recognize_google(audio)
        #this line is used to use the google speech recognition to convert audio to text
        return text