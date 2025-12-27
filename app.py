from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatbot import get_ai_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('user_message')
def handle_user_message(data):
    user_msg = data['message']
    bot_reply = get_ai_response(user_msg)

    emit('bot_message', {
        'user': user_msg,
        'bot': bot_reply
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
