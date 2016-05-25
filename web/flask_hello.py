#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/sign', methods=['GET'])
def sign_form():
    return render_template('form.html')


@app.route('/sign', methods=['POST'])
def sign():
    username = request.form['username']
    pwd = request.form['password']
    if username == 'admin' and pwd == 'password':
        return render_template('sign_ok.html', username=username)

    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()

