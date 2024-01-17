import json

def open_json_file(file_path):
  with open(file_path) as json_file:
    data = json.load(json_file)
    return data

def merge_objects(obj1, obj2):
  merged_data = {}
  merged_data["id"] = obj1["id"]
  merged_data["count"] = round(obj1["count"] + obj2["count"], 2)
  merged_data["percentage_question"] = round(obj1["percentage_question"] + obj2["percentage_question"], 2)
  merged_data["percentage_survey"] = round(obj1["percentage_survey"] + obj2["percentage_survey"], 2)
  merged_data["entity"] = obj1["entity"]
  merged_data["entity"].update(obj2["entity"])  
  return merged_data

def find_object_by_id(objects, id):
  for obj in objects:
    if obj["id"] == id:
      return obj
  return None

file_path = 'debugging_and_profiling__debugging_and_profiling_problems_debugging_tools_other.json' # to trzeba zmienić
question_key = 'debugging_and_profiling_problems_debugging_tools_other' # i tu te to trzeba zmienić

json_data = open_json_file(file_path)
new_data = []
new_keys = []
current_data = json_data['dataAPI']['survey'][question_key]['all_years'][0]['facets'][0]['buckets']
keys = json_data['dataAPI']['survey'][question_key]['keys']
for group in keys:
  if type(group) == list:
    new_keys.append(group[0])
    merged_data = find_object_by_id(current_data, group[0])
    if merged_data == None:
      print(f'Could not find object with id {group[0]}')
      continue
    for i in range(1, len(group)):
      merged_data = merge_objects(merged_data, find_object_by_id(current_data, group[i]))
    if 'name' not in merged_data["entity"]:
      merged_data["entity"]["name"] = group[0]
      merged_data["entity"]["description"] = ""
      merged_data["entity"]["homepage"] = {
        "url": "",
      }
      merged_data["entity"]["github"] = {
        "url": "",
      }
      merged_data["entity"]["npm"] = {
        "url": "",
      }
    new_data.append(merged_data)
json_data['dataAPI']['survey'][question_key]['all_years'][0]['facets'][0]['buckets'] = new_data
json_data['dataAPI']['survey'][question_key]['keys'] = new_keys

name = file_path.split('.')[0]
with open(f'{name}_new.json', 'w') as outfile:
  json.dump(json_data, outfile, indent=2)
