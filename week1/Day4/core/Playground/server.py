# playground_server

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', times=3) 

@app.route('/play/<int:num>')
def mult_boxes(num):
    return render_template('index.html', times=num) 

@app.route('/play/<int:num>/<color_change>') 
def color_change(num, color_change):
   return render_template('index.html', times=num, color=color_change)

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No Response. Please redirect to "/play"'

if __name__=="__main__":
    app.run(debug=True)