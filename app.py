from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this should be a secret random string'

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
