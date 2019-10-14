import json

# loading json obj from a separate file
with open('states.json') as file:
    data = json.load(file)

# printing states names
for state in data['states']:
    print(state['name'])

# deleting area codes
for state in data['states']:
    del state['area_codes']

# writing new json obj to a new json file
with open('new_states.json', 'w') as new_file:
    json.dump(data, new_file, indent=2)




