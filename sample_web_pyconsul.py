from flask import Flask, request
app = Flask(__name__)


@app.route('/get_value', methods=['GET'])
def process_get_value():
    if not request.args:
        return 'No keys specified', 400

    key_name = list(request.args)[0]
    # TODO: Get from Consul
    return f'{key_name}\n'


@app.route('/set_value', methods=['POST', 'PUT'])
def process_set_value():
    if not request.args:
        return 'No keys specified', 400

    key_name, value = [(k, v) for k, v in request.args.items()][0]
    # TODO: Set to Consul
    return f'SET: {key_name} : {value}\n'