from flask import Flask, request, jsonify
import random
import google.generativeai as genai
import os

app = Flask(__name__)

API_KEYS = ["DEIN_API_KEY_HIER"]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("prompt", "")
    if not user_input:
        return jsonify({"reply": "Bitte gib eine Nachricht ein."})

    genai.configure(api_key=random.choice(API_KEYS))
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat_session = model.start_chat()
    response = chat_session.send_message(user_input)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
