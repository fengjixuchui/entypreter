from flask import Flask
import os

app = Flask(__name__)

def is_keyword(os):
    print(os)

@app.route('/')
def index():
    text = open('index.html').read()
    return text
    
@app.route('/js/')
def js():
    return "protonscript.js\nmode-proton.js"

@app.route('/css/')
def css():
    return "style.css"

@app.route('/html/')
def html():
    return "index.html"

@app.route('/css/style.css')
def style():
    return open('css/style.css').read()

@app.route('/js/protonscript.js')
def protonscript():
    return open('js/protonscript.js').read()

@app.route('/js/mode-proton.js')
def mode_proton():
    return open('js/mode-proton.js').read()

if __name__ == '__main__':
    os.system("python urlloop.py")
    app.run(debug=False)
