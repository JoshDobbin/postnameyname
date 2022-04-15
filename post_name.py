#!/bin/python3
# importing the requests library
import sys
import requests
  
# defining the api-endpoint 
API_ENDPOINT = "https://my-app-txjhu.ondigitalocean.app/namey/hello/" + sys.argv[1]


# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = {})
  
print("The pastebin URL is:%s"%r.text)