from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html',name=name)

@app.route('/say_hello')
def say_hello():
    return render_template('say_hello.html')

@app.route('/say_hello', method='post')
def say_hello_post():
    name = request.form['text']
    return hello(name)


app.run(debug=True)