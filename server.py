from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/io', methods=['POST'])
def io_test():
    filename = 'test.txt'
    content = request.form.get('content')

    with open(filename, 'w') as f:
        f.write(content)

    with open(filename, 'r') as f:
        result = f.read()

    os.remove(filename)
    return jsonify({'result': result})


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.route('/calculation', methods=['GET'])
def calculation_test():
    n = int(request.args.get('n', 10))
    result = fibonacci(n)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
