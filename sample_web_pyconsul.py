from flask import Flask, request
import requests
#import json

app = Flask(__name__)


@app.route('/get_value', methods=['GET'])
def process_get_value():
    get_value = requests.get("http://172.21.0.2:8500/v1/kv/" + request.args.get('key') + "?raw")
    return get_value.text


@app.route('/set_value', methods=['POST', 'PUT'])
def process_set_value():
    ## TODO send post
