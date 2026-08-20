
'''Exercise 9 ----> How to speech text'''



import pyttsx3
import time
# Initialize the speech engine
engine = pyttsx3.init()

# Optional: Adjust voice properties
engine.setProperty('rate', 200)    # Speed of speech (default is around 200)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

x =['zuned', 'kartik','rishi','sachin']
for name in x:    

# Speak aloud
    if name == 'zuned':

        engine.say(f'sir {name} He is trying to impress sonic but sonic is reject zuned   ')
    elif name =='kartik':
        engine.say(f'kartik is not try to impress sonic because he is jenious')

    elif name == 'rishi':
        engine.say(f'he is trying to impress frquency')

    elif name == 'sachin':
        engine.say(f'sonic is reject the')

# Process and run the engine queue
engine.runAndWait()
time.sleep(10)
import os
from gtts import gTTS
from playsound import playsound

# Text to convert
text = "hi i am ai"
# Generate the speech (speciy language 'en' for English)
speech = gTTS(text=text, lang='en', slow=False)

# Save the generated audio file
output_file = "speech.mp3"
speech.save(output_file)

# Play the audio file directly from Python
playsound(output_file)
