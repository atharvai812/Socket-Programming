# Here we import the request library
import requests

# Here we define the api-endpoint 
url = "https://postman-echo.com/get?foo1=bar1&foo2=bar2"

# BASIC Authentication
API_USERNAME = 'postman' 
API_PASSWORD = 'password'

# Here we define the headers
headers = {'content-type' : 'application/vnd.json+api'}

# Sending GET request and saving response as response object 
r = requests.get(url, headers=headers, auth=(API_USERNAME, API_PASSWORD)) 

# Printing the response object
response = dir(r)
print("Response:%s"%response)
