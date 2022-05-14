import requests
from twilio.rest import Client

account_sid = "AC7dda47a69e1cf63f4d9b99c62e2c475d"   # copy from my own twilio account
auth_token = "bd93105925ceee4ebaf2241984bc4593"     # copy from my own twilio account

#API key of openwearthermap.org
api_key = "cef4ca24f80e699dce75a1243b2beb03"

# check lat and log at website latlong.net
MY_LATITUDE = 51.481846
MY_LONGITUDE = 7.216236
parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
response = requests.get(url=OWN_ENDPOINT, params=parameters)
response.raise_for_status()
# parse weather data from API to json file
weather_data = response.json()

##TODO: Check if the weather data in the next 12 hour can be rainly, then print the message of "Bring an Umbrella"
# copy the first 12 elements of list "hourly" into a new list
weather_12_hours = weather_data["hourly"][0:12]
print(weather_12_hours)

# check if any hour with id less than 700, then print the message of "Bring an Umbrella"
will_rain = False
for hour in weather_12_hours:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+19108385518',
        to='+4917624679967'
    )

    print(message.status)



