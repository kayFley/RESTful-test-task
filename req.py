import requests

url = 'http://localhost:5000/payments'

# data = {
#     "date": "2023.04.01",
#     "amount": 100.50
# }
# headers = {'Content-Type': 'application/json'}
# response = requests.post(url, json=data, headers=headers)
# print(response.json())

# params = {'date1': '2023.01.01'}
# response = requests.get(url, params=params)
# print(response.json())

params = {'date1': '2023.01.01', 'date2': '2023.12.31'}
response = requests.get(url, params=params)
print(response.json())
