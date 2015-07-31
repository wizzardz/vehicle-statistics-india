import urllib.request
import json
import sys
import os

# specify the url format for downloading the json data
url_format = 'https://data.gov.in/node/{0}/datastore/export/json'

years = [2011, 2009, 2006, 2004, 2002]
# default data for constructing the urls for each States and union teritories
json_string = json.dumps({
    "Data": [{
        "Andaman and Nicobar Islands": [89524, 100624, 100681, 100729, 100794]
    }, {
        "Chandigarh": [89529, 100629, 100682, 100730, 100795]
    }, {
        "Dadra And Nagar Haveli": [
            89531, 100626, 100683, 100731, 100796
        ]
    }, {
        "Daman and Diu": [89532, 100627, 100684, 100732, 100797]
    }, {
        "Delhi": [89533, 100628,
                  100685, 100733, 100798
                  ]
    }, {
        "Lakshadweep": [89539, 100629, 100686, 100734, 100799]
    }, {
        "Puducherry": [89546, 100630, 100687, 100735, 100800]
    }, {
        "Bihar": [89528, 100599, 100656, 100704, 100769]
    }, {
        "Chhattisgarh": [
            89530, 100600, 100657, 100705, 100770
        ]
    }, {
        "Goa": [89534, 100601, 100658, 100706, 100771]
    }, {
        "Gujarat": [89535, 100602, 100659, 100706, 100772]
    }, {
        "Haryana": [89536, 100603, 100660, 100708, 100773]
    }, {
        "Himachal Pradesh": [
            89537, 100604, 100661, 100709, 100774
        ]
    }, {
        "Jammu and Kashmir": [
            89555, 100605, 100662, 100710, 100775
        ]
    }, {
        "Jharkhand": [89556, 100606,
                      100663, 100711, 100776
                      ]
    }, {
        "Karnataka": [89557, 100607,
                      100664, 100712, 100777
                      ]
    }, {
        "Kerala": [89538, 100608, 100665, 100713, 100778]
    }, {
        "Madhya Pradesh": [
            89558, 100609, 100666, 100714, 100779
        ]
    }, {
        "Maharashtra": [89540, 100610,
                        100667, 100715, 100780
                        ]
    }, {
        "Manipur": [89541, 100611, 100668, 100716, 100781]
    }, {
        "Meghalaya": [89542, 100612,
                      100669, 100717, 100782
                      ]
    }, {
        "Mizoram": [89543, 100613, 100670, 100718, 100783]
    }, {
        "Nagaland": [89544, 100614, 100671, 100719, 100784]
    }, {
        "Odisha": [89545, 100615, 100672, 100720, 100785]
    }, {
        "Punjab": [89547, 100616, 100673, 100721, 100786]
    }, {
        "Rajasthan": [89548, 100617,
                      100674, 100722, 100787
                      ]
    }, {
        "Sikkim": [89549, 100618, 100675, 100723, 100788]
    }, {
        "Tamil Nadu": [89550, 100619,
                       100676, 100724, 100789
                       ]
    }, {
        "Tripura": [89551, 100620, 100677, 100725, 100790]
    }, {
        "Uttarakhand": [89553, 100621,
                        100678, 100726, 100791
                        ]
    }, {
        "Uttar Pradesh": [89552, 100622,
                          100679, 100727, 100792
                          ]
    }, {
        "West Bengal": [89554, 100623, 100680, 100728, 100793]
    }]
})

# loads the default data in josn format
state_data = json.loads(json_string)

# check whether an url data is specified through an input file, if thats
# the case then overwrite the default data by the input file
if len(sys.argv) > 1:
  with open(sys.argv[1], 'r') as json_file:
    state_data = json.loads(json_file.read())

failed_urls = ''
# iterates through each data for downloading the json content
for state in state_data["Data"]:

  # get the name of the state, ideally the key is same as that of
  # state/union teritory
  state_name = ''
  for key in state.keys():
    state_name = key

  # initialises the index for downloading the data
  index = 0

  # for a state, download the json data for each year
  for identifer in state[state_name]:
    url = url_format.format(identifer)

    try:
      downloaded_data = ''

      with urllib.request.urlopen(url) as response:
        downloaded_data = response.read().decode('utf-8')

      fille_name = '{0}/{1}.json'.format(state_name, years[index])
      os.makedirs(os.path.dirname(fille_name), exist_ok=True)

      with open(fille_name, "w") as output_file:
        output_file.write(downloaded_data)
      print(
          'Downloading completed for {0}-{1}'.format(state_name, str(years[index])))
      index += 1
    except Exception as e:
      failed_urls += "{0} - {1}\n".format(state_name, url)

if len(failed_urls) > 0:
  with open("failedurl.txt", 'w') as f:
    f.write(failed_urls)
  print('Failed url details has been written to failedurl.txt')
