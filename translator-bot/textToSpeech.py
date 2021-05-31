import pyttsx3
engine = pyttsx3.init()

#Setting the rate at which the words are spoken in the response
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

#Setting the volume of the sound
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

#Setting whether to use a male voice or a female voice
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#defining the actual function that'll be used
def textToSpeech(message):
    #Saving Voice Note to a file to be send as a response
    engine.save_to_file(message, 'reply.ogg')
    engine.runAndWait()
    #engine.stop()

