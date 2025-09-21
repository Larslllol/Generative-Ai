import random
import google.generativeai as genai
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['GRPC_VERBOSITY'] = 'ERROR'

class NullWriter:
    def write(self, x):
        pass
    def flush(self):
        pass

API_KEYS = [
    "AIzaSyD1Rs2JuNdnZTUex80swuXezs72mAhA6j4",
    "AIzaSyCgGxdIXJneSR3pTpxwHEG7aaMoLk4WhAI",
    "AIzaSyB34JLzTswSztt12modJRcSIQLelKlqbkY",
    "AIzaSyDJbKxZ0wL3rX3o0FmMzEbmM5ngjCSyq6U",
    "AIzaSyCrH8NydtsubwAyxozz2CdjsK-kxFX81b8"
]

print("Chat with LARSGPT! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting chat...")
        break
    
    api_key = random.choice(API_KEYS)
    try:
        original_stderr = sys.stderr
        sys.stderr = NullWriter()
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        chat = model.start_chat()
        response = chat.send_message(user_input)
        
        sys.stderr = original_stderr
        
        print("LARSGPT:", response.text)
    except Exception as e:
        sys.stderr = original_stderr
        print("LARSGPT: Es tut mir leid, ich konnte keine Antwort generieren. Bitte versuchen Sie es erneut.")