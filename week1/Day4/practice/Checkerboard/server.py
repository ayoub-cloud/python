from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html', col=4, row=8, color1='black', color2='red')



@app.route('/<int:y>')
def set_row(y):
    return render_template('index.html', col=4, row=y, color1='black', color2='red')


@app.route('/<int:x>/<int:y>')
def set_col_row(x, y):
    return render_template('index.html', col=x, row=y, color1='black', color2='red')


@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def set_all(x, y, color1, color2):
    return render_template('index.html', col=x, row=y, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)