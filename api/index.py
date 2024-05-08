from flask import Flask, render_template

static_path = '/static'
template_path = '/templates'

app = Flask(__name__, static_url_path=static_path, template_folder=template_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(500)
def internal_server_err(e):
    return "Internal Server Error (500) ", 500 
