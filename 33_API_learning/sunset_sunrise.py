import requests


# iss_response=requests.get(url="http://api.open-notify.org/iss-now.json")
# iss_response.raise_for_status()
# data=iss_response.json()["iss_position"]
# longitude=data["longitude"]
# latitude=data["latitude"]
# response=requests.get(f"https://api.sunrise-sunset.org/v2?lat={latitude}&lng={longitude}").json()
# print(f"""Date: {response["date"]},
#       sunrise:{response["sunrise"]},
#       sunset:{response["sunset"]}""")

MY_LAT=51.507351
MY_LNG=-0.127758
parameter={
    "lat": MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}
response=requests.get(f"https://api.sunrise-sunset.org/v2",params=parameter)