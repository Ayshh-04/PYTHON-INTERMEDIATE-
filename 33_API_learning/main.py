import requests

#api Endpoint 
#Api request 
#Api Parameter
response=requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#1xx -hold on 2xx -here you go 3xx-not allowed 4xx -not found 5xx servr down

# print(response.status_code)

# if response.status_code ==404:
#     raise Exception("That page doesnot found")

#instead of doing this for every status code exception we can dop
response.raise_for_status()

data=response.json()["iss_position"]
longitude=data["longitude"]
latitude=data["latitude"]
iss_position=(longitude,latitude)

