import os
import openai
from dotenv import load_dotenv
from random import choice

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

initiate="""Helper is a therapist who employs cognitive behavioural therapy - or CBT - approaches.

Helper is friendly, helpful, non-judgemental, and optimistic. Most of Helper's patients experience conditions
like anxiety, depression, grief, and low self-esteem. Helper listens to the things people say, and asks whether
people's interpretations could be framed more positively.

Person:"""

def gpt3(prompt, engine='davinci', response_length=50,
         temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):

    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']

    # update what our chat_history says and return it to our session
    #global chat_log
    #chat_log = prompt + start_text + answer + restart_text

    return answer

def update_log(question, answer, log=None):
    global initiate

    if log is None:
        log = initiate

    return f'{log}\nPerson: {question}\nHelper: {answer}'

def ask(question, log=None):
    global initiate

    if log is None:
        log = initiate

    print("IN ASK")
    sys.stdout.flush()
    log = log + '\nPerson: '+question;
    answer = gpt3(log,temperature=0.9,frequency_penalty=1,presence_penalty=1,start_text='\nHelper:',restart_text='\nPerson: ',stop_seq=['\nPerson:', '\n'])

    return answer
