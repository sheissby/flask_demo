# encoding: utf-8
from flask import Flask, render_template, redirect, url_for
from flask import request

app = Flask(__name__)

@app.route('/login.html', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print username, password
        if username == '1' and password == '1':
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()