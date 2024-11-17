from weather_fetcher import get_weather
from weather_publisher import publish_weather
import os
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

api_key = os.getenv('WEATHER_API_KEY')
location = f'{os.getenv("WEATHER_ZIP", "19460")} US'
mqtt_host = os.getenv('MQTT_HOST', 'homepi3')
mqtt_username = os.getenv('MQTT_USERNAME', 'home-metrics')
mqtt_password = os.getenv('MQTT_PASSWORD', 'woodlawn')
weather_topic = os.getenv('WEATHER_TOPIC')

try:
    weather_data = get_weather(location, api_key)
    publish_weather(mqtt_host, weather_topic, mqtt_username, mqtt_password, weather_data)
except Exception as err:
    logging.error(err)