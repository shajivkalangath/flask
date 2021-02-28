#!/usr/bin/env python

from flask import Flask 
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vxvmcheck')
def vxvmcheck():
    return render_template('vxvmcheck.html')

@app.route('/vcscheck')
def vcscheck():
    return render_template('vcscheck.html')

@app.route('/oscheck')
def oscheck():
    return render_template('oscheck.html')

@app.route('/veritasversioncheck')
def veritasversioncheck():
    return render_template('veritasversioncheck.html')

if __name__ == '__main__':
    app.run(debug=True)
