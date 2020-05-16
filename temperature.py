import requests

city = input("Enter City Name:")
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cff9c23c0022d8edc49c00321eb4104b&units=metric')
d = r.json()
print("Temperature for city",city,"is",d["main"]["temp"])


