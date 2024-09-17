IEEE PAPER - https://ieeexplore.ieee.org/document/10465431

### Speech Recognised Voice Bot (Alpha)

Alpha is a speech recocogonised voice bot that uses both machine learning (ML) and deep learning (DL) techniques for advanced tasks like speech recognition, natural language processing (NLP), and question-answering. It performs various tasks such as playing music, fetching weather information, setting reminders, translating languages, answering factual questions, and controlling your system.

Features

- **Play Music**: Play any song from YouTube by saying, "Alpha, play [song name]."
- **Tell Time**: Ask for the current time by saying, "Alpha, what's the time?"
- **Wikipedia Search**: Get a quick summary from Wikipedia by saying, "Alpha, who is [person]?" or "Alpha, what is [subject]?"
- **Tell Jokes**: Get a joke by saying, "Alpha, tell me a joke."
- **Weather Updates**: Ask for the current weather by saying, "Alpha, what's the weather?"
- **Send Emails**: Send an email by saying, "Alpha, send an email."
- **Set Reminders**: Set reminders by saying, "Alpha, remind me to [task]."
- **Language Translation**: Translate text by saying, "Alpha, translate [phrase]."
- **Question Answering**: Alpha uses deep learning models to answer factual questions like, "Alpha, question [your question]."
- **Google Search**: Search for anything on Google by saying, "Alpha, search for [topic]."
- **System Control**: Control your system with commands like "Alpha, shutdown" or "Alpha, restart."

## Machine Learning & Deep Learning Features

- **Speech Recognition**: Alpha uses machine learning models for accurate and real-time speech recognition, allowing you to interact seamlessly.
- **Natural Language Processing (NLP)**: Integrated deep learning models such as transformers are used for language understanding, helping Alpha comprehend complex commands and questions.
- **Question Answering**: Alpha can use pre-trained deep learning models from the [Hugging Face Transformers](https://huggingface.co/transformers/) library to answer complex questions based on context and knowledge.
- **Intent Detection**: Machine learning techniques are used to detect user intent for various commands, improving the assistant’s response accuracy.
  
## Requirements

- Python 3.x
- The following Python packages:
  - `speech_recognition`
  - `pyttsx3`
  - `pywhatkit`
  - `wikipedia-api`
  - `pyjokes`
  - `requests`
  - `googletrans==4.0.0-rc1`
  - `transformers`
  - `torch`
  - `smtplib`
  
  You can install them by running the command:

  ```bash
  pip install SpeechRecognition pyttsx3 pywhatkit wikipedia-api pyjokes requests googletrans==4.0.0-rc1 transformers torch
  ```

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BSRohit20/Development-and-Evaluation-of-Speech-Recogonized-Voice-Bot.git
   ```

2. **Install Dependencies**:
   Navigate to the project directory and install the required libraries using pip:

   ```bash
   cd alpha-voice-assistant
   pip install -r requirements.txt
   ```

3. **Set API Keys**:
   - **Weather API**: Sign up for a free API key on [OpenWeatherMap](https://openweathermap.org/api), and replace `"your_openweather_api_key"` in the `get_weather()` function with your actual API key.
   - **Email Sending**: Replace `"your_email@example.com"` and `"your_password"` in the `send_email()` function with your actual email and password for the bot to send emails.

4. **Run the Assistant**:
   Start the assistant by running the following command:

   ```bash
   python assistant.py
   ```

## Usage

Once the assistant is running, simply say "Alpha" followed by your command. Here are some examples:

- **Play Music**: 
  - Say: "Alpha, play Shape of You."
  
- **Send Email**:
  - Say: "Alpha, send an email."
  - The bot will prompt you for the subject and body of the email.

- **Set Reminder**:
  - Say: "Alpha, remind me to call John at 5 PM."

- **Get Weather**:
  - Say: "Alpha, what's the weather?"

- **Translate Text**:
  - Say: "Alpha, translate Hello, how are you?"

- **Ask a Question**:
  - Say: "Alpha, question What is artificial intelligence?"

- **Search Google**:
  - Say: "Alpha, search for the best programming languages in 2024."

## Machine Learning and Deep Learning

### Speech Recognition
Alpha uses the `speech_recognition` library with machine learning models that handle the transcription of spoken words into text. The assistant processes speech input and performs actions based on the recognized command.

### Natural Language Processing (NLP)
For understanding user commands and questions, Alpha integrates deep learning models from the `transformers` library. Specifically, the bot can answer questions using models like `DistilBERT` or `BERT`, which are trained on large corpora to provide contextual and accurate answers.

### Question Answering
Alpha can answer factual questions based on user input using a transformer model, allowing it to comprehend queries like "What is the capital of France?" or "Who is Albert Einstein?" and provide accurate responses.

### Intent Detection
The assistant uses ML algorithms to identify user intent from speech input. By processing the recognized text, Alpha determines the appropriate action, whether it’s playing music, fetching news, or performing a Google search.

