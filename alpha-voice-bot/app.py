import gradio as gr
import requests
import json
import pyttsx3
import threading
import speech_recognition as sr

# 🔐 OpenRouter API Key and model
API_KEY = "API TOKEN"
MODEL = "deepseek/deepseek-chat-v3-0324:free"

def query_openrouter(messages, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": 1024,
        "stream": False
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ OpenRouter error: {str(e)}"

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

def handle_input(user_input, chat_history, temperature):
    if not user_input:
        return chat_history

    messages = [{"role": "system", "content": "You are a helpful and intelligent assistant."}]
    for user_msg, assistant_msg in chat_history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    messages.append({"role": "user", "content": user_input})

    reply = query_openrouter(messages, temperature)
    chat_history.append((user_input, reply))
    threading.Thread(target=speak_text, args=(reply,)).start()
    return chat_history

def handle_audio(audio_file, chat_history, temperature):
    try:
        text = transcribe_audio(audio_file)
        return handle_input(text, chat_history, temperature)
    except Exception as e:
        return chat_history + [("🎙️ Mic input failed", f"⚠️ Error: {e}")]

# 🎨 Gradio UI
with gr.Blocks(css=".gradio-container {max-width: 800px; margin: auto;}") as demo:
    gr.Markdown("""
    <div style="text-align: center; padding: 10px;">
        <h1 style="font-size: 2.2em;">🎤🤖 Alpha Voice Assistant</h1>
        <p style="font-size: 1.1em;">Chat via voice or text, powered by DeepSeek + OpenRouter</p>
    </div>
    """)

    chatbot = gr.Chatbot(label="💬 Chat History", height=400)
    chat_state = gr.State([])

    with gr.Row():
        manual_input = gr.Textbox(placeholder="Type a message...", show_label=False, container=False, scale=4)
        audio_input = gr.Audio(type="filepath", label="🎙 Record Voice", scale=1)
        clear_btn = gr.Button("🗑", scale=1)

    temperature = gr.Slider(0, 1, value=0.7, step=0.1, label="🧠 Creativity Level")

    manual_input.submit(fn=handle_input,
                        inputs=[manual_input, chat_state, temperature],
                        outputs=chatbot)

    audio_input.change(fn=handle_audio,
                       inputs=[audio_input, chat_state, temperature],
                       outputs=chatbot)

    clear_btn.click(lambda: [], None, chatbot)
    clear_btn.click(lambda: [], None, chat_state)

demo.launch()
