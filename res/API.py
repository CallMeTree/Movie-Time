import requests
from requests.exceptions import ConnectionError

title = 'sdfsdf'
api_url = 'http://www.omdbapi.com/?apikey=b49eb448&t={}'.format(title)
try:
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        print(response.json())
    else:
        print("Error:", response.status_code, response.text)
except ConnectionError as e:
    print("Bruh")
    response = "No response"
