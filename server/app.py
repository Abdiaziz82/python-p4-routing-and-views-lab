#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print in the console
    return parameter  # Return the plain string without HTML tags

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate a string with each number in range on a new line, including a trailing newline
    result = "\n".join(str(i) for i in range(parameter)) + "\n"
    # Return the result as plain text
    return result, 200, {'Content-Type': 'text/plain'}


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Perform floating-point division
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
