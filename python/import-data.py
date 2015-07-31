import json
import pprint
import sys
import os
import re
import copy

# this script will try to convert the raw data avaliable from data.gov.in
# website to a more meaning full data format for processing

# initialises the object for storing the transport statistic data for a state


def initalise_data(state_name):
  json_string = json.dumps({"TransportType": "", "Category": "", "State": state_name,
                            "VehicleType": "", "Period": "", "NewCount": "", "TotalCount": ""})
  return json.loads(json_string)

# creates a new copy of specified object and update the value of 'period'


def copy_data(data_object, period):
  new_copy = copy.deepcopy(data_object)
  new_copy["Period"] = period
  return new_copy

# initialise the root folder for processing the data
root_folder = ""

# verify whether a root folder is already passed as a command line argument
if not len(sys.argv) > 1:
  # no command line arguments are passed, so take the current node as the
  # root folder
  root_folder = os.path.dirname(os.path.realpath(__file__))

# need to get these folder name programatically
state_folders = ["Andhra Pradesh", "Arunachal Pradesh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka",
                 "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab",
                 "Andaman and Nicobar Islands", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Dadra And Nagar Haveli", "Daman and Diu", "Delhi",
                 "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

# initialise the list for saving the data
data_set = []  # json.dumps([])

# declare a constant variable that corresponds to the index where the
# actual count starts
DATA_START_INDEX = 3

# iterates through all the state folders and read the raw data files
for states in state_folders:
  # get all the json files in the current state folder
  files = os.listdir(os.path.join(root_folder, states))

  # start processing each json files
  for f in files:
    # construct the json file path
    json_file = os.path.join(root_folder, states, f)

    # load the json file for reading
    with open(json_file) as file_pointer:
      json_data = json.load(file_pointer)

      # get the count of number of fields in the raw data
      field_count = len(json_data["fields"])

      # regx for matching the strings of pattern 'Newly registered-2006-07';
      # this is for extracting the period value
      new_vehicle_pattern = re.compile("\d{4}-\d{2}")

      """" The raw data may contain the statistics of more than a single year, the data is of the following format
       ["TransportType","Vehicle Category","Vehicle Type","New registrations in year - 1","New registrations in year - 2"..."New registrations in year - N",
       "Total registrated as on year - 1","Total registrated as on year - 2"..."Total registrated as on year - N"]
      """"

      # initialise the index variable for getting the details of newly
      # regsiterd vehicle details
      index = DATA_START_INDEX

      # the variable for calculating the offset index for getting the total
      # vehicles registered for the specified year
      offset_index = 0

      # get the details of the fields
      field_data = json_data["fields"]

      # iterates through filed data till the end of field data or the pattern
      # is matched
      while index < field_count and new_vehicle_pattern.search(field_data[index]["label"]):
        offset_index += 1
        index += 1

      # iterats through the raw data for conversion
      for vechile_data in json_data["data"]:

        # skip the data with total values, we will calculate it programatically
        if not vechile_data[1].startswith("Total"):

          # get the new json object data and fillin the common properties
          new_data = initalise_data(states)
          new_data["TransportType"] = vechile_data[0]
          new_data["Category"] = vechile_data[1]
          new_data["VehicleType"] = vechile_data[2]

          # now start filling the details of vehicle
          for data_index in range(DATA_START_INDEX, field_count - offset_index):
            vechile_stat_data = copy_data(
                new_data, new_vehicle_pattern.search(field_data[data_index]["label"]).group())
            vechile_stat_data["NewCount"] = vechile_data[data_index]
            vechile_stat_data["TotalCount"] = vechile_data[
                data_index + offset_index]
            data_set.append(vechile_stat_data)

# finally write the dataset to a file
with open("output/dataset.json", "a") as dataset_file:
  dataset_file.write(str(data_set))

print("The data conversion has been finished")
