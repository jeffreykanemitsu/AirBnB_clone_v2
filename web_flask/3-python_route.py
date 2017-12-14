#!/usr/bin/python3
'''
starts a Flask web application
'''


from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
