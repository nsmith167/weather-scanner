import json
from datetime import datetime, timezone
import os

def to_message(data):
    data = data['data']['values']
    message = {
        'timestamp': str(datetime.now(timezone.utc).isoformat()),
        'zip': os.getenv('WEATHER_ZIP'),
        'cloud_cover': data['cloudCover'],
        'temperature':  data['temperature'],
        'temperature_apparent': data['temperatureApparent'],
        'humidity': data['humidity']
    }
    return json.dumps(message)
    