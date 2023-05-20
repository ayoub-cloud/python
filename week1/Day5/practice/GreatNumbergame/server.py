from flask import Flask, render_template, session, redirect, request, url_for
import random

app = Flask(__name__)
app.secret_key="my Secret_key"

@app.route('/')
def index():
    if "final_number" not in session:
        session['final_number'] = random.randint(1, 100)
    print(session['final_number'])
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    session["guess"] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)