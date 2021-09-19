import requests
# AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk
route_api = 'https://maps.googleapis.com/maps/api/directions/json?origin=351+Tealby+Cres&destination=362+King+St+N&mode=walking&key=AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk'
# must use lat and longitude for location
find_locations = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk&location=43.490970,-80.523100&radius=1500&rankby=prominence'



def find_pois(api_key: str, lat: str, lon: str, dist: int) -> dict:
  payload = {}
  headers = {}
  url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={api_key}&location={lat},{lon}&radius={dist}&rankby=prominence'
  response = requests.request("GET", url, headers=headers, data=payload)
  # print(response.text)
  response.json()


