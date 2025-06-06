#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    [
  {
    "baked_goods": [
      {
        "bakery_id": 1,
        "created_at": "2023-11-03 16:11:18",
        "id": 1,
        "name": "Chocolate dipped donut",
        "price": 2.75,
        "updated_at": null
      },
      {
        "bakery_id": 1,
        "created_at": "2023-11-03 16:11:18",
        "id": 2,
        "name": "Apple-spice filled donut",
        "price": 3.5,
        "updated_at": null
      }
    ],
    "created_at": "2023-11-03 16:11:18",
    "id": 1,
    "name": "Delightful donuts",
    "updated_at": null
  },
  {
    "baked_goods": [
      {
        "bakery_id": 2,
        "created_at": "2023-11-03 16:11:18",
        "id": 3,
        "name": "Glazed honey cruller",
        "price": 3.25,
        "updated_at": null
      },
      {
        "bakery_id": 2,
        "created_at": "2023-11-03 16:11:18",
        "id": 4,
        "name": "Chocolate cruller",
        "price": 100,
        "updated_at": "2023-11-03 16:11:18"
      }
    ],
    "created_at": "2023-11-03 16:11:18",
    "id": 2,
    "name": "Incredible crullers",
    "updated_at": null
  }
]
    return ''

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    {
  "baked_goods": [
    {
      "bakery_id": 1,
      "created_at": "2023-11-03 16:11:18",
      "id": 1,
      "name": "Chocolate dipped donut",
      "price": 2.75,
      "updated_at": null
    },
    {
      "bakery_id": 1,
      "created_at": "2023-11-03 16:11:18",
      "id": 2,
      "name": "Apple-spice filled donut",
      "price": 3.5,
      "updated_at": null
    }
  ],
  "created_at": "2023-11-03 16:11:18",
  "id": 1,
  "name": "Delightful donuts",
  "updated_at": null
}
    return ''

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    [
  {
    "bakery": {
      "created_at": "2023-11-03 16:31:32",
      "id": 1,
      "name": "Delightful donuts",
      "updated_at": null
    },
    "bakery_id": 1,
    "created_at": "2023-11-03 16:31:32",
    "id": 2,
    "name": "Apple-spice filled donut",
    "price": 3.5,
    "updated_at": null
  },
  {
    "bakery": {
      "created_at": "2023-11-03 16:31:32",
      "id": 2,
      "name": "Incredible crullers",
      "updated_at": null
    },
    "bakery_id": 2,
    "created_at": "2023-11-03 16:31:32",
    "id": 4,
    "name": "Chocolate cruller",
    "price": 3.4,
    "updated_at": null
  },
  {
    "bakery": {
      "created_at": "2023-11-03 16:31:32",
      "id": 2,
      "name": "Incredible crullers",
      "updated_at": null
    },
    "bakery_id": 2,
    "created_at": "2023-11-03 16:31:32",
    "id": 3,
    "name": "Glazed honey cruller",
    "price": 3.25,
    "updated_at": null
  },
  {
    "bakery": {
      "created_at": "2023-11-03 16:31:32",
      "id": 1,
      "name": "Delightful donuts",
      "updated_at": null
    },
    "bakery_id": 1,
    "created_at": "2023-11-03 16:31:32",
    "id": 1,
    "name": "Chocolate dipped donut",
    "price": 2.75,
    "updated_at": null
  }
]
    return ''

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    {
  "bakery": {
    "created_at": "2023-11-03 16:16:21",
    "id": 1,
    "name": "Delightful donuts",
    "updated_at": null
  },
  "bakery_id": 1,
  "created_at": "2023-11-03 16:16:21",
  "id": 2,
  "name": "Apple-spice filled donut",
  "price": 3.5,
  "updated_at": null
}
    return ''

if __name__ == '__main__':
    app.run(port=5555, debug=True)
