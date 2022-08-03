import requests
from datetime import datetime

my_lat = 20.5937
my_lng = 78.9629

parameter = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter, verify=False)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(datetime.now().hour)
