from flask import Flask, jsonify
from flask_cors import CORS
import sys
import re

# A good guide on getting data from my data:
# https://roadfiresoftware.com/2016/12/how-to-parse-json-with-swift-3/

SHOPS = [
    {
    'ID': 'courant_Deli',
    'store_Longtitude': '-73.9957',
    'store_Latitude': '+40.7287',
    'store_Name': 'Courant Deli',
    'address': '251 Mercer St, New York, NY 10012',
    'Food':
        [{
            'name': 'BLT Sandwich',
            'price': '3.49',
            'store_ID': 'courant_Deli',
            'image': 'blt_sandwich_0',
            'picture': 'https://assets.marthastewart.com/styles/wmax-1500/d28/perfect-blt-sandwich-mscs107/perfect-blt-sandwich-mscs107_horiz.jpg?itok=I4oSSmei',
        },
        {
            'name': 'PBJ Sandwich',
            'price': '2.29',
            'store_ID': 'courant_Deli',
            'image': 'pbj_sandwich_1',
            'picture': 'https://cdn-image.myrecipes.com/sites/default/files/styles/4_3_horizontal_-_1200x900/public/mr-grilled-peanut-butter-jelly-sandwich.jpg?itok=2_kP_HET',
        },
        {
            'name': 'Turkey Club',
            'price': '5.59',
            'store_ID': 'courant_Deli',
            'image': 'turkey_club_2',
            'picture': 'https://d5dnlg5k9nac9.cloudfront.net/processed/thumbs/cd6e29f04c23bcdae0ff7acc734c544ea1a0a318_r791_530.png',
        }],
    'Drinks':
        [{
            'name': 'Coffee',
            'price': '1.50',
            'store_ID': 'courant_Deli',
            'image': 'coffee_3',
            'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/1200px-A_small_cup_of_coffee.JPG',
        },
        {
            'name': 'Mango Smoothie',
            'price': '7.39',
            'store_ID': 'courant_Deli',
            'image': 'mango_smoothie_4',
            'picture': 'https://silk.com/sites/default/files/recipes/medium/CarrotMango_1146X860.png',
        },
        {
            'name': 'Tea',
            'price': '1.00',
            'store_ID': 'courant_Deli',
            'image': 'tea_5',
            'picture': 'https://cms.splendidtable.org/sites/default/files/styles/w2000/public/cedar-tea_by_Mette-Nielsen-LEDE.jpg?itok=P-UvOBBE',
        }],
    },
    {
    'ID': 'silver_Deli',
    'store_Longtitude': '-73.9953',
    'store_Latitude': '+40.7307',
    'store_Name': 'Silver Deli',
    'address': '31 Waverly Pl, New York, NY 10003',
    'Food':
        [{
            'name': 'BLT Sandwich',
            'price': '3.59',
            'store_ID': 'silver_Deli',
            'image': 'blt_sandwich_6',
            'picture': 'https://assets.marthastewart.com/styles/wmax-1500/d28/perfect-blt-sandwich-mscs107/perfect-blt-sandwich-mscs107_horiz.jpg?itok=I4oSSmei',
        },
        {
            'name': 'Cheese Steak Sandwich',
            'price': '6.99',
            'store_ID': 'silver_Deli',
            'image': 'cheese_steak_sandwich_7',
            'picture': 'https://assets.kraftfoods.com/recipe_images/opendeploy/174511_640x428.jpg',
        },
        {
            'name': 'Grilled Chicken Sandwich',
            'price': '7.59',
            'store_ID': 'silver_Deli',
            'image': 'chicken_sandwich_8',
            'picture': 'https://www.goldnplump.com/sites/default/files/Grilled%20Mesquite%20Chicken%20Sandwich-0268.JPG',
        }],
    'Drinks':
        [{
            'name': 'Water Bottle',
            'price': '0.99',
            'store_ID': 'silver_Deli',
            'image': 'waterbottles_9',
            'picture': 'https://www.factsaboutbpa.org/sites/default/files/images/waterbottles.png',
        },
        {
            'name': 'Orange Juice',
            'price': '4.39',
            'store_ID': 'silver_Deli',
            'image': 'orangejuice_10',
            'picture': 'https://www.organicfacts.net/wp-content/uploads/orangejuice.jpg',
        },
        {
            'name': 'Tea',
            'price': '1.09',
            'store_ID': 'silver_Deli',
            'image': 'tea_11',
            'picture': 'https://cms.splendidtable.org/sites/default/files/styles/w2000/public/cedar-tea_by_Mette-Nielsen-LEDE.jpg?itok=P-UvOBBE',
        }],
    },

    ]

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
    return jsonify(SHOPS)

if __name__ == '__main__':
    app.run()
