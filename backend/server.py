import math

import requests
from requests import api
from requests.api import get
from dotenv import dotenv_values
from flask import Flask, Response, request
from flask_cors import CORS
import random

from utils.routes import find_url, get_streetview

CONFIG = dotenv_values('.env')
API_KEY = CONFIG['API_KEY']

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/get_route', methods='POST')
def get_route():
  data = request.json
  run_length = data['length'] #km
  start_latitude = data['latitude']
  start_longitude = data['longitude']
  # pois = data['pois']

  url, joe = find_url(API_KEY, start_latitude, start_longitude, run_length)

  routes = joe["routes"]
  legs = routes["legs"]
  leg = random.choice(legs)
  step = random.choice(leg["steps"])
  loc = step["end_location"]
  
  img = get_streetview(API_KEY, loc["lat"], loc["lng"])

  return {
    "path_url": url,
    "img_url": img
  }


@app.route('/', methods=['GET'])
def joe():
  return Response(
    'joe',
    status=200
  )

def main():
  app.run('0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
  main()
