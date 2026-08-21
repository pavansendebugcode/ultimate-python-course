'''Exercise -- 10 -----> Write a python program which reminds you of drinking water every hour or two. 
                        Your program can either beep or send desktop notifications for a 
                        specific operating system
'''

import time
import pyttsx3
from plyer import notification


def speak(text):
    # Create a new speech engine each time
    engine = pyttsx3.init()

    engine.setProperty("rate", 170)
    engine.setProperty("volume", 2)

    engine.say(text)
    engine.runAndWait()

    # Properly stop the engine
    engine.stop()


while True:

    message = "Hi , kartik sir  this time  is drinking water  please drink water "

    # Desktop notification
    notification.notify(
        title="Water Reminder",
        message=message,
        timeout=10
    )

    # Speak
    speak(message)

    # Wait 1 hour
    time.sleep(10)