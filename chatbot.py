import random
import time

def get_ai_response(user_msg):
    msg = user_msg.lower()

    responses = {
        "hello": [
            "Hello 👋 How can I help you today?",
            "Hi there! Ready to explore real-time AI 🚀"
        ],
        "cloud": [
            "Cloud computing allows applications to run on internet servers instead of local machines.",
            "In cloud computing, apps are scalable, available, and globally accessible."
        ],
        "ai": [
            "Artificial Intelligence enables machines to learn, reason, and respond intelligently."
        ]
    }

    time.sleep(0.8)  # thinking delay

    for key in responses:
        if key in msg:
            return random.choice(responses[key])

    return "This is a real-time streaming AI chatbot responding word by word like ChatGPT."
