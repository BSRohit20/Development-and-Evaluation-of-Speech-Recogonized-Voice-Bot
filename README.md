#### IEEE PAPER - https://ieeexplore.ieee.org/document/10465431
#### LINK - https://bit.ly/Alphavoicebot
# 🚀 Alpha Full-Stack LLM + Sentiment Voice Assistant

This project is a **full-stack machine learning voice assistant** that combines:
✅ **LLM responses (via OpenRouter + DeepSeek)**
✅ **Your own sentiment analysis ML model (Naive Bayes)**
✅ **Speech input and output (Gradio + Pyttsx3)**
✅ **Frontend + backend + ML model all in one app**

---

## 💡 Features

* 🎤 **Voice + text input**
* 💬 **LLM-powered responses (DeepSeek via OpenRouter)**
* 🧠 **Custom sentiment classifier (Naive Bayes, trained locally)**
* 🔊 **Optional text-to-speech for replies**
* 🌐 **Deployed-ready with Gradio for Hugging Face Spaces**

---

## 📂 Project Structure

```
app/
 ├── app.py                # Gradio app with LLM + sentiment logic
 ├── model.pkl             # Pre-trained sentiment classifier (Naive Bayes)
 ├── requirements.txt      # Python dependencies
 └── README.md             # This file
```

---

## 🛠️ Installation (local)

```bash
git clone https://huggingface.co/spaces/your-username/alpha-voice-assistant
cd alpha-voice-assistant

# Recommended: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 🌍 Deployment on Hugging Face Spaces

✅ This project is designed for **Gradio + Python template Spaces**.
To deploy:
1️⃣ Create a new Space → Select **Gradio / Python template**
2️⃣ Upload:

* `app.py`
* `model.pkl`
* `requirements.txt`
* `README.md`
  3️⃣ Hugging Face will auto-install and serve the app.

---

## 📝 **How it works**

🔹 **LLM (OpenRouter + DeepSeek)**

* We send user input + chat history to OpenRouter’s DeepSeek LLM.
* Get a creative assistant reply.

🔹 **Your ML Model (Sentiment)**

* We trained a Naive Bayes sentiment classifier on small demo data.
* It classifies user input as `positive` or `negative`.

🔹 **Frontend (Gradio)**

* Gradio provides chat UI with both text + audio input.
* Shows LLM response + sentiment label.

🔹 **Optional TTS**

* Uses `pyttsx3` to read LLM reply aloud (can be enabled/disabled).

---

## 🧠 **Training the sentiment model**

If you want to retrain or improve the sentiment model:

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

texts = ["I love this!", "This is bad", "Amazing work", "Terrible experience"]
labels = ["positive", "negative", "positive", "negative"]

vec = CountVectorizer()
X = vec.fit_transform(texts)
clf = MultinomialNB()
clf.fit(X, labels)

joblib.dump((vec, clf), "model.pkl")
```

💡 *Tip: Replace `texts` + `labels` with your own dataset!*

---

## 📌 Requirements

```
gradio
requests
pyttsx3
scikit-learn
joblib
```

*Note: On Spaces, no need to install separately. Just list in `requirements.txt`.*

---

## 🚧 Limitations

⚠️ This project depends on external API (OpenRouter) for LLM, so you need a valid key.
⚠️ The sentiment model is very basic — for production, train on a large dataset.

---

## 🎉 Credits

* OpenRouter.ai (LLM backend)
* DeepSeek LLM
* Gradio (frontend)
* scikit-learn (ML sentiment model)

---

## 💬 Contact

For help, ideas, or feedback, open an issue or contact `your-username` on Hugging Face.

---
