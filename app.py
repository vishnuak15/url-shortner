from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name='home')

@app.route('/about')
def about():
    return "This is a Url shortner"