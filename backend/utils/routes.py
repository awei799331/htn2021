import requests
import json

from requests import api
# AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk
route_api = 'https://maps.googleapis.com/maps/api/directions/json?origin=351+Tealby+Cres&destination=362+King+St+N&mode=walking&key=AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk'
# must use lat and longitude for location
find_locations = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk&location=43.490970,-80.523100&radius=1500&rankby=prominence'



def find_pois(api_key: str, lat: str, lon: str, dist: int) -> dict:
  payload = {}
  headers = {}
  url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={api_key}&location={lat},{lon}&radius={dist}&rankby=prominence'
  response = requests.request("GET", url, headers=headers, data=payload)
  return response.json()

def find_relevant_pois(api_key: str, pois: dict, lat: str, lon: str, dist: int) -> list:
  current_loc = f"{lat}%2C{lon}"
  place_ids = [current_loc]
  for poi in pois["results"]:
    if "business_status" not in poi:
      continue
    place_ids.append(f"place_id:{poi['place_id']}")

  #truncate places
  place_ids = place_ids[0:7]
  
  payload = {}
  headers = {}
  url = f'https://maps.googleapis.com/maps/api/distancematrix/json?key={api_key}&origins={"%7C".join(place_ids)}&destinations={"%7C".join(place_ids)}&mode=walking'
  response = requests.request("GET", url, headers=headers, data=payload)
  return response.json()
  
def find_relevant_path(dist_mat: dict, metric_size: int, dist_over_time: bool = True, greater_than_threshhold: float = 2.0, top_k: int = 5) -> list:
  if dist_over_time:
    metric = "distance"
  else:
    metric = "duration"
  nodes = {i: dist_mat["destination_addresses"][i] for i in range(len(dist_mat["destination_addresses"]))}
  graph = [[element for element in row["elements"]] for row in dist_mat["rows"]]

  paths = [
    {"cum_metric": graph[0][i][metric]["value"], "path": [0, i], "unvisited": [j for j in range(0, len(nodes)) if i != j]} 
    for i in range(1, len(nodes)) if graph[0][i]["status"] == "OK"]
  completed_paths = []

  # store paths in list format, keeping track of current cumulative metric, and nodes visited
  while paths:
    current_path = paths.pop()
    for unvisited_node in current_path["unvisited"]:
      if graph[current_path["path"][-1]][unvisited_node]["status"] != "OK":
        continue
      cum_metric = current_path["cum_metric"] + graph[current_path["path"][-1]][unvisited_node][metric]["value"]
      if cum_metric > metric_size * greater_than_threshhold:
        continue
      new_path = {
        "cum_metric": cum_metric,
        "path": current_path["path"] + [unvisited_node],
        "unvisited": [j for j in range(0, len(nodes)) if j not in current_path["path"] + [unvisited_node] or j == 0]
      }
      if unvisited_node == 0:
        completed_paths.append(new_path)
        continue
      paths.append(new_path)
  
  pot_paths = [[path["cum_metric"], [nodes[location] for location in path["path"]]] for path in completed_paths]
  pot_paths.sort(key=lambda x: x[0])
  return findClosestElements(pot_paths, top_k, metric_size)

def find_route(api_key: str, loc_list: list):
  payload = {}
  headers = {}
  url = f'https://maps.googleapis.com/maps/api/directions/json?key={api_key}&mode=walking&origin={loc_list[0].replace(" ", "+")}&destination={loc_list[0].replace(" ", "+")}&waypoints={"|".join(loc_list[1:-1]).replace(" ", "+")}'
  response = requests.request("GET", url, headers=headers, data=payload)
  return response.json()

def find_route_url(api_key: str, loc_list: list):

  return f'https://maps.googleapis.com/maps/api/directions/json?key={api_key}&mode=walking&origin={loc_list[0].replace(" ", "+")}&destination={loc_list[0].replace(" ", "+")}&waypoints={"|".join(loc_list[1:-1]).replace(" ", "+")}'

def findClosestElements(arr: list, k: int, x: int) -> list:
  left = 0
  right = len(arr) - 1
  
  while right - left >= k:
      if abs(arr[left][0] - x) > abs(arr[right][0] - x):
          left += 1
      else:
          right -= 1
  
  return arr[left:right + 1]

if __name__ == "__main__":
  lat = "43.490970"
  lon = "-80.523100"
  api_key = "AIzaSyBqoTgyqFmFUpOn3neyDu5-1WinqTjRfmk"
  dist = "500"

  pois = find_pois(api_key=api_key, lat=lat, lon=lon, dist=dist)
  distance_matrix = find_relevant_pois(api_key=api_key, pois=pois, lat=lat, lon=lon, dist=dist)
  paths = find_relevant_path(distance_matrix, 3000, greater_than_threshhold=2, top_k=5)
  print(paths)
  joe = find_route(api_key, paths[0][1])
  
  with open("joe.json", "w") as f:
    json.dump(joe, f)
