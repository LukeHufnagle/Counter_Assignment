from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    if "refresh" in session:
        session['refresh'] += 1
        print(session['refresh'])
    else:
        session['refresh'] = 1
    return redirect('/')

@app.route('/addtwo', methods=['POST'])
def addtwo():
    if "refresh" in session:
        session['refresh'] += 2
        print(session['refresh'])
    else:
        session['refresh'] = 1
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)