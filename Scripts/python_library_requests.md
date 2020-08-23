
LINKS:
Blog: https://blog.jamesfheath.com/2020/08/python-library-requests.html
Code: https://github.com/JamesFHeath/jamesfheathblog_code/blob/master/Python%20Libraries/requests.py
Requests Site: https://requests.readthedocs.io/en/master/
Weather API: https://www.weather.gov/documentation/services-web-api

# Intro
Hi Everyone, SearingFrost here in the Python library.
Today, we're going to check out the requests library. 
Requests is a fantastic open-source library for sending HTTP requests. 
Requests abstracts away the details and complications of the standard libary urllib module
Requests can be installed with **pip install requests**.
Here's a list of the HTTP methods and their requests equivalents.
You'll see that it's a fairly straightforward relationship. 

| HTTP Method | requests |
|:------|:--------|
| GET | requests.get(url, params=None, **kwargs) |
| POST | requests.post(url, data=None, json=None, **kwargs) |
| OPTIONS | requests.options(url, **kwargs) |
| HEAD | requests.head(url, **kwargs) |
| PUT | requests.put(url, data=None, **kwargs) |
| DELETE | requests.delete(url, **kwargs) |
| PATCH | requests.patch(url, data=None, **kwargs) |

### Simple Get Request
To see how easy using requests is, let's just make a get request for the James Heath Blog. 
First we need to import requests.
We'll set the blog url to a string.
Then set the get request to a response object.
The status code is available, and luckily it is a 200 success code.
We can see the HTML string with response.text

import requests

blog_url = 'https://blog.jamesfheath.com'

response = requests.get(blog_url)

response.status_code

response.text

response.content

### National Weather Service API
Requests is great for communicating with APIs. 
Let's try out some requests with query parameters and headers. 
The National Weather Service has an open API that we can use to test requests out. 
The API is linked in the video description
Once again we import requests.
And set the url to the API
We're going to specifically loiok at the stations URL to get a list of weather stations.
The header is going to contain a User-Agent, used to identify who is making the request.
This API currently doesn't have authentication requirements. 
For the parameters, we're going to ask for up to 10 weather stations in either north carolina or virginia. 
We just need to pass all of this to our get request. 
We check that the status code is success
A great thing about the requests library is we can get JSON responses as Python dictionaries using the json method.
Now we can just operate on the json like a python dictionary and get the name of a weather station.

import requests

weather_url = 'https://api.weather.gov'
stations_url = f'{weather_url}/stations'

headers = {'User-Agent': '(jamesfheath.com, jamesheathradford@gmail.com)'}

params = {'state': ['NC', 'VA'],
          'limit': 10}

response = requests.get(url=station_url, headers=headers, params=params)

response.status_code

response.json()

response.json()['features'][1]['properties']['name']


# Thanks for Watching
Thanks for joining me in the python library to talk about requests.
There are other parameters you can specify and pass in to your HTTP request. 
Some common examples are **timeout** and **authorization**. 
Mostly, requests just works exactly how you hope it would, and it makes your life dealing with HTTP simple. 
Links to my blog post on the requests library and the video code are in the description. 
I'll see everyone next time. 