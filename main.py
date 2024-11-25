from flask import Flask, render_template, redirect, request, session, url_for, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CampF1Game2025'



if __name__ == '__main__':
    app.run(debug=True)