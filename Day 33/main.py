import requests
from datetime import datetime


MY_LAT = 41.008240
MY_LONG = 28.978359

response=requests.get(url="http://api.open-notify.org/iss-now.json")
data=response.json()

iss_latitude =float(data["iss_position"]["latitude"])
iss_longitude =float(data["iss_position"]["longitude"])


parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
value = response.json()
sunrise = int(value["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(value["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()
print(sunrise)
print(sunset)

now_time=time_now.hour

if now_time >= sunset:
    if MY_LAT-iss_latitude <= 5 and MY_LONG-iss_longitude<=5:
        print("E mail sended ")