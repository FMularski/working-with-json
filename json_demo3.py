import json
import requests

api_key = 'bd239ec2eb18419898bfd45653d24d2a'
url = 'https://api.spoonacular.com/recipes/search'
params = {'query': 'cheese', 'number': 2, 'apiKey': api_key}

respond = requests.get(url, params=params)

data = respond.json()

print(json.dumps(data, indent=2))
