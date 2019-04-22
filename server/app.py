from flask import Flask, jsonify
from flask_cors import CORS
import sys
import re

# For Jimmy:
# A good guide on getting data from my data:
# https://roadfiresoftware.com/2016/12/how-to-parse-json-with-swift-3/

SHOPS = [
    {
    'ID': 'courant_Deli',
    'store_Longtitude': '12',
    'store_Latitude': '12',
    'store_Name': 'Courant Deli',
    'address': '251 Mercer St, New York, NY 10012',
    'Food': {
        'picture': 'food.jpg',
        'items': [{
            'name': 'BLT',
            'price': '3.50',
            },
            {
            'name': 'PBJ',
            'price': '2.20',
            },
            {
            'name': 'Turkey Club',
            'price': '5.50',
            }],
    },
    'Drinks': {
        'picture': 'drink.jpg',
        'items': [{
            'name': 'Coffee',
            'price': '1.50',
            },
            {
            'name': 'Mango Smoothie',
            'price': '7.30',
            },
            {
            'name': 'Tea',
            'price': '1.00',
            }],
    },
    }]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# @app.route('/shops', methods=['GET'])
# def all_classes():
#     return jsonify({
#         'status': 'success',
#         'Shops': SHOPS,
#         })


@app.route('/')
def root():
    return jsonify({
        'status': 'success',
        'Shops': SHOPS,
        })

if __name__ == '__main__':
    app.run()
