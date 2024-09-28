import requests
from options import params

response = requests.get(url='https://opentdb.com/api.php?', params=params)
response.raise_for_status()
data = response.json()
questions = data['results']
