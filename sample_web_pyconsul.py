from flask import Flask, request
import requests
#import json

app = Flask(__name__)


@app.route('/get_value', methods=['GET'])
def process_get_value():
    get_value = requests.get(f"http://consul-server:8500/v1/kv/{request.args.get('key')}?raw")
    return get_value.text


@app.route('/set_value', methods=['POST', 'PUT'])
def process_set_value():
    for key, value in request.args.items():
        uri =  requests.put(f"http://consul-server:8500/v1/kv/{key}", data=value)
    return uri.text
