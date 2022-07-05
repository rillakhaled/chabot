from flask import Flask, render_template, request, url_for, flash, redirect, session
from gptqueries import ask, update_log
from random import random
import sys
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
messages = []
# print("Clearing the session...")
# sys.stdout.flush();

@app.route('/', methods=('GET', 'POST'))
def index():
    # if request.method == 'GET':
        # This proves that GET runs on every page load sadly
        # message = "I am {}".format(random())
        # flash(message)

    if request.method == 'POST':
        incoming_msg = request.form['content']
        print("INCOMING MSG:" + incoming_msg)
        sys.stdout.flush();

        if not incoming_msg:
            flash('Content is required!')

        else:
            # add our new message to the message list
            messages.append({'content': incoming_msg})

            # obtain chat_log
            chat_log = session.get('chat_log')
            session.pop('chat_log', None);

            # This allows us to write to the web log, which may help
            if chat_log:
                print("CHATLOG: "+chat_log)
                sys.stdout.flush()
            else:
                print("CHATLOG IS EMPTY")

            # obtain a response, update our session's chat_log
            bot_answer = ask(incoming_msg, chat_log)
            session['chat_log'] = update_log(incoming_msg, bot_answer, chat_log)

            # add our new message to the message list
            messages.append({'content': bot_answer})

            # refresh the page with our updated messages
            return redirect(url_for('index'))

    return render_template('index.html', messages=messages)

if __name__ == "__main__":
    app.debug = True
    app.run()
