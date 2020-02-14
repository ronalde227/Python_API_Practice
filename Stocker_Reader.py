import sys
import os
import urllib
import json

from urllib import request


print("STOCK READER 2019")

print(dir(request))

API_KEY = "L8RUF6TZTHWE2W11"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo'
json_obj = request.urlopen(url)
print("The json code", json_obj.code)

data = json.load(json_obj)

#print(data)
'''
print("2. The type is : ", type(data))
print("3. The keys are :" ,data.keys())

print("4. The values are :" ,data.values())
print("4.1 Meta data is a ", type(data['Meta Data']['1. Information']) )
print ("4.2 ", data['Meta Data']['1. Information'])
print("5. Getting ", data['Meta Data'])
print("6. The length of data is ", len(data))
'''

print("data keys :", data.keys())

print("The symbol is :", data['Meta Data']['2. Symbol'])
print("Time Series type is :", type(data['Time Series (Daily)']))
print("The time frame is :", data['Time Series (Daily)'])
print("The key of time frame is:", data['Time Series (Daily)'].keys() )
#print("The type of 2019", type(data['Meta Data']['Time Series (Daily)']))
print('The type is :', type(data['Time Series (Daily)'].get('2019-09-27')))
print('The 2019 - 9 - 27  :', data['Time Series (Daily)'].get('2019-09-27'))
print(type(data['Time Series (Daily)'].get('2019-09-27').get("1. open")))
count = 0
for key, value in data['Time Series (Daily)'].items():
    print(key)
    print(type(value))
    for ke, val in value.items():
        print(ke)
        print(val)

    count += 1
    if count == 3:
        break

'''
for key, value1  in data['Time Series (Daily)'].items():
    for value2 in data['Time Series(Daily)'].values()'''
