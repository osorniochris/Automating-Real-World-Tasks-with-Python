#! /usr/bin/env python3

import os
import requests

path = "/data/feedback/"
IP = "34.122.34.64"

files = os.listdir(path)

for f in files:
  data = {}
  with open(os.path.join(path, f)) as fd:
    lines = fd.readlines()

    data = { 'title': lines[0], 'name': lines[1], 'date' : lines[2], 'feedback': lines[3] }

  response = requests.post('http://{}/feedback/'.format(IP), json = data)
  print("Response code in {}: {}".format(f, response.status_code))
