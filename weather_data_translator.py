import json
import os
import time
import logging

def to_persistence_model(data):
    data = data['data']['values']
    persistence_data = {
        'device': os.getenv("DEVICE_NAME"),
        'timestamp': int(time.time()),
        'measurements': [
            'cloud_cover',
            'temperature',
            'temperature_apparent'
            'humidity'
        ],
        'values' : [
            data['cloudCover'],
            data['temperature'],
            data['temperatureApparent'],
            data['humidity']
        ]
    }
    return json.dumps(persistence_data)
    