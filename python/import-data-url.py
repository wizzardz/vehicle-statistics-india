import urllib.request
import json
import sys
import os

data = ''

url = sys.argv[1]
output_folder = sys.argv[2]
file_name = sys.argv[3]

with urllib.request.urlopen(url) as response:
  data = response.read().decode('utf-8')

index = 1
filename = output_folder + '/' + file_name + '.json'
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as output_file:
  output_file.write(data)
