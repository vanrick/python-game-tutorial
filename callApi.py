# Creating a simple AJAX call
import sys
import requests

# parameters = {
#     'lat': 40.71,
#     'lon':-74
# }
# response = requests.get('http://api.open-notify.org/iss-pass.json', params=parameters)

# data = response.json()
# # print(type(data))
# # print(data)
# print(response.headers['Content-Type'])

# Finding the number of people in space

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
# print(data)
# print('number of people ',data['number'])
# print('peoples names ',data['people'][1])
peoplesNames = data['people']
for name in peoplesNames:
    print(name['name'])
