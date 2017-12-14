#!/usr/bin/python3
'''
starts a Flask web application
'''


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    displays Hello HBNB!
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    displays HBNB
    '''
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_route():
    '''
    displays 'c' followed by the value of the text variable
    replace underscore symbols with space
    '''
    return 'C {:s}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text='is cool'):
    '''
    displays 'Python', followed by value of the text variable
    replace underscore symbols with space
    '''
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''
    displays 'n is a number' only if n is an int
    '''
    return '{:d} is a number'.format(num)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    displays HTML page only if n is an int
    '''
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
    displays HTML page only if n is int
    number: n is even|odd
    '''
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
