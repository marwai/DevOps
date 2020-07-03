# Application Programme Interface
# WHat is it?
# Why Use is
# in python we have a module called request to interact with web-apis
# To install: pip install requests

import requests

#check HTTP/HTTPS 200 success - 400 - 404 page no found
response_bbc = requests.get("https://www.bbc.co.uk/")

print(response_bbc)
