import requests
print("Welcome to the Weather Forecasting Platform")
city=input("Enter the City Name you want the forecast for: ")

url='http://api.openweathermap.org/data/2.5/forecast?units=metric&appid=5f1aaab27154e9d7a4c6e81336e9266a&q='

resurl = url + city
data=requests.get(resurl).json()

for (k,v) in data.items():
    print('key: {}'.format(k))
    print('value: {}'.format(v))
