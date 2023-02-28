from flask import Flask, request, render_template

app = Flask(__name__)

contacts = [{'id': 1, 'name': 'John Doe',  'phone': '555-555-5555'},
            {'id': 2, 'name': 'João Ponez',  'phone': '4444-444-444'}]

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html',name=name)

@app.route('/say_hello')
def say_hello():
    return render_template('say_hello.html')

@app.route('/say_hello', methods=['post'])
def say_hello_post():
    name = request.form['text']
    return hello(name)


@app.route('/contactsTemplate.html')
def contact_template():
    return render_template('contactsTemplate.html' ,contacts=contacts)

@app.route('/dict')
def dict():
    my_dict = {'name':'banana', 'quantidade' : 10}
    return render_template('dict.html', item = my_dict)

@app.route('/list')
def list():
    my_list = [{'name':'banana', 'price':10},
               {'name':'Omo', 'price':1},
               {'name':'Nescau', 'price':2},
               {'name':'picanha', 'price':20}]
    return render_template('list.html', list=my_list)

app.run(debug=True)