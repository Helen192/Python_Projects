import requests
from datetime import datetime

USERNAME = "helen123"
TOKEN = "1234567890"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "phuong123"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# 1. Create your user account
#response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
#print(response.text)

# 2. Create a graph definition
graph_config = {
    "id": GRAPH_ID,
    "name": "Yoga graph",
    "unit": "Minutes",
    "type": "int",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=header)
#print(response.text)

# 4. Post value to the graph
today = datetime.now()

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you exercise Yoga today?: "),
}

pixel_endpoint = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=header)
print(response.text)

# 5. Update the pixel
day_update = datetime(year=2022, month=2, day=27).strftime("%Y%m%d")
day_update_endpoint = f"{pixel_endpoint}/{day_update}"
quantity_parameter = {
    "quantity": "70"
}

#response = requests.put(url=day_update_endpoint, json=quantity_parameter, headers=header)
#print(response.text)

# 6. Delete an existed pixel
#response = requests.delete(day_update_endpoint, headers=header)
#print(response.text)