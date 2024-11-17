import requests
import logging

url = 'https://api.tomorrow.io/v4/weather/realtime'
headers = {'accept': 'application/json'}

def get_weather(location, api_key):
    logging.info(f"Retrieving weather data for {location}")
    response = requests.get(f'{url}?location={location}&apikey={api_key}', headers=headers).json()
    # Handle error codes as they are not standard for this endpoint
    if 'code' in response and str(response['code'])[:1] != '2':
        raise Exception(response)
    logging.info("Successfully retrieved weather data")
    return str(response)
