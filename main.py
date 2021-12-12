from dotenv import load_dotenv
import os
import requests
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

# Your Details
GENDER = "male"
WEIGHT_KG = 81
HEIGHT_CM = 180
AGE = 24

# Nutritionix endpoint and header
NUTRITIONIX_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutix_headers = {
    "x-app-id": os.getenv("NUTRITIONIX_API_ID"),
    "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
}

exercise_text = input("What exercise did you do?: ")
print(f"Query: {exercise_text}")

nutix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutix_response = requests.post(url=NUTRITIONIX_END_POINT, json=nutix_params, headers=nutix_headers)
nutix_response.raise_for_status()
data = nutix_response.json()['exercises']
print(f"Response text: {nutix_response.text}")

# Current date and time in dd/mm/yyyy and hh:mm:ss resp.
now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
today_time = now.strftime("%H:%M:%S")

# Sheety API

SHEETY_END_POINT = "https://api.sheety.co/90203dcb0b578ada8862d86b9cefcc1e/workoutTracking/workouts"

bearer_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
}

print(f"bearer token: {bearer_headers}")

for exercise in data:
    workout = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=SHEETY_END_POINT, json=workout, headers=bearer_headers)
    print(f"Response: {sheety_response.json()}")
