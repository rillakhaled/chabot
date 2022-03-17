from flask import Flask, render_template, request, url_for, flash, redirect, session
from gptqueries import ask
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloeiwur92843uqghvnefjancwqefjfjewngvve'
messages = []

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        incoming_msg = request.form['content']
        if not incoming_msg:
            flash('Content is required!')
        else:
            messages.insert(0, {'content': incoming_msg})
            bot_answer = ask(incoming_msg)
            messages.insert(0, {'content': bot_answer})
            return redirect(url_for('index'))

    return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.run()
