from flask import Flask, jsonify
from flask_cors import CORS

import sys

import re

SHOPS = [
    {
    'name': 'Deli 1',
    'address': '123 E10th St',
    }]



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/shops', methods=['GET'])
def all_classes():
    return jsonify({
        'status': 'success',
        'Shops': SHOPS,
        })


@app.route('/')
def root():
    return "root"

if __name__ == '__main__':
    app.run()
