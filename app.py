from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatbot import get_ai_response
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('user_message')
def handle_user_message(data):
    user_msg = data['message']

    # notify typing
    emit('bot_typing', broadcast=True)

    # generate reply
    reply = get_ai_response(user_msg)

    # stream word-by-word
    for word in reply.split():
        emit('bot_stream', word + " ", broadcast=True)
        socketio.sleep(0.15)  # streaming speed

    emit('bot_done', broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
