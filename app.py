# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template
from helper import help

app = Flask(__name__)

anchor = '<!-- output anchor -->'

@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    params = text.split(" ")
    if len(params) < 4:
        processed_text = "INVALID INPUT"
    if len(params) == 4:
        processed_text =help(params[0], params[1], params[2], params[3], None)
    if len(params) > 4:
        processed_text =help(params[0], params[1], params[2], params[3], params[4])

    response_text = f'<p>{processed_text}</p>'

    return render_template('my-form.html').replace(anchor, response_text)
