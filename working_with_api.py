import requests


url = "https://morningstar1.p.rapidapi.com/dividends"

querystring = {"Ticker":"IOC","Mic":"XNSE"}

headers = {
    'accept': "string",
    'x-rapidapi-key': "5015d61e13mshcbb3771deca7b37p19c7c8jsnc900286d0d7b",
    'x-rapidapi-host': "morningstar1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
"""
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

querystring = {"symbol":"AMRN","region":"US"}

headers = {
    'x-rapidapi-key': "5015d61e13mshcbb3771deca7b37p19c7c8jsnc900286d0d7b",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"

querystring = {"uuid":"9803606d-a324-3864-83a8-2bd621e6ccbd","region":"US"}

headers = {
    'x-rapidapi-key': "5015d61e13mshcbb3771deca7b37p19c7c8jsnc900286d0d7b",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

response = requests.get('https://randomfox.ca/floof')

# will return 200 if everything goes OK
print(response.status_code)

# will return the response text
# print(response.text)

# will return data in a dictionary format
print(response.json())

fox = response.json()

print(fox['image'])
"""
