import requests

url = "https://api.opensea.io/api/v1/assets?order_by=pk&order_direction=desc&limit=20&include_orders=true"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)
