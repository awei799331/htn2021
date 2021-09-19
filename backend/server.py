from json import dumps
import math

import requests
from requests import api
from requests.api import get
from dotenv import dotenv_values
from flask import Flask, Response, request, render_template, session, redirect, flash, url_for, Markup,
from flask_cors import CORS, cross_origin
import random

from Cachexplorer.Cachexplorer import cachexplorer

from utils.routes import find_url, get_streetview

CONFIG = dotenv_values('.env')
API_KEY = CONFIG['API_KEY']

app = Flask(__name__)

#probably have to replace relative path to crt with direct path
conn_string = r'cockroachdb://dan:1TMINz3aSHskuiZe@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/cachexplorer?sslmode=verify-full&sslrootcert=$env:appdata\.postgresql\root.crt&options=--cluster%3Dgifted-marmot-3567'
cachexplorer = cachexplorer(conn_string)

cors = CORS(app, resources={r"/*": {"origins": "http://localhost"}})
app.config['CORS_HEADERS'] = ['Content-Type', 'Authorization']

@app.route('/get-route', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*')
def get_route():
  data = request.json
  run_length = data['length'] * 1000 #km
  start_latitude = data['latitude']
  start_longitude = data['longitude']
  # pois = data['pois']
  pois = 3
  max_distance_of_poi = run_length * pois

  # make a route and find the embedding url for it
  url, joe = find_url(API_KEY, start_latitude, start_longitude, max_distance_of_poi, run_length)

  routes = joe["routes"][0]
  legs = routes["legs"]
  legs = random.sample(legs, 3)
  steps = [random.choice(leg["steps"]) for leg in legs]
  loc = [e["end_location"] for e in steps]
  
  imgs = [get_streetview(API_KEY, e["lat"], e["lng"]) for e in loc]

  return Response(dumps({
    "path_url": url,
    "img_url": imgs
  }), status=200, mimetype='application/json')


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
