from flask import Flask, render_template, request, url_for, flash, redirect, session
from gptqueries import ask, update_log
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloeiwur92843uqghvnefjancwqefjfjewngvve'
messages = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        incoming_msg = request.form['content']

        if not incoming_msg:
            flash('Content is required!')
        else:

            # obtain chat_log
            chat_log = session.get('chat_log')

            # obtain a response, update our session's chat_log
            bot_answer = ask(incoming_msg, chat_log)
            session['chat_log'] = update_log(bot_answer, chat_log)

            # add our new message to the message list
            messages.insert(0, {'content': incoming_msg})
            messages.insert(0, {'content': bot_answer})

            # refresh the page with our updated messages
            return redirect(url_for('index'))

    return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.run()
