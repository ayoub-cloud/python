from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key="dfojr903j902jnroj3r0932ijk9"

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")

@app.route('/result')
def display_result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)


