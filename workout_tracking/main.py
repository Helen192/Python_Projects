import requests
from datetime import datetime

# API nutritionix.com
API_ID = "08b6539c"
API_KEY = "355ec8822898b51ffc4f88754f4618f7"

# ENDPOINTs
nutrients_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exercises_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/5aa970bf038b3ee49fababde2a2e5366/workoutTracking/workouts"

GENDER = "female"
WEIGHT_KG = 45
HEIGHT_CM = 153
AGE = 29

HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

# ask for exercises that user did
exercies_query = input("Tell me which exercises you did? ")
exercise_params = {
    "query": exercies_query,
    "gender" : GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercises_response = requests.post(exercises_endpoint, json=exercise_params, headers=HEADERS)
result = exercises_response.json()["exercises"]


# get the current time in form of dd/mm/yyyy
today = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")


# saving data into the google spreadsheet
for exercise in result:
    post_params = {
        'workout':{
            'date': today,
            'time': today_time,
            'exercise': exercise["user_input"].title(),
            'duration': exercise["duration_min"],
            'calories': exercise["nf_calories"]
        }
    }
    response = requests.post(sheety_endpoint, json=post_params)


# get data from the google spreadsheets and turn it into json file
sheet_info = requests.get(sheety_endpoint)
json_result = sheet_info.json()
print(json_result)