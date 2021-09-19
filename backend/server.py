import math

import requests
from dotenv import dotenv_values
from flask import Flask, Response, request
from flask_cors import CORS

from utils.routes import find_pois

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
  pois = data['pois']

  max_distance_of_poi = int(math.ceil((run_length*1000/pois) / 500) * 500) #m
  found_locations = find_pois(API_KEY, start_latitude, start_longitude)


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
