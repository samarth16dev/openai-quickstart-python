import requests


def find_temp(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    response = requests.get(url)

    data = response.json()
    return data["current"]["temperature_2m"]

#type(data)

#data.keys()

#data["current"]["temperature_2m"]

foundTemp = find_temp(23.81,86.44)
print(f"Indian temperature: {foundTemp}")

