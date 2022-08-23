
from flask import Flask, request
import datetime


app = Flask(__name__)
all_message = []


@app.route("/")
def index_page():
    """Домашняя страница"""
    return "Hello"


@app.route("/get_messages")
def get_messages():
    """Получить сообщения."""
    return {"messages": all_message}


@app.route('/send_message')
def send_message():
    """Получение из запроса имя отправителя и текст."""
    sender = request.args.get("name")
    text = request.args.get("text")
    add_message(sender, text)
    return 'OK'


def print_message(message):
    """Вывод сообщений."""
    print(
        f"""
         - [{message.get('sender')}] {message.get('text')} / {message.get('time')}
        """
        )


def add_message(sender, text):
    """Добавление сообщений."""
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
    }
    all_message.append(new_message)
    return 'ok'


app.run()


if __name__ == "__main__":

    add_message("Cat", "I need food")
    add_message("Dog", "I need food")
    for msg in all_message:
        print_message(msg)
