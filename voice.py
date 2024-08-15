import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import webbrowser
import os
import math

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use the second voice available


def talk(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


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
        print("API was unreachable or unresponsive.")
        talk("Sorry, I am unable to reach the recognition service.")
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
        talk("Sorry, I did not catch that. Please say the command again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("An error occurred while processing your request.")
    return None


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


def get_news():
    """Fetches latest news headlines using NewsAPI."""
    api_key = "your_newsapi_key"
    base_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    
    try:
        response = requests.get(base_url)
        news_data = response.json()
        articles = news_data["articles"]
        talk("Here are the top 3 news headlines.")
        for i in range(3):
            talk(articles[i]["title"])
    except Exception as e:
        talk("I was unable to fetch the news headlines.")
        print(f"News API error: {e}")


def get_affirmation():
    """Provides a daily affirmation or motivational quote."""
    affirmations = [
        "You are capable of achieving great things.",
        "Believe in yourself, and all that you are.",
        "Every day is a new opportunity to grow and become better.",
        "You are stronger than you think.",
        "Stay positive, work hard, and make it happen."
    ]
    talk(affirmations[datetime.datetime.now().day % len(affirmations)])


def do_math(command):
    """Performs basic math calculations."""
    try:
        if 'add' in command or '+' in command:
            numbers = [int(s) for s in command.split() if s.isdigit()]
            result = sum(numbers)
        elif 'subtract' in command or '-' in command:
            numbers = [int(s) for s in command.split() if s.isdigit()]
            result = numbers[0] - sum(numbers[1:])
        elif 'multiply' in command or '*' in command:
            numbers = [int(s) for s in command.split() if s.isdigit()]
            result = math.prod(numbers)
        elif 'divide' in command or '/' in command:
            numbers = [int(s) for s in command.split() if s.isdigit()]
            result = numbers[0] / numbers[1]
        else:
            talk("I couldn't understand the math operation.")
            return
        talk(f"The result is {result}")
    except Exception as e:
        talk("I couldn't perform the calculation.")
        print(f"Math calculation error: {e}")


def open_application(command):
    """Opens common applications like a web browser or text editor."""
    if 'browser' in command:
        talk('Opening web browser.')
        webbrowser.open('http://www.google.com')
    elif 'notepad' in command:
        talk('Opening notepad.')
        os.system('notepad')
    else:
        talk('I am not sure how to open that application.')


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
        elif 'who is' in command or 'who the heck is' in command:
            person = command.replace('who is', '').replace('who the heck is', '').strip()
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('Sorry, I have a headache.')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi.')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'weather' in command:
            get_weather()
        elif 'news' in command:
            get_news()
        elif 'affirmation' in command:
            get_affirmation()
        elif any(op in command for op in ['add', 'subtract', 'multiply', 'divide']):
            do_math(command)
        elif 'open' in command:
            open_application(command)
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
