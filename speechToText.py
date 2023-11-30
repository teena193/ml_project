# import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio_text = r.listen(source, timeout=10)  # Timeout is set to 5 seconds, adjust as needed

# recognize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using Google Speech Recognition
    text = r.recognize_google(audio_text)
    print('Converting audio transcripts into text ...')
    print('You said:', text)
except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except sr.RequestError as e:
    print(f'Could not request results from Google Speech Recognition service; {e}')

# Note: Make sure you have an active internet connection for Google Speech Recognition to work.
