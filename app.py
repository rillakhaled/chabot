from flask import Flask, render_template, request, url_for, flash, redirect, session
from gptqueries import ask, update_log
from random import random
import sys
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
messages = []
counter = 1

@app.route('/', methods=('GET', 'POST'))
def index():

    # obtain chat_log
    chat_log = session.get('chat_log')
    session.pop('chat_log', None)

    if request.method == 'GET':
        # This seems to run just as often as POST
        # updateMessage = "HELLO" + counter
        # flash(updateMessage)
        # counter = counter+1
        message = "I am {}".format(random())
        flash(message)
        print("hei")
        sys.stdout.flush()

        # Trying gunicorn
        app.logger.debug('this is a DEBUG message')


    if request.method == 'POST':
        incoming_msg = request.form['content']

        if not incoming_msg:
            flash('Content is required!')

        else:
            # add our new message to the message list
            # messages.insert(0, {'content': incoming_msg})

            messages.append({'content': incoming_msg})

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
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run()
