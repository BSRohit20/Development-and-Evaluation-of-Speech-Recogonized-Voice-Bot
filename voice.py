import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import webbrowser
import os
import smtplib
import math
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from googletrans import Translator
from transformers import pipeline

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use the second voice available

# Google Translate API
translator = Translator()

# Initialize NLP model for Q&A
qa_model = pipeline("question-answering")

# Set your email details (Replace with actual credentials)
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"

# Function to convert text to speech
def talk(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    """Listens for user commands and returns the recognized command."""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alpha' in command:
                command = command.replace('alpha', '').strip()
                print(f'Command recognized: {command}')
                return command
            else:
                print('Command not recognized as intended for Alpha.')
                return None
    except sr.RequestError:
        talk("Sorry, I am unable to reach the recognition service.")
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please say the command again.")
    except Exception as e:
        talk(f"An error occurred: {e}")
    return None

# Function to send emails
def send_email(receiver_email, subject, body):
    """Sends an email to the specified address."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, receiver_email, text)
        server.quit()

        talk('Email has been sent.')
    except Exception as e:
        talk('I was unable to send the email.')
        print(f"Email error: {e}")

# Function to get current weather
def get_weather():
    """Fetches current weather data from OpenWeatherMap."""
    api_key = "your_openweather_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "your_city"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            weather_description = weather["description"]
            talk(f"Current temperature in {city_name} is {temperature} degrees Celsius with {weather_description}.")
        else:
            talk("City not found.")
    except Exception as e:
        talk("I was unable to fetch the weather information.")
        print(f"Weather API error: {e}")

# Function to set reminders
def set_reminder(command):
    """Sets a reminder based on voice command."""
    try:
        reminder_time = command.replace('remind me to', '').strip()
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Reminder set for {reminder_time}. Current time is {time}')
    except Exception as e:
        talk('Failed to set a reminder.')
        print(f"Reminder error: {e}")

# Function for language translation
def translate_text(command):
    """Translates text between languages using Google Translate."""
    try:
        if 'translate' in command:
            phrase = command.split('translate')[-1].strip()
            translated_text = translator.translate(phrase, dest='es').text  # Translating to Spanish
            talk(f'The translation is: {translated_text}')
    except Exception as e:
        talk("I couldn't translate the text.")
        print(f"Translation error: {e}")

# Function for answering factual questions
def ask_question(question):
    """Answers factual questions using pre-trained NLP model."""
    try:
        context = "Alpha bot is a speech assistant that can perform a variety of tasks, such as sending emails, setting reminders, telling jokes, and more."
        result = qa_model(question=question, context=context)
        talk(result['answer'])
    except Exception as e:
        talk("I couldn't find the answer to your question.")
        print(f"Q&A error: {e}")

# Function to search on Google
def search_google(query):
    """Performs a Google search based on a voice query."""
    search_query = query.replace('search for', '').strip()
    webbrowser.open(f"https://www.google.com/search?q={search_query}")
    talk(f'Searching Google for {search_query}')

# Function to run the main assistant
def run_alpha():
    """Main function that runs the assistant and processes commands."""
    command = take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f'Playing {song}')
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'Current time is {time}')
        elif 'who is' in command or 'what is' in command:
            person = command.replace('who is', '').replace('what is', '').strip()
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        elif 'email' in command:
            talk("What is the subject of the email?")
            subject = take_command()
            talk("What should I say in the email?")
            body = take_command()
            send_email("receiver_email@example.com", subject, body)  # Replace with actual recipient
        elif 'remind me' in command:
            set_reminder(command)
        elif 'translate' in command:
            translate_text(command)
        elif 'search for' in command:
            search_google(command)
        elif 'weather' in command:
            get_weather()
        elif 'question' in command:
            question = command.replace('question', '').strip()
            ask_question(question)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'shutdown' in command:
            talk('Shutting down the system.')
            os.system('shutdown /s /t 5')
        elif 'restart' in command:
            talk('Restarting the system.')
            os.system('shutdown /r /t 5')
        else:
            talk('I did not understand that command. Please say it again.')
    else:
        print("No command processed.")

if __name__ == "__main__":
    while True:
        run_alpha()
