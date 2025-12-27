def get_ai_response(user_msg):
    msg = user_msg.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! 👋 How can I help you today?"

    elif "who are you" in msg:
        return "I am a real-time AI chatbot built using Flask and WebSockets."

    elif "cloud" in msg:
        return "Cloud computing allows applications to run on internet servers instead of local machines."

    elif "help" in msg:
        return "Sure 🙂 Ask me anything about AI, cloud, or programming."

    elif "bye" in msg:
        return "Goodbye 👋 Have a great day!"

    else:
        return "🤔 I am still learning. Can you rephrase your question?"
