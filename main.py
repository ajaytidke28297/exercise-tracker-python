import requests
from dotenv import load_dotenv
import os

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

exercise = input("What exercise did you do?: ")
print(f"Query: {exercise}")

nutix_params = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_END_POINT, json=nutix_params, headers=nutix_headers)
print(f"Response text: {response.text}")
