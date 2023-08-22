import requests

# url = 'http://localhost:5000/payments'
# data = {
#     "date": "2023.04.01",
#     "amount": 100.50
# }
# headers = {'Content-Type': 'application/json'}
# response = requests.post(url, json=data, headers=headers)
# print(response.json())

# url = 'http://localhost:5000/payments'
# params = {'date1': '2023.01.01'}
# response = requests.get(url, params=params)
# print(response.json())

# url = 'http://localhost:5000/payments'
# params = {'date1': '2023.01.01', 'date2': '2023.12.31'}
# response = requests.get(url, params=params)
# print(response.json())

url = 'http://localhost:5000/payments/1'
params = {'date': '2023.06.03', 'amount': 150}
response = requests.put(url, json=params)
print(response.json())
