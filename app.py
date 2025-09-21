from flask import Flask, request, jsonify
import random
import google.generativeai as genai
import os

app = Flask(__name__)

API_KEYS = [
    "AIzaSyD1Rs2JuNdnZTUex80swuXezs72mAhA6j4",
    "AIzaSyCgGxdIXJneSR3pTpxwHEG7aaMoLk4WhAI",
    "AIzaSyB34JLzTswSztt12modJRcSIQLelKlqbkY",
    "AIzaSyDJbKxZ0wL3rX3o0FmMzEbmM5ngjCSyq6U",
    "AIzaSyCrH8NydtsubwAyxozz2CdjsK-kxFX81b8"
]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("prompt", "")
    if not user_input:
        return jsonify({"reply": "Bitte gib eine Nachricht ein."})

    api_key = random.choice(API_KEYS)
    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        chat_session = model.start_chat()
        response = chat_session.send_message(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "Fehler: konnte keine Antwort generieren."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
