from flask import Flask, render_template, redirect, request, session, url_for, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CampF1Game2025'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/logarSite', methods=['POST'])
def login():
    emailLogar = request.form.get('emailCamp')
    senhaLogar = request.form.get('senhaCamp')
    return render_template('login.html')

@app.route('/bntCadastrar')
def rotaBntCadastrar():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)