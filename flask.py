from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
    return 'Esta é minha HomePage. 😋'

@app.route('/contatos')
def contatos():
    return 'Aqui está minha lista de contatos.'

app.run()
