import requests

blog_url = 'https://blog.jamesfheath.com'
# Response object contains all you need
response = requests.get(blog_url)

print(response.status_code)
# 200

# String of the HTML
print(response.text)
# '<!DOCTYPE html>\n<html lang="en">\n\n<link re...'

# Prints out the raw HTML bytes
print(response.content)
# b'<!DOCTYPE html>\n<html lang="en">\n\n<link re...'



weather_url = 'https://api.weather.gov'
# We will ask for a list of weather stations
stations_url = f'{weather_url}/stations'

# Header to give our identity
headers = {'User-Agent': '(jamesfheath.com, jamesheathradford@gmail.com)'}

# Asking for 10 stations from North Carolina or Virginia
params = {'state': ['NC', 'VA'],
          'limit': 10}

response = requests.get(url=station_url, headers=headers, params=params)

# JSON response as a Python dict
print(response.json())
# {'@context': ['https://geojson.org/geojson-ld/geojson-context.jsonld',
#  {'@version': '1.1',}
# ...

# Use Python syntax to operate on the dict
print(response.json()['features'][1]['properties']['name'])
# 'KG4EUF Virginia Beach'

# String response
print(response.text)
# '{\n    "@context": [\n        "https://geojson.org/geojson-ld/geojson-context.jsonld",\n 